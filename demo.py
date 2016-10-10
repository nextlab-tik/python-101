# <demo> -------------------------------- stop --------------------------------

"""
Hello **MTCFSS** members to the `MTCFSS Start with Python` course!
let's enjoy coding!
::
                               [1;34m.iiiiiiiiii.[m
                             [1;34m.ii``iiiiiiiiii.[m
                             [1;34miii..iiiiiiiiiii[m
                             [1;34m````````iiiiiiii[m
                     [1;34m.iiiiiiiiiiiiiiiiiiiiiii[m [1;33miiiiiii,[m
                  [1;34m.iiiiiiiiiiiiiiiiiiiiiiiiii[m [1;33miiiiiiiii.[m
                  [1;34miiiiiiiiiiiiiiiiiiiiiiiiiii[m [1;33miiiiiiiiii[m
                  [1;34miiiiiiiiiiiiiiiiiiiiiiiiiii[m [1;33miiiiiiiiii[m
                  [1;34miiiiiiiiii[m [1;33m,,,,,,,,,,,,,,,,,iiiiiiiiii[m
                  [1;34miiiiiiiiii[m [1;33miiiiiiiiiiiiiiiiiiiiiiiiiii[m
                  [1;34m`iiiiiiiii[m [1;33miiiiiiiiiiiiiiiiiiiiiiiiii`[m
                     [1;34m`iiiiii[m [1;33miiiiiiiiiiiiiiiiiiiiiii`[m
                             [1;33miiiiiiii,,,,,,,,[m
                             [1;33miiiiiiiiiii``iii[m
                             [1;33m`iiiiiiiiii..ii`[m
                               [1;33m`iiiiiiiiii`[m
                     ____        _   _
                    |  _ \ _   _| |_| |__   ___  _ __
                    | |_) | | | | __| '_ \ / _ \| '_ \
                    |  __/| |_| | |_| | | | (_) | | | |
                    |_|    \__, |\__|_| |_|\___/|_| |_|
                           |___/
"""

# <demo> -------------------------------- stop --------------------------------

"""
Why Python
``````````

- Easy to start with
- Cross-platform
- Multi pattern: Object-Oriented, Procedural, Fonctional
- Interpreted language
"""

# <demo> -------------------------------- stop --------------------------------

"""
Use cases
`````````

- Small scripts and automitization
- Dekstop apps (GTK, Qt)
- Games: engine, and scripting
- Web server (Django, Flask)
- Scientific (Numpy, SciPy, Matplotlib)
- Security and Sysadmin
"""

# <demo> -------------------------------- stop --------------------------------

"""
Builtin types
~~~~~~~~~~~~~


:NOTE 1: Python is a non-typed language (variables are declared without specifying the type)
:NOTE 2: There is not `;` in Python
"""

# :Example:

x = 5
y = 'Hello! World!'
z = True

# :Example:

x = 5
x = 'Hello! World!'


# <demo> -------------------------------- stop --------------------------------

"""
Builtin types
=============

Numbers
-------
"""

x = 1
x = 1.5
x = -1


# <demo> -------------------------------- stop --------------------------------

"""
String (Chaine de caracteres)
-----------------------------
"""

# :Example:

x = 'Hello! World!'
x = "Salut"
x = """ciao"""

# :Example:

x = "line 0\nline 1\nline 2"
x = """line 0
line 1
line 2"""

# :NOTE 3: type char in python is just String with  1 character

x = "A"
x = 'a'

# <demo> -------------------------------- stop --------------------------------

"""
Boolean
-------
"""

x = True
y = False


# <demo> -------------------------------- stop --------------------------------

"""
Print
=====
"""

print('Hello! World!')
print(5)
x = 1
print(x)
print(True, 5)

# <demo> -------------------------------- stop --------------------------------

"""
Operators in Numbers (1/3)
==========================
"""

x = 1 + 2
print(x)
print(2 + 1.3)

x = 1 * 8
x = 1 - 1

print(4 / 2)
x = 4 / 3
x = 5 % 2

# <demo> -------------------------------- stop --------------------------------

"""
Operators in Numbers (2/3)
==========================
"""

print(5 // 2)

print(2 ** 8)

x = 1
y = 2
z = x + y
print(z)
print(4 * 9 + 5)

# <demo> -------------------------------- stop --------------------------------

"""
Operators in Numbers (3/3)
=========================
"""

x = 1
x += 5
print(x)
x -= 3
print(x)
x *= 9
print(x)
x %= 2
print(x)


# <demo> -------------------------------- stop --------------------------------

"""
Operators in String (1/2)
=========================
"""

x = 'Hello!' + ' ' + 'World!'
print(x)

x = 'Hello!'  ' '  'World!'
print(x)

x = x + '!'

x = '1' + 1

# <demo> -------------------------------- stop --------------------------------

"""
Operators in String (2/2)
=========================
"""

pinution = "I will do my homework \n" * 10
print(pinution)

x = 'Hello world !'
print(x[0])
print(x[-1])

# <demo> -------------------------------- stop --------------------------------

"""
Input
=====
"""

x = input("Donnez une chaine: ")
print(x)
x = input("Donnez un entier: ")
print(x)

# :NOTE 4: input donner toujours une chaine de caractere

x = int(input("Donnez un entier: "))
print(x)

# <demo> -------------------------------- stop --------------------------------

"""
Type Casting
============
"""

print(int("1"))
print(str(2.5))
print(bool(1))
print(bool(0))
print(bool("0"))
print(bool(""))


# <demo> -------------------------------- stop --------------------------------

"""
Multiple Affectation
====================
"""

x = 1
y = 2
x, y = y, x
print("x =", x, "y =", y)
x, y = 5, "string"


# <demo> -------------------------------- stop --------------------------------

"""
EXERCISE 1
~~~~~~~~~~
"""

"""
:Question:
    Given U(0), U(1), U(2) of suite arithmetique, donnez U(x), U(y),
    U(z) de x, y, z donnés respectivement
"""

# <demo> -------------------------------- stop --------------------------------

"""
SOLUTION 1
~~~~~~~~~~
"""

u0 = int(input())
u1 = int(input())
u3 = int(input())

add = u1 - u0

x = int(input())
y = int(input())
z = int(input())

print(u0 + add * x)
print(u0 + add * y)
print(u0 + add * z)


# <demo> -------------------------------- stop --------------------------------

"""
Blocks
======

IF (1/3)
-------
"""

if True:
    print("hi")

# :NOTE 5: pas (, ), just `:` pour separer la condition et le traitement

# :NOTE 6: pas {, } , mais identation (tab, ou 2, 4 spaces)

if 5 % 2 == 0:
    print("paire")
else:
    print("impaire")


# <demo> -------------------------------- stop --------------------------------

"""
IF (2/3)
-------
"""

if True and 5 % 2 == 0:
    print("cond 1")
elif False or 5 % 2 == 0:
    print("cond 2")
else:
    print("cond 3")


# <demo> -------------------------------- stop --------------------------------

"""
Boolean operators
=================
"""

5 == 5
5 != 4
5 < 6
5 >= 4
4 < 5 <= 6

5 == 6 and 6 % 2 or True

(5 == 6 and bool(6 % 2)) or True


# <demo> -------------------------------- stop --------------------------------

"""
IF (3/3)
-------
"""

if not False:
    print("True")

if 5 is 6:
    print("equal")
elif 5 is not 6:
    print("not equal")

if "c" in "abcdef":
    print("la chaine 'c' est sous-chaine de 'abcdef'")


# <demo> -------------------------------- stop --------------------------------

# EXERCISE

# TODO: check hacker rank

# <demo> -------------------------------- stop --------------------------------

"""
Python Philosophies
~~~~~~~~~~~~~~~~~~~
"""

éimport this

# <demo> -------------------------------- stop --------------------------------

"""
Python Philosophies
~~~~~~~~~~~~~~~~~~~

:Zen 1: Beautiful is better than ugly.

- Less punctuations, prefer English words
- keyword arguments
"""

# :Ugly:

# valid = form != null && form.is_valid(true)

# :Beautiful:

# is_valid = form is not None and form.is_valid(include_hidden_fields=True)

# <demo> -------------------------------- stop --------------------------------

"""
BONUS
#####
"""

import antigravity

# <demo> -------------------------------- stop --------------------------------

"""
Good vs. Bad habits (1/20)
==========================
"""

# :Bad:

s = "a" + " " + "simple" + " " + "example" + " " + "."

# :Good:

s = ' '.join(["a", "simple", "example", "."])

# <demo> -------------------------------- stop --------------------------------
"""
LIST
===
"""
list = ["ali","sami","rami","xxx"]
list
print(list[0])
print(list[-1])
list + ["hela","fatma"]
list
i=0
for s in list:
    print(i,s)
    i+=1
print(len(list))
list.append("fatma")
print(len(list))
list.append("hela")
print(len(list), list[-1])


# <demo> -------------------------------- stop --------------------------------
# LIST & STRING
# FOR
# WHILE & break, continue & pass
# BUILTIN FUNCTION (sum, reversed, sorted, ...)
# TYPES (dict, tuple, set, ...)
# FUNCTIONS & ARGS & KEYWORD ARGS
# GENERATOR & Comprehensions & PACKING & UNPACKING
# STANDARD FUNCTIONS (os, sys, datetime, re, math, timeit, json, ...)
# LAMBDA
# docstring
# unittest
# CLASS
# coding style
# exception
