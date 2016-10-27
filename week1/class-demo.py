class Person:

    # constructor
    def __init__(self, nom, prenom):
        # self is `this` equvalent on python
        self.nom = nom
        self.prenom = prenom

    def whoami(self):
        print("I'm", self.nom, self.prenom)

    # toString() on python
    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

p = Person("Firas", "Chaaben")

print("Created person:", p)
p.whoami()


class Employee(Person):

    def __init__(self, nom, prenom, job):
        # super() on python (call parent constructor)
        Person.__init__(self, nom, prenom)
        self.job = job

    def __str__(self):
        return "{} - {}".format(Person.__str__(self), self.job)

e = Employee("Firas", "Chaaben", "Etudiant")

print("Created employee:", e)
e.whoami()
print(e.job)
