import sqlite3
from sqlite3 import  Error
class DataBase:
    def __init__(self):
        self.db_name="POS DataBase"
    def CreateDataBAse(self):
        try:
            self.con=sqlite3.connect(self.db_name)
            print("Successfully Created!")
            return self.con
        except Error:
            print(Error)
        finally:
            print("not created")
    def CreateTableCasier(self):
        self.curObj=self.con.cursor()
        self.curObj.execute("CREATE TABLE cashierInfo(id integer PRIMARY KEY,CashierName text, CashierEMail text ,CashierID integer)")
        self.con.commit()
    def CreateTableSale(self):
        self.curObj = self.con.cursor()
        self.curObj.execute("CREATE TABLE SaleInfo(id integer PRIMARY KEY,RecieptNo integer, TotalAmount double,Date datetime)")
        self.con.commit()
    def Insert(self):
        pass
    def Delete(self):
        pass
    def Update(self):
        pass