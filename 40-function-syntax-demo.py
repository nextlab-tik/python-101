"""
Function
"""


# Empty function
def fn_vide():
    pass


fn_vide()


# Void function
def hi():
    print('hi')


hi()


# Function arguments
def salut(nom):
    print("hi", nom)


salut("firas")


# Default values, positional arguments vs. keyword arguments
def hello(name, family_name="chaaben", suffix="Mr."):
    print("hello", suffix, name, family_name)


hello("ali", 10)
hello("ali", "bouhlel")
hello("ali", family_name="bouhlel", suffix="5")
hello(suffix="bohlel", family_name="Mr.", name="ali")

hello("salma", "M.")
hello("salma", suffix="M.")


# Return
def pow2(x=2):
    return x ** 2


print(pow2())
print(pow2(5))


# Return multiple values
def multi_return():
    return 1, 2, 3


x, y, z = multi_return()
print(x, y, z)

# Alias
print2 = print
print2("Hello", "World", sep="-")


# Var arguments
def rec_sum(*a, **k):
    if not a:
        return 0
    elif len(a) == 1:
        return a[0]
    elif len(a) == 2:
        return a[0] + a[1]
    else:
        return rec_sum(a[0] + a[1], *a[2:])


print(rec_sum())
print(rec_sum(1))
print(rec_sum(1, 2))
print(rec_sum(1, 2, 3, 4, 5))


# recursive functions
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# passing function as argument
def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def op(operation, a, b):
    return operation(a, b)


print(op(add, 1, 2))
print(op(mul, 3, 2))


# Conditional function generation
def fn1(x):
    if x:
        def fn2():
            print("hi")
    else:
        def fn2():
            print("hello")
    return fn2


fn = fn1(True)
fn()
fn = fn1(False)
fn()

