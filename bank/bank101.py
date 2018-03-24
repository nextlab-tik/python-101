# github.com/tiktn/python-101
# github.com/tiktn/webapp-101
from account import Account, BalanceException
import sys

accounts = {
    "home": Account("home"),
    "work": Account("work"),
}
"""
ac.deposit(50) # Account.deposit(ac, 50)
try:
    ac.withdraw(10)
    print("p1")
    ac.withdraw(500)
    print("p2")
except BalanceException as e:
    print("Erreur de blance")
print(ac)
"""
while True:
    a = input("Select Account (work/home): ")
    ac = accounts.get(a, accounts["home"])
    print(ac)
    t = input("Transaction Type or statics or quit (D/w/s/q): ")
    try:
        if t.lower() == "d":
            am = int(input("Amount: "))
            # ac.deposit(am)
            ac += am
        elif t.lower() == "w":
            am = int(input("Amount: "))
            # ac.withdraw(am)
            ac -= am
        elif t.lower() == "s":
            ac.statics()
        else:
            sys.exit()

    except BalanceException as e:
        print("Erreur!", e)
    print(ac)
