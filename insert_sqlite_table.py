import sqlite3

conn = sqlite3.connect("studetails.db")

conn.execute('''INSERT INTO STUDENT
              (ID, FIRSTNAME, LASTNAME) VALUES (1, "Omkar", "Pakki");
            ''')

conn.commit()
conn.close()
