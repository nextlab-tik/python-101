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
    largeur = (hauteur * 2) - 1
    for l in range(1, largeur + 1, 2):
        etoiles = '*' * l
        print(etoiles.center(largeur))
