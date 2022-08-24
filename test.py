from database import *

mycursor.execute("SELECT * FROM Stocks")
for i in mycursor:
    print(i)

x = input("masukan kode saham:",)
mycursor.execute("DELETE FROM Stocks WHERE codes = %s", [x])
db.commit()