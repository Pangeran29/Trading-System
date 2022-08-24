from database import *
from datetime import datetime

#super class
class Action:


    #init and input
    def __init__(self) -> None:
        stock = input('enter stock code : ')
        self.__stock = stock.upper()
        self.__lot = int(input(f'enter {self.__stock} quantity : '))
        self.__price = int(input(f'enter {self.__stock} price : '))
        self.__total = self.__lot*self.__price*100
        self.__date = datetime.today()
        pass

    """buy command """
    #input database 
    @property
    def save(self):
        #input into database
        mycursor.execute("INSERT INTO Stocks (codes, price, quantity, total) VALUES (%s,%s,%s,%s)",(self.__stock,self.__price ,self.__lot, self.__total))
        #save command
        db.commit()

    """sell command """
    #delete database
    @property
    def delete(self):
        x = "DELETE FROM Stocks WHERE codes = %s"
        mycursor.execute("SELECT codes FROM Stocks")
        for i in mycursor:
            if self.__stock in i:
                mycursor.execute(x,[self.__stock])
                db.commit()
                print("done")
                break
        else:
            print(f'{self.__stock}, is\'nt in portofolio')
    
    """status command """
    #status
    @property
    def status(self):
        print(f'You\'re gonna execute {self.__stock}\n\tPrice : {self.__price:,}\n\tquantity : {self.__lot}\n\tTotal : {self.__total:,}\n\tdate : {self.__date}')

    #confirmation buy
    @property
    def confirmation_buy(self):
        print(f'are you sure wanna execute {self.__stock}')
        #branching
        x = input("y/n ? ")
        if x =="y":
            print(f'OKEY :)')
            self.save
            devider()
            portofolio()
        elif x =="n":
            print('OKEY, bye-bye')
        else:
            print("wrong input")

    #confirmation sell
    @property
    def confirmation_sell(self):
        print(f'are you sure wanna execute {self.__stock}')
        #branching
        x = input("y/n ? ")
        if x =="y":
            print(f'OKEY :)')
            self.delete
            devider()
            portofolio()
        elif x =="n":
            print('OKEY, bye-bye')
        else:
            print("wrong input")

""" status """
#devider
def devider():
    print('='*50)

#check portofolio
def portofolio():
    mycursor.execute("SELECT * FROM Stocks")
    print("portofolio saat ini : ")
    for i in mycursor:
        print(f'{i}')


#class buy
class Buy(Action):

    def __init__(self) -> None:
        super().__init__()
        devider()
        self.status
        devider()
        self.confirmation_buy


#class sell
class Sell(Action):

    def __init__(self) -> None:
        portofolio()
        devider()
        super().__init__()
        devider()
        self.confirmation_sell