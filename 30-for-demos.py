"""
For use cases
"""

print("For 1:")
for i in range(2, 5, 2):
    print(i)

print("For 2:")
for i in range(5, 2, -1):
    print(i)

lst = [1, 5, 9]

print("For 3:")
for i in lst:
    print(i)

print("For 4:")
s = "hello"
for i in s:
    print(i, end='')


x = [5, 4, 1, 9, 2, 5, 0, -1]

print("Elements in pair positions")
for var in x[::2]:
    print(var)

print("Elements sorted")
for var in sorted(x):
    print(var)

print("Elements sorted in pair positions")
for var in sorted(x)[::2]:
    print(var)

print("X in reverse")
for var in x[::-1]:
    print(var)


s = "azerty"

print("Elements and their index")
for i, c in enumerate(s):
    print(i, c)


l1 = [5, 2, 3, -1]
l2 = ['a', 'b', 'c']

print("Elements from 2 or more lists and their index")
for i, (x1, x2) in enumerate(zip(l1, l2)):
    print(i, x1, x2)
