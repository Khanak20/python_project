import sqlite3
def connection():
    a=sqlite3.connect('mydata.db')
    return a

def create_table(a):
    a.execute('''CREATE TABLE IF NOT EXISTS STUDENT1(NAME TEXT)''')
    print("table")

def insert(a):
    c = input("Enter name : ")
    a.execute('''INSERT INTO STUDENT1(NAME) VALUES('?')''',(c))
    print("inserted")

x=connection()
create_table(x)
insert(x)
x.commit()
x.close()