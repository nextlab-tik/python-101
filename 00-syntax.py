# <demo> -------------------------------- stop --------------------------------

"""
Hello `Python` course!
let's enjoy coding!
.. raw:
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
Pourquoi python
```````````````

- C'est plus  simple  pour  bien debuter
- multi-plateforme
- orienté objet , procédurale, fonctionnelle
- langage interpreté
"""

# <demo> -------------------------------- stop --------------------------------

"""
Domaines d'application
``````````````````````

- des petits scripts utilitaires afin d'automatiser les taches
- des applications graphiques(GTK,QT)
- les jeux vidéo
- la programmation web  (Django, Flask)
- la recherche scientifique(Numpy, SciPy, Matplotlib)
- administrateur systèmes et securité
"""

# <demo> -------------------------------- stop --------------------------------

"""
types intégrés
~~~~~~~~~~~~~~


:NOTE 1: Python est un  langage non typé
:NOTE 2: sans `;` a la fin
:Note 3: sensible aux majuscules et minuscules
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

# :NOTE 3: le type char dans python est un string qui possede un seul caractere

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
==========================
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
Les opérations sur le type string  (1/2)
========================================
"""

x = 'Hello!' + ' ' + 'World!'
print(x)

x = x + '!'

# :Warnin:

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

# :NOTE 4: input retourne toujours une chaine de caractére

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
affectation multiple
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
    on donne: U(0), U(1), U(2) d'une suite arithmethique, trouver  U(x), U(y),
    U(z) de x, y, z donnés respectivement
"""

# <demo> -------------------------------- stop --------------------------------

"""
SOLUTION 1
~~~~~~~~~~
"""

u0 = int(input())
u1 = int(input())
u2 = int(input())

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
--------
"""

if True:
    print("hi")

# :NOTE 5: pas des paranthéses `()`, just `:` pour separer la condition et le traitement

# :NOTE 6: pas  des accolades `{}` , mais tabulation (tab, ou 2, 4 spaces)

if 5 % 2 == 0:
    print("paire")
else:
    print("impaire")


# <demo> -------------------------------- stop --------------------------------

"""
IF (2/3)
--------
"""

if True and 5 % 2 == 0:
    print("cond 1")
elif False or 5 % 2 == 0:
    print("cond 2")
else:
    print("cond 3")


# <demo> -------------------------------- stop --------------------------------

"""
Les opérateurs booleéns
=======================
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
--------
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
"""
LIST
===
"""
list = ["ali", "sami", "rami", "xxx"]
list
print(list[0])
print(list[-1])
list + ["hela", "fatma"]
list
i = 0
for s in list:
    print(i, s)
    i += 1
print(len(list))
list.append("fatma")
print(len(list))
list.append("hela")
print(len(list), list[-1])

# <demo> -------------------------------- stop --------------------------------
"""
String
======
"""
ch = 'hi'
print(ch)
print(type(ch))
ch1 = 'hello'
ch2 = 'hello'
if ch1 is ch2:
    print('equal')
else:
    print('different ! ')
print(len(ch))
word = 'python'
print(word[0])
print(word[-1])
print(word[-2])
print(word[4])
print(word[0:2])  # caractere 0 , 1, 2

# <demo> -------------------------------- stop --------------------------------

"""
FOR
===
"""

for i in range(10):
    print(i)
mots = 'je suis parfait'
for lettre in mots:
    print(lettre)
list = ['mohamed', 'ali', 'salah', 'fedi']
for element in list:
    print(element)
for i in range(len(element)):
    print(i, '->', list[i])

# <demo> -------------------------------- stop --------------------------------

"""
Rappel
======

- types
- casting
- operations
- print & input
- expression booléen
- if
- list
- for
"""

# <demo> -------------------------------- stop --------------------------------

"""
Range
=====
"""

# :Example:

# de 0 jusqu'à 4

for i in range(5):
    print(i)

# de 5 jusqu'à 9

for i in range(5, 10):
    print(i)

# de 0 jusqu'à 9 avec un step de 2

for i in range(0, 10, 2):
    print(i)

# decroissant

for i in range(10, 0, -1):
    print(i)

# <demo> -------------------------------- stop --------------------------------

"""
While
=====
"""

i = 0
while i < 5:
    print(i)
    i += 1

# <demo> -------------------------------- stop --------------------------------

"""
Do While
========

:Warning: non implémenté en Python
"""

# <demo> -------------------------------- stop --------------------------------

"""
Excercice
=========

saisir un entier x dans l'intervalle [2..8]

:Note 6: Le but est de supporté la boucle tant que :)
"""


# <demo> -------------------------------- stop --------------------------------

"""
Solution
========
"""

while True:
    x = int(input("donner un entier entre 2 et 8 : "))
    if x > 2 and x < 8:
        break

# <demo> -------------------------------- stop --------------------------------

"""
Continue
========
"""

for i in range(2, 10):
    if i % 2 == 0:
        continue
    print(i)


# <demo> -------------------------------- stop --------------------------------

"""
Pass
====
"""

while True:
    pass


class test:
    pass


def fn():
    pass

# <demo> -------------------------------- stop --------------------------------

"""
Function (1/3)
==============
"""


def hi():
    print("hello python")
hi()


def salut(name):
    print("Hello", name)

salut("imen")
salut("ali")

# <demo> -------------------------------- stop --------------------------------

"""
Function (2/3)
==============

Valeur par default
"""


def hi(name="firas"):
    print(name)

hi()
hi("sahar")


def hii(num, name="firas"):
    print(num, name)

hii(5)
hii(5, "sahar")

# <demo> -------------------------------- stop --------------------------------

"""
Function (3/3)
==============

Positional Arg vs. Keyword Arg
"""


def hi(nom, prenom):
    print("Hi", nom, prenom)

# Positional Args

hi("firas", "chaaben")

# Keyword Args

hi(nom="firas", prenom="chaaben")
hi(prenom="chaaben", nom="firas")

# <demo> -------------------------------- stop --------------------------------

"""
Lambda (Functional programming)
===============================
"""

f = lambda x: x ** 2
print(f(5))


def execute(f, x):
    print(f(x))

execute(f, 5)
execute(lambda x: x ** 2, 5)


# <demo> -------------------------------- stop --------------------------------

"""
String Functions
================
"""

s = "  hello! world!  "
len(s)
s = s.strip()
s.upper()
s.lower()
s.capitalize()
s.title()
s.center(50, '*')
s[0].isalnum()

# <demo> -------------------------------- stop --------------------------------

"""
String Formatting
=================
"""

# Old-fashion

'%s %d %.5f' % ('mot', 5, 9.2)

# Python way

'Hi {} !'.format('firas')
'Hi {nom} {prenom} !'.format(prenom='chaaben', nom='firas')
'first element {tab[0]}'.format(tab=[1, 2, 3])
'dec = {0}, bin = {0:b}, hex = {0:x}, oct = {0:o}'.format(15)
'ljust: {0:<10}, center: {0:^10}, rjust: {0:>10}'.format('hi')

# <demo> -------------------------------- stop --------------------------------

"""
Built-in Function
=================

- dir / help
- sum / max / min
- hex / bin / oct
- chr / ord
- abs / pow / round
"""

# <demo> -------------------------------- stop --------------------------------

"""
Class
=====
"""


class Demo1:
    pass

d = Demo1()


class Demo2:

    def __init__(self):
        print("new Demo")

d = Demo2()


class Demo3(Demo2):

    def hi(self):
        print("Hi")

d = Demo3()
d.hi()

# <demo> -------------------------------- stop --------------------------------

"""
Tuple
=====
"""

t = (1, 2)
t = (1,)

# <demo> -------------------------------- stop --------------------------------

"""
Set
===
"""

s = {1, 2, 3, 2}
print(s)
s.add(2)
s.add(5)

{1, 2, 3} - {1, 2}  # difference
{1, 2, 3} & {2}     # intersection
{1, 2, 3} | {4}     # union
{1, 2, 3} ^ {2, 4}  # difference symmetric
{1} < {1, 2, 3}     # sous-ensemble ?

# <demo> -------------------------------- stop --------------------------------

"""
Dict
====
"""

d = {"nom": "Firas", "prenom": "chaaben", "age": 90}
print(d["nom"])
d["age"] = 80
len(d)
"nom" in d

# <demo> -------------------------------- stop --------------------------------

"""
Python Philosophies
~~~~~~~~~~~~~~~~~~~
"""

import this

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
