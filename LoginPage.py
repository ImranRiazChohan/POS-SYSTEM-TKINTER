import tkinter as tk
from tkinter import ttk
from DataBase import *
from MenuPOS import MenuPos,MenuFORM
from Manager import Manager
from DataBase import CashierDataBase,SalesDataBase
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
    def LoginFOrm(self):
        self.Login_frame=ttk.LabelFrame(self.root,relief=tk.GROOVE).pack()
        self.Login_Icon=ttk.Label(self.root,text="LOGIN PAGE").place(x=120,y=50)
        self.userName_label=ttk.Label(self.Login_frame,text="UserName: ").place(x=20,y=100)
        self.UserPass_label=ttk.Label(self.Login_frame,text="PassWord: ").place(x=20,y=150)
        self.UserName_Entry_v=tk.StringVar()
        self.UserName_Entry=ttk.Entry(self.Login_frame,textvariable=self.UserName_Entry_v).place(x=120,y=100)
        self.UserPass_Entry_v = tk.StringVar()
        self.UserPass_Entry = ttk.Entry(self.Login_frame,textvariable=self.UserPass_Entry_v).place(x=120,y=150)
        self.LoginButton=ttk.Button(self.Login_frame,text="Login",command=self.Clicked).place(x=60,y=200)
        self.CancelButton=ttk.Button(self.Login_frame,text="Cancle",command=self.Cancel).place(x=170,y=200)

    def Clicked(self):
        self.q=CashierDataBase()

        if self.UserName_Entry_v.get()=="admin" and self.UserPass_Entry_v.get()=="admin":
            self.root.destroy()
            obj1=Manager()

        elif self.q.curObj.execute("select *from CashierInfo Where CashierName=? and CashierId=?",(self.UserName_Entry_v.get(), self.UserPass_Entry_v.get()),):
            self.root.destroy()
            obj2=MenuPos()
            # self.CashierInfo(self.UserPass_Entry_v.get())

        elif self.UserPass_Entry_v.get()=="" and self.UserName_Entry_v.get()=="":
                messagebox.showinfo("Error","Please Enter a Correct Detail")


    def CashierInfo(self,ids):
        id = self.obj.casheirIDEntry_
        email =self.obj.casheirEmailEntry_
        name =self.obj.casheirNameEntry_

        result=self.q.curObj.execute("select *from CashierInfo where CashierID=? ", (ids,))
        self.cashierDetail=[]
        for r in result:
            # print("name:".format(r[2]))
            # print("Id:".format(r[1]))
            # print("Email".format(r[3]))
            self.cashierDetail.append(result[r])
        return self.cashierDetail



        self.q.curObj.commit()
    def Cancel(self):
        self.root.quit()
    # def CashierInfo(self):


class LOGIN(Login):
    def __init__(self):
        root = tk.Tk()
        root.geometry("300x300")
        root.title("LOGIN")
        obj = Login(root)
        obj.LoginFOrm()
        root.mainloop()
#
# if __name__=="__main__":
    #
    # root = tk.Tk()
    # root.geometry("300x300")
    # root.title("LOGIN")
    # obj = Login(root)
    # obj.LoginFOrm()
    # root.mainloop()
# l1=LOGIN()