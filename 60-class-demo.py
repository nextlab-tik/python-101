# Class
class Person:

    # constructor
    def __init__(self, nom, prenom):
        # self is `this` alternative on python
        self.nom = nom
        self.prenom = prenom
        self.name = nom + " " + prenom

    def hi(self):
        print("hi", self.name)

    def whoami(self):
        print("I'm", self.nom, self.prenom)

    # replace toString() on Java
    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)


firas = Person("Firas", "Chaaben")

firas.hi()
firas.whoami()
Person.whoami(firas)
print(firas)


class Personne:
    nom = "moez"
    prenom = "bouhlel"


p2 = Personne()
Person.whoami(p2)


# Subclass
class Employee(Person):

    def __init__(self, nom, prenom, job):
        # super().__init__(nom, prenom) # super() on python (call parent constructor)
        Person.__init__(self, nom, prenom)
        self.job = job

    def hi(self):
        super().hi()
        print("job:", self.job)

    def __str__(self):
        return "{} - {}".format(Person.__str__(self), self.job)


e = Employee("Firas", "Chaaben", "Etudiant")

print("Created employee:", e)
e.whoami()
print(e.job)


class Demo:
    for i in range(10):
        print(i)

    counter = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value
        Demo.counter += 1

    def __lt__(self, obj2):
        return self.value < obj2.value


d1 = Demo("demo1", 5)
d2 = Demo("demo2", 3)

print(d1 < d2)


# Identity theft


class JSON(int):
    from json import dumps


json = JSON(5)
print("DUMPS:", json.dumps())
