#!/bin/env python3
from __future__ import print_function

import os
import re
import shlex
import sys

import pygments

from IPython.utils.text import marquee
from IPython.utils import openpy
from IPython.utils import py3compat

__all__ = ['Demo', 'LineDemo', 'DemoError']

class DemoError(Exception):
    pass

def re_mark(mark):
    return re.compile(r'^\s*#\s+<demo>\s+%s\s*$' % mark, re.MULTILINE)

class Demo(object):

    re_stop = re_mark('-*\s?stop\s?-*')
    re_silent = re_mark('silent')
    re_auto = re_mark('auto')
    re_auto_all = re_mark('auto_all')

    def __init__(self, src, title='', arg_str='', auto_all=None):
        if hasattr(src, "read"):
            # It seems to be a file or a file-like object
            self.fname = "from a file-like object"
            if title == '':
                self.title = "from a file-like object"
            else:
                self.title = title
        else:
            # Assume it's a string or something that can be converted to one
            self.fname = src
            if title == '':
                (filepath, filename) = os.path.split(src)
                self.title = filename
            else:
                self.title = title

        self.sys_argv = [src] + shlex.split(arg_str)
        self.auto_all = auto_all
        self.src = src

        self.inside_ipython = "get_ipython" in globals()

        self.formatter = pygments.formatters.get_formatter_by_name(
            "16m",
            style="colorful")
        self.rst_lexer = pygments.lexers.get_lexer_by_name("rst")
        self.python_lexer = pygments.lexers.get_lexer_by_name("py3")

        if self.inside_ipython:
            ip = get_ipython()
            self.ip_ns = ip.user_ns
            self.ip_showtb = ip.showtraceback
            self.ip_run_cell = ip.run_cell
            self.shell = ip

        self.reload()

    def highlight(self, block):
        tokens = pygments.lex(block, self.python_lexer)
        toks = []
        for token in tokens:
            if token[0] == pygments.token.Token.String.Doc and len(token[1]) > 6:
                toks += pygments.lex(token[1][:3], self.python_lexer)
                toks += pygments.lex(token[1][3:-3], self.rst_lexer)
                toks += pygments.lex(token[1][-3:], self.python_lexer)
            elif token[0] == pygments.token.Token.Comment.Single:
                toks.append((pygments.token.Token.Comment.Single, token[1][0]))
                toks += list(pygments.lex(token[1][1:], self.rst_lexer))[:-1]
            else:
                toks.append(token)
        return pygments.format(toks, self.formatter)

    def fload(self):
        """Load file object."""
        # read data and parse into blocks
        if hasattr(self, 'fobj') and self.fobj is not None:
            self.fobj.close()
        if hasattr(self.src, "read"):
            # It seems to be a file or a file-like object
            self.fobj = self.src
        else:
            # Assume it's a string or something that can be converted to one
            self.fobj = openpy.open(self.fname)

    def reload(self):
        self.fload()

        self.src = "".join(openpy.strip_encoding_cookie(self.fobj))
        src_b = [b.strip() for b in self.re_stop.split(self.src) if b]
        self._silent = [bool(self.re_silent.findall(b)) for b in src_b]
        self._auto = [bool(self.re_auto.findall(b)) for b in src_b]

        # if auto_all is not given (def. None), we read it from the file
        if self.auto_all is None:
            self.auto_all = bool(self.re_auto_all.findall(src_b[0]))
        else:
            self.auto_all = bool(self.auto_all)

        # Clean the sources from all markup so it doesn't get displayed when
        # running the demo
        src_blocks = []
        auto_strip = lambda s: self.re_auto.sub('', s)
        for i, b in enumerate(src_b):
            if self._auto[i]:
                src_blocks.append(auto_strip(b))
            else:
                src_blocks.append(b)
        # remove the auto_all marker
        src_blocks[0] = self.re_auto_all.sub('', src_blocks[0])

        self.nblocks = len(src_blocks)
        self.src_blocks = src_blocks

        # also build syntax-highlighted source
        self.src_blocks_colored = list(map(self.highlight, self.src_blocks))

        # ensure clean namespace and seek offset
        self.reset()

    def reset(self):
        self.user_ns = {}
        self.finished = False
        self.block_index = 0

    def _validate_index(self, index):
        if index < 0 or index >= self.nblocks:
            raise ValueError('invalid block index %s' % index)

    def _get_index(self, index):
        if index is None:
            if self.finished:
                print('Demo finished.  Use <demo_name>.reset() if you want to rerun it.')
                return None
            index = self.block_index
        else:
            self._validate_index(index)
        return index

    def seek(self, index):
        if index < 0:
            index = self.nblocks + index
        self._validate_index(index)
        self.block_index = index
        self.finished = False

    def back(self, num=1):
        self.seek(self.block_index - num)

    def jump(self, num=1):
        self.seek(self.block_index + num)

    def again(self):
        self.back(1)
        self()

    def edit(self, index=None):

        index = self._get_index(index)
        if index is None:
            return
        # decrease the index by one (unless we're at the very beginning), so
        # that the default demo.edit() call opens up the sblock we've last run
        if index > 0:
            index -= 1

        filename = self.shell.mktempfile(self.src_blocks[index])
        self.shell.hooks.editor(filename, 1)
        with open(filename, 'r') as f:
            new_block = f.read()
        # update the source and colored block
        self.src_blocks[index] = new_block
        self.src_blocks_colored[index] = self.highlight(new_block)
        self.block_index = index
        # call to run with the newly edited index
        self()

    def show(self, index=None):

        index = self._get_index(index)
        if index is None:
            return

        print(self.marquee('<%s> block # %s (%s remaining)' %
                           (self.title, index, self.nblocks - index - 1)))
        print(self.src_blocks_colored[index])
        sys.stdout.flush()

    def show_all(self):

        fname = self.title
        title = self.title
        nblocks = self.nblocks
        silent = self._silent
        marquee = self.marquee
        for index, block in enumerate(self.src_blocks_colored):
            if silent[index]:
                print(marquee('<%s> SILENT block # %s (%s remaining)' %
                              (title, index, nblocks - index - 1)))
            else:
                print(marquee('<%s> block # %s (%s remaining)' %
                              (title, index, nblocks - index - 1)))
            print(block, end=' ')
        sys.stdout.flush()

    def run_cell(self, source):

        exec(source, self.user_ns)

    def __call__(self, index=None):

        index = self._get_index(index)
        if index is None:
            return
        try:
            marquee = self.marquee
            next_block = self.src_blocks[index]
            self.block_index += 1
            if self._silent[index]:
                print(marquee('Executing silent block # %s (%s remaining)' %
                              (index, self.nblocks - index - 1)))
            else:
                self.pre_cmd()
                self.show(index)
                if self.auto_all or self._auto[index]:
                    print(marquee('output:'))
                else:
                    print(marquee('Press <q> to quit, <Enter> to execute...'),
                          end=' ')
                    ans = py3compat.input().strip()
                    if ans:
                        print(marquee('Block NOT executed'))
                        return
            try:
                save_argv = sys.argv
                sys.argv = self.sys_argv
                self.run_cell(next_block)
                self.post_cmd()
            finally:
                sys.argv = save_argv

        except:
            if self.inside_ipython:
                self.ip_showtb(filename=self.fname)
        else:
            if self.inside_ipython:
                self.ip_ns.update(self.user_ns)

        if self.block_index == self.nblocks:
            mq1 = self.marquee('END OF DEMO')
            if mq1:
                print()
                print(mq1)
                print(self.marquee('Use <demo_name>.reset() if you want to rerun it.'))
            self.finished = True

    def marquee(self, txt='', width=78, mark='*'):
        return marquee(txt, width, mark)

    def pre_cmd(self):
        pass

    def post_cmd(self):
        pass

class LineDemo(Demo):

    def reload(self):
        # read data and parse into blocks
        self.fload()
        lines = self.fobj.readlines()
        src_b = [l for l in lines if l.strip()]
        nblocks = len(src_b)
        self.src = ''.join(lines)
        self._silent = [False] * nblocks
        self._auto = [True] * nblocks
        self.auto_all = True
        self.nblocks = nblocks
        self.src_blocks = src_b

        # also build syntax-highlighted source
        self.src_blocks_colored = list(map(self.highlight, self.src_blocks))

        # ensure clean namespace and seek offset
        self.reset()

class ClearMixin:

    def marquee(self, txt='', width=78, mark='*'):
        return ''

    def pre_cmd(self):
        # FIXME: Qtconsole does not support `clear` \033[J\033[H
        print("\033[2J\033[H")

class ClearDemo(ClearMixin, Demo):
    pass

class ClearIPLineDemo(ClearMixin, LineDemo):
    pass


def qtconsole_fix():
    try:
        # Enable blod text
        import qtconsole.ansi_code_processor
        qtconsole.ansi_code_processor.AnsiCodeProcessor.bold_text_enabled = \
            True
    except:
        pass

def slide(file):
    qtconsole_fix()
    demo = ClearDemo(demo_file)
    while not demo.finished:
        demo()
        input('\n...')

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        demo_file = sys.argv[1]
    else:
        demo_file = "demo.py"
    slide(demo_file)
