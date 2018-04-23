class Person:
    nationalite = "Tunisia"

    def __init__(self):
        self.nationalite = "Maroc"

    @staticmethod
    def printN():
        print(Person.nationalite)


p = Person()

p.printN()
Person.printN()

p2 = Person()
print(p.nationalite)
print(p2.nationalite)


p.nationalite = "French"

print(p.nationalite)
print(p2.nationalite)

p3 = Person()
print(p3.nationalite)
print(Person.nationalite)
Person.nationalite = "USA"
print(Person.nationalite)
print(p.nationalite)
p4 = Person()
print(p4.nationalite)
print(p2.nationalite)
