""" untuk database yang perlu ditambahi adalah sistem update data 
    yang nanti nya berguna dalam avg down ataupun up """

import mysql.connector
from datetime import datetime

#database
db = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="prince29",
    database="action"
)

#cursor
mycursor = db.cursor()

#query command
C1 = "SHOW DATABASES"
C2 = "SHOW TABLES"
C3 = "SELECT * FROM Stocks"
C32 = "SELECT quantity FROM Stocks WHERE codes = 'emtk'"
C4 = "DELETE FROM Stocks WHERE codes = 'wskt'"

#mycursor.execute("CREATE TABLE Stocks (codes VARCHAR(50), price INT, quantity INT, total INT, created datetime)")

#mycursor.execute("INSERT INTO Stocks (codes, price, quantity, total) VALUES (%s,%s,%s,%s)",(self.__stock,self.__price ,self.__lot, self.__total))


# y = int(input("berapa lot? "))
# x= "UPDATE Stocks SET quantity = %s WHERE quantity = %s"
# value = (y, 11)

# try:
#     mycursor.execute(x,value)
#     db.commit()
#     print("success to upload data")
# except:
#     print("failed to upload data")


""" fixing ghost sell bug, use this codes """
# mycursor.execute("SELECT codes FROM Stocks")
# for i in mycursor:
#     if 'ASSA' in i:
#         print("halo")

# mycursor.execute(C3)
# for i in mycursor:
#     print(i)
# print('='*20)
# y = input("masukan kode saham ; ")
# x = "DELETE FROM Stocks WHERE codes = %s"
# mycursor.execute(x, [y])
# db.commit()
# mycursor.execute(C3)
# for i in mycursor:
#     print(i)
# print('='*20)