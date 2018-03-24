"""
:Question:
    implement une ``do {} while ()`` pour forcer l'utilisateur à entrer un
    nombre entre 2 et 8
"""

# Sol 1 (not optimale & code dupliqué)
x = int(input())
while x not in range(2, 9):
    x = int(input())

# Sol 2 (code dupliqué)
x = int(input('donner un x'))
while not 2 <= x <= 8:
    x = int(input('donner un x'))

# Sol 3 (avec break)
while True:
    x = int(input("donner x"))
    if 2 <= x <= 8:
        break
