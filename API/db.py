import sqlite3

con = sqlite3.connect('data.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR2(2000) NOT NULL,
            age VARCHAR2(10) NOT NULL,
            image VARCHAR2(1000) NOT NULL
        )
    """)

def enterData(name, age, image):
    db.execute("INSERT INTO user VALUES(NULL,?,?,?)",(name, age, image))
    con.commit()
    return True

def getData():
    db.execute("SELECT * FROM user")
    users = db.fetchall()
    return users

def getOneData(id):
    db.execute("SELECT * FROM user WHERE id=(?)",(id,))
    user = db.fetchall()
    return user

def deleteData(id):
    db.execute("SELECT * FROM user WHERE id=(?)",(id,))
    user = db.fetchall()
    db.execute("DELETE FROM user WHERE id=(?)",(id,))
    con.commit()
    return user



# createTable()
