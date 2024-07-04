import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid  INTEGER PRIMARY KEY,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(sup_id INTEGER PRIMARY KEY,invoice  INTEGER,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cat_ID INTEGER PRIMARY KEY,name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS Product(pId  INTEGER PRIMARY KEY ,Category text,Supplier text,name text,price text,quantity text,status text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL,email TEXT NOT NULL)")
    con.commit()


create_db()