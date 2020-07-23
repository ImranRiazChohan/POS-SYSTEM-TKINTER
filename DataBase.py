import sqlite3
from sqlite3 import  Error
from abc import ABC,abstractmethod

class DataBase(ABC):
    def __init__(self):
        self.db_name="POS DataBase.db"
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
        try:
            self.curObj.execute("CREATE TABLE cashierInfo(CashierName text, CashierEMail text ,CashierID integer PRIMARY KEY)")
            self.con.commit()
        except Error:
            print(Error)
        finally:
            print("Tabel is already Created")
    def CreateTableSale(self):
        try:
            self.curObj = self.con.cursor()
            self.curObj.execute("CREATE TABLE SaleInfo(RecieptNo integer PRIMARY KEY, TotalAmount double,Date datetime)")
            self.con.commit()
        except Error:
            print(Error)
        finally:
            print("Table is AlreadY Created")
    @abstractmethod
    def Insert(self):
        pass
    @abstractmethod
    def Delete(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def FetchAll(self):
        pass


class CashierDataBase(DataBase):
    def __init__(self):
        super().__init__()
        c = self.CreateDataBAse()
        a=self.CreateTableCasier()
        b=self.CreateTableSale()
        print(self.db_name)
    def Update(self,Cashier_Name,Cashier_ID):
        try:
            self.curObj.execute("Update cashierInfo set CashierName=? where CashierID=?" ,(Cashier_Name,Cashier_ID))
            self.con.commit()
            self.curObj.close()
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("The Value is UpDate it")
    def Delete(self,Cashier_ID):
        try:
            self.con.execute("DELETE from cashierInfo where CashierID=?",(Cashier_ID,))
            self.con.commit()
            self.curObj.close()
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("The Entity is Deleted")
    def Insert(self,CashirName,Cashier_ID,Cashier_Email):
        try:
            self.curObj.execute("INSERT INTO cashierInfo (CashierName,CashierEmail,CashierID) VALUES (?,?,?)",(CashirName,Cashier_Email,Cashier_ID))
            self.con.commit()
            self.curObj.close()
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("Connection is closed")

    def FetchAll(self):
        try:
            self.curObj.execute("select * from CashierInfo")
            self.result=self.curObj.fetchall()
            for row in self.result:
                pass
            return self.result
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("All Connection is Closed")
    def FetchOne(self,CashierID):
        try:
            self.curObj.execute("select *"+" from CashierInfo where CashierID=? ",(CashierID))
            self.result=self.curObj.fetchone()
            return self.result
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("All Connection is Closed")
    # def auth(self,uname,upass):
    #     try:
    #         self.curObj.execute("select *from CashierInfo Where CashierName=? and CashierId=?",(uname,upass))
    #         self.con.commit()
    #         self.curObj.close()
    #     except Error:
    #         print(Error)
    #     finally:
    #         if self.con:
    #             self.con.close()
    #             print("Connection is closed")

class SalesDataBase(DataBase):
    def __init__(self):
        super().__init__()
        c = self.CreateDataBAse()
        a=self.CreateTableCasier()
        b=self.CreateTableSale()
        print(self.db_name)
    def Update(self):
        pass
    def Delete(self):
        pass
    def Insert(self,Reciept_No,Total_amount,Date):
        try:
            self.curObj.execute("INSERT INTO saleInfo (RecieptNo,TotalAmount,Date) VALUES (?,?,?)",(Reciept_No,Total_amount,Date))
            self.con.commit()
            self.curObj.close()

        except Error:
            print(Error)

        finally:
            if self.con:
                self.con.close()
            print("Connection is closed")
    def FetchAll(self):
        try:
            self.curObj.execute("select * from SaleInfo")
            self.result=self.curObj.fetchall()

            for row in self.result:
                print("RecieptNo:",row[0])
                print("TotalAmount:",row[1])
                print("Date:",row[2])
                print("\n")
        except Error:
            print(Error)
        finally:
            if self.con:
                self.con.close()
                print("All Connection is Closed")
        return self.result



