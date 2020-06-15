import sqlite3

conn = sqlite3.connect("studetails.db")

conn.execute('''CREATE TABLE STUDENT
              (ID INT PRIMARY KEY NOT NULL,
              FIRSTNAME TEXT NOT NULL,
              LASTNAME TEXT NOT NULL);''')

conn.close();
