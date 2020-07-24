import tkinter as tk
from tkinter import ttk
from DataBase import *
from MenuPOS import MenuPos
from Manager import Manager
from DataBase import CashierDataBase,SalesDataBase
from  tkinter import  messagebox
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

        elif self.q.curObj.execute("select *from CashierInfo Where CashierName=? and CashierId=?",(self.UserName_Entry_v.get(), self.UserPass_Entry_v.get()))==1:
            self.root.destroy()
            obj2=MenuPos()

        elif self.UserPass_Entry_v.get()=="" or self.UserName_Entry_v.get():
                tk.messagebox.showinfo("Error","Please Enter a Correct Detail")



    def Cancel(self):
        self.root.quit()
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