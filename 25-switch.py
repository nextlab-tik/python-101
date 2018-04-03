i = int(input())

if i == 5 or i == 8:
    print("hi")
elif i in [1, 4]:
    print("bye")
elif i == 9:
    print("salut")
elif 10 <= i <= 16 or i == 18:
    print("ciao")
elif i in range(20, 101, 2):
    print("a revoir")
else:
    print("hello")
