import os
import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

class BalanceException(Exception):
    pass

class Account:
    journal_file = "journal.csv"

    def __init__(self, name):
        self.name = name
        self.balance = 0
        # SOL 1
        try:
            f = open(self.journal_file)
            r = csv.reader(f)
            for line in r:
                if line[0] == self.name:
                    self.balance += int(line[1])
            f.close()
        except FileNotFoundError:
            pass
        """
        # SOL 2
        if os.path.isfile("bank.txt"):
            f = open("bank.txt")
            for line in f:
                self.balance += int(line)
            f.close()
        """

    def deposit(self, amount):
        self.balance += amount
        f = open(self.journal_file, "a")
        # f.write("+%s\n" % amount)
        w = csv.writer(f)
        w.writerow([self.name, "+%s" % amount, datetime.now()])
        f.close()

    def withdraw(self, amount):
        if amount > self.balance:
            raise BalanceException("Not Enough Balance")
        self.balance -= amount
        f = open(self.journal_file, "a")
        # f.write("-%s\n" % amount)
        w = csv.writer(f)
        w.writerow([self.name, "-%s" % amount, datetime.now()])
        f.close()

    def statics(self):
        f = open(self.journal_file)
        r = csv.reader(f)
        #trs = []
        #for row in r:
        #    if row[0] == self.name:
        #        trs.append([row[1], row[2]])
        trs = [
            [row[1], row[2]]
            for row in r
            if row[0] == self.name
        ]
        #X = []
        #for tr in trs:
        #   X.append(int(tr[0]))
        X = [
            datetime.strptime(
                tr[1],
                '%Y-%m-%d %H:%M:%S.%f'
            )
            for tr in trs
        ]
        #Y = [int(tr[0]) for tr in trs]
        Y = []
        bal = 0
        for tr in trs:
            bal += int(tr[0])
            Y.append(bal)
        print(list(X))
        print(list(Y))
        plt.plot(X, Y)
        plt.show()
        f.close()

    def __str__(self):
        return "Account: %s" % self.balance

    def __add__(self, n):
        self.deposit(n)
        return self

    def __sub__(self, n):
        self.withdraw(n)
        return self
