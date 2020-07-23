import tkinter as tk
from tkinter import *
from tkinter import ttk
from DataBase import *
from MenuPOS import MenuPos
class ManagerPage(CashierDataBase,SalesDataBase):
    obj1=CashierDataBase()
    obj2=SalesDataBase()


    def __init__(self,root):
        self.root=root
        self.root.title("Admin Page")
        self.root.geometry("1000x800")
        self.CashierName=StringVar()
        self.CashierEmail=StringVar()
        self.CashierID=IntVar()

    def Form(self):
        self.leftbutton_frame=Frame(self.root,relief=RIDGE,bg="green").place(x=0,y=0,height=800,width=200)
        self.bottombutton_frame=Frame(self.root,relief=RIDGE,bg="orange").place(x=201,y=700,height=100,width=800)
        self.showdata_frame=Frame(self.root,relief=RIDGE,bg="grey").place(x=201,y=0,height=699,width=800)

        #******************buttons in LeftButton*****************************
        self.Cashier_Button=Button(self.leftbutton_frame,text="manage Cashier",command=self.ShowCashier,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=10,y=50,height=40,width=150)
        self.Sales_Button = Button(self.leftbutton_frame, text="Sale Information",command=self.ShowSale,font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey").place(x=10,y=101,height=40,width=150)
        self.Logout_Button=Button(self.leftbutton_frame, command=self.logout,text="Logout ",font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey").place(x=10,y=151,height=40,width=150)

    def ShowCashier(self):
        # self.CashierListBox=Listbox(self.showdata_frame).place(x=201,y=0,height=699,width=800)
        self.cnameLabel = Label(self.showdata_frame, text="Name", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=210, y=710, height=20, width=50)
        self.cNameEntry=Entry(self.showdata_frame,textvariabl=self.CashierName,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=270,y=710,height=20,width=100)
        self.cEmailLabel = Label(self.showdata_frame, text="Email", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=390, y=710, height=20, width=50)
        self.cEmailEntry = Entry(self.showdata_frame, textvariable=self.CashierEmail,font=("times new roman", 14, 'italic'), relief=FLAT,bg="grey").place(x=450, y=710, height=20, width=100)
        self.cIdLabel = Label(self.showdata_frame, text="CashierID", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=570, y=710, height=20, width=100)
        self.cIdEntry=Entry(self.showdata_frame,textvariable=self.CashierID,font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=680, y=710, height=20, width=100)
        #
        self.cadd_button=Button(self.showdata_frame,command=self.add,text="ADD",font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=210,y=740,height=30,width=70)
        self.cupdate_button = Button(self.showdata_frame,command=self.update, text="UPDATE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=300, y=740, height=30, width=70)
        self.cDelete_button = Button(self.showdata_frame, command=self.delete,text="DELETE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=390, y=740, height=30, width=70)
        self.csearchEntry=Entry(self.showdata_frame,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=480,y=742,height=25,width=150)
        self.csearchbutton=Button(self.showdata_frame,text="SEARCH", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=650, y=740, height=30, width=100)

        self.CashierForm=ttk.Treeview(self.showdata_frame)
        self.CashierForm.place(x=201,y=0,height=699,width=800)
        self.CashierForm["columns"]=("one","two","three")

        self.CashierForm.column("#0",width=200,minwidth=250,stretch=tk.NO)
        self.CashierForm.column("one", width=200, minwidth=250, stretch=tk.NO)
        self.CashierForm.column("two", width=200, minwidth=250, stretch=tk.NO)
        self.CashierForm.column("three", width=300, minwidth=250, stretch=tk.NO)

        self.CashierForm.heading("#0",text="ID",anchor=tk.W)
        self.CashierForm.heading("one", text="CashierID", anchor=tk.W)
        self.CashierForm.heading("two", text="Name", anchor=tk.W)
        self.CashierForm.heading("three", text="Email", anchor=tk.W)
    def ShowSale(self):
        self.sallbuttton = Button(self.showdata_frame, text="SaleInformation", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=790, y=730, height=60, width=160)

        self.SaleForm=ttk.Treeview(self.showdata_frame)
        self.SaleForm.place(x=201, y=0, height=699, width=800)
        self.SaleForm["columns"]=("one","two","three","four")

        self.SaleForm.column("#0",width=170,minwidth=250,stretch=tk.NO)
        self.SaleForm.column("one", width=170, minwidth=250, stretch=tk.NO)
        self.SaleForm.column("two", width=170, minwidth=250, stretch=tk.NO)
        self.SaleForm.column("three", width=170, minwidth=250, stretch=tk.NO)
        self.SaleForm.column("four", width=170, minwidth=250, stretch=tk.NO)

        self.SaleForm.heading("#0",text="Reciept No",anchor=tk.W)
        self.SaleForm.heading("one", text="Total", anchor=tk.W)
        self.SaleForm.heading("two", text="Date/Time", anchor=tk.W)
        self.SaleForm.heading("three", text="ID", anchor=tk.W)
        self.SaleForm.heading("four", text="CashierName", anchor=tk.W)



#fetch all wala function tree.insert me call hoga
    def add(self):
        self.ShowCashier
        self.obj1.Insert(self.CashierName.get(),self.CashierID.get(),self.CashierEmail.get())
    def delete(self):
        self.ShowCashier()
        self.obj1.Delete(self.CashierID.get())
    def update(self):
        self.ShowCashier()
        self.obj1.Update(self.CashierName.get(),self.CashierID.get())

    def All_Data(self):
        pass
    def onlyone_Data(self):
        pass
    def logout(self):
        self.root.quit()
class Manager:
    def __init__(self):
        root=tk.Tk()
        obj1=ManagerPage(root)
        obj1.Form()
        root.mainloop()
#
# if __name__=="__main__":
#     # root=tk.Tk()
#     # obj=ManagerPage(root)
#     # obj.Form()
#     # root.mainloop()