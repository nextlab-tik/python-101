"""
:Question:
    on donne un mot et la longeur du ligne
    centrer le mot au milieu de la ligne
"""

mot = input()
long = int(input())

print("SOL 1")
# print les espaces en gauche
for i in range((long - len(mot)) // 2):
    print(' ', end='')
print(mot, end='')
# print les espaces en droite
for i in range((long - len(mot)) // 2):
    print(' ')


print("SOL 2")
print(' ' * ((long - len(mot)) // 2), mot,
      ' ' * ((long - len(mot)) // 2), sep='')


print("SOL 3")
print(mot.center(long))
