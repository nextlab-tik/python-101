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
print(firas)


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
