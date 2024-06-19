
import sqlite3

conn = sqlite3.connect('test.db')
print("success")

conn.execute("INSERT INTO TEACHERS VALUES (1,'JULIAN','NWOYE',46,90330.00)")
conn.execute("INSERT INTO TEACHERS VALUES (2,'JAMES','NAOMI',23,90000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (3,'JANE','GWANDA',18,30330.00)")
conn.execute("INSERT INTO TEACHERS VALUES (4,'VIVIAN','NJERI',24,60330.00)")
conn.execute("INSERT INTO TEACHERS VALUES (5,'VALARY','MALOBA',35,23330.00)")
conn.execute("INSERT INTO TEACHERS VALUES (6,'VINCENT','KAMAU',27,35330.00)")

conn.commit()
print("successfully inserted records")

conn.close()