m = input("Enter the word: ")
l = int(input("Enter the width of the line: "))

## SOL 1

i = (l - len(m)) // 2
x = 0
while x < i:
    print('*', end='')
    x+= 1
print(m)

## SOL 2

i = (l - len(m)) // 2
print('*' * i, m, '*' * i, sep='')

## SOL 3

print(m.center(l, '*'))

## SOL 4

print(m.rjust(i + len(m)))
