import sqlite3
import os


if not os.path.isfile("db.sqlite3"):
    db = sqlite3.connect("db.sqlite3")
    db.execute("""
CREATE TABLE transactions (
    client TEXT,
    account TEXT,
    amount REAL,
    time TEXT
)""")
    db.execute("INSERT INTO transactions VALUES(?, ?, ?, ?)", ("moez", "work", 500, "2012-10-01"))
    db.commit()
    db.close()
db = sqlite3.connect("db.sqlite3")
c = db.cursor()
c.execute("SELECT * FROM transactions")
for row in c:
    print(row)
db.close()
