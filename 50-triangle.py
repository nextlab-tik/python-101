"""
:Question:
    Ecrire une fonction qui permet d'afficher un triangle de hauteur donné
:Exemple:
>>> triangle(3)
  *
 ***
*****
>>> triangle(5)
    *
   ***
  *****
 *******
*********
"""


def triangle(hauteur):
    base = (hauteur * 2) - 1
    for l in range(hauteur):
        etoiles = '*' * (l * 2 + 1)
        print(etoiles.center(base))


def triangle2(hauteur):
    for i in range(1, hauteur+1):
        print(' ' * (hauteur - i) + '*' * (i * 2 - 1))


triangle(3)
triangle(5)

triangle2(3)
triangle2(5)
