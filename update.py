import sqlite3

conn = sqlite3.connect('test.db')
print("successfully connected")

conn.execute("UPDATE TEACHERS SET SALARY=56000.00 WHERE ID=4")
conn.commit()

data = conn.execute("SELECT * FROM TEACHERS")

for teacher in data:
    print("ID :", teacher[0])
    print("FIRSTNAME :", teacher[1])
    print("LASTNAME :", teacher[2])
    print("AGE :", teacher[3])
    print("SALARY :", teacher[4])

print("successfully updated a record")
conn.close()