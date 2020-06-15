import sqlite3

conn = sqlite3.connect("studetails.db")

cursor = conn.execute("select * from STUDENT")

print("Cursor Here::", cursor)
for col in cursor:
    print("Data::", col)

conn.close();
