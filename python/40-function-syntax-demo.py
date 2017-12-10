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
