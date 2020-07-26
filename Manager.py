import tkinter as tk
from tkinter import *
from tkinter import ttk
from DataBase import *
# from LoginPage import LOGIN
from MenuPOS import MenuPos
class ManagerPage(CashierDataBase,SalesDataBase):
    # obj1=CashierDataBase()
    # obj2=SalesDataBase()


    def __init__(self,root):
        self.root=root
        self.root.title("Admin Page")
        self.root.geometry("1000x800")
        self.CashierName=StringVar()
        self.CashierEmail=StringVar()
        self.CashierID=IntVar()
        self.Search=IntVar()
        self.obj1 = CashierDataBase()
        self.obj2 = SalesDataBase()
    def Form(self):
        self.leftbutton_frame=Frame(self.root,relief=RIDGE,bg="green").place(x=0,y=0,height=800,width=200)
        self.bottombutton_frame=Frame(self.root,relief=RIDGE,bg="orange").place(x=201,y=700,height=100,width=800)
        self.showdata_frame=Frame(self.root,relief=RIDGE,bg="grey").place(x=201,y=0,height=699,width=800)

        #******************buttons in LeftButton*****************************
        self.Label=Label(self.leftbutton_frame,text="Welcome",font=("times new roman", 14, 'italic'),relief=FLAT,bg="yellow",fg="black").place(x=0,y=10,width=200,height=30)
        self.Cashier_Button=Button(self.leftbutton_frame,text="manage Cashier",command=self.ShowCashier,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=10,y=50,height=40,width=150)
        self.Sales_Button = Button(self.leftbutton_frame, text="Sale Information",command=self.ShowSale,font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey").place(x=10,y=101,height=40,width=150)
        # self.Sales_Button = Button(self.leftbutton_frame, text="Sale Information",font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey")
        # self.Sales_Button.bind("Button-1",self.All_DataS)
        # self.Sales_Button.place(x=10, y=101,height=40,width=150)


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
        # self.cadd_button=Button(self.showdata_frame,command=self.add,text="ADD",font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=210,y=740,height=30,width=70)
        self.cadd_button = Button(self.showdata_frame, command=self.add, text="ADD",font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey")
        self.cadd_button.bind("Button-1",self.add)
        self.cadd_button.place(x=210, y=740,height=30,width=70)

        self.cupdate_button = Button(self.showdata_frame,command=self.update, text="UPDATE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=300, y=740, height=30, width=70)
        self.cDelete_button = Button(self.showdata_frame, command=self.delete,text="DELETE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=390, y=740, height=30, width=70)
        self.csearchEntry=Entry(self.showdata_frame,textvariable=self.Search,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=480,y=742,height=25,width=150)
        self.csearchbutton=Button(self.showdata_frame,text="SEARCH", font=("times new roman", 14, 'italic'),command=self.onlyone_Data,relief=FLAT, bg="grey").place(x=650, y=740, height=30, width=100)
        self.cShowbutton=Button(self.showdata_frame,text="Show", font=("times new roman", 10, 'italic bold'),relief=FLAT, bg="grey",command=self.All_DataC).place(x=800, y=730, height=60, width=100)
        self.CashierForm=ttk.Treeview(self.showdata_frame)
        self.CashierForm.place(x=201,y=0,height=699,width=800)
        self.CashierForm["columns"]=("one","two","three","four")

        self.CashierForm.column("#0",width=0,minwidth=0,stretch=tk.NO)
        self.CashierForm.column("one", width=200, minwidth=250, stretch=tk.NO)
        self.CashierForm.column("two", width=200, minwidth=250, stretch=tk.NO)
        self.CashierForm.column("three", width=200, minwidth=250, stretch=tk.NO)
        self.CashierForm.column("four", width=200, minwidth=250, stretch=tk.NO)

        # self.CashierForm.heading("#0",text="ID",anchor=tk.W)
        self.CashierForm.heading("one", text="ID", anchor=tk.W)
        self.CashierForm.heading("two", text="Name", anchor=tk.W)
        self.CashierForm.heading("three", text="Email", anchor=tk.W)
        self.CashierForm.heading("four", text="CashierID", anchor=tk.W)

    def ShowSale(self):
        self.sallbuttton = Button(self.showdata_frame, text="SaleInformation", font=("times new roman", 10, 'italic bold'),relief=FLAT, bg="grey",command=self.All_DataS).place(x=900, y=730, height=60, width=100)
        self.SaleForm=ttk.Treeview(self.showdata_frame)
        self.SaleForm.place(x=201, y=0, height=699, width=800)
        self.SaleForm["columns"]=("one","two","three","four")
        self.SaleForm.column("#0", width=0, minwidth=0, stretch=tk.NO)
        self.SaleForm.column("one", width=170, minwidth=170, stretch=tk.NO)
        self.SaleForm.column("two", width=170, minwidth=170, stretch=tk.NO)
        self.SaleForm.column("three", width=250, minwidth=170, stretch=tk.NO)
        self.SaleForm.column("four", width=250, minwidth=250, stretch=tk.NO)

        self.SaleForm.heading("one", text="ID", anchor=tk.W)
        self.SaleForm.heading("two", text="RecieptNo", anchor=tk.W)
        self.SaleForm.heading("three", text="Total", anchor=tk.W)
        self.SaleForm.heading("four", text="Date", anchor=tk.W)


#fetch all wala function tree.insert me call hoga
    def add(self):
        self.ShowCashier()
        self.obj1.Insert(self.CashierName.get(),self.CashierID.get(),self.CashierEmail.get())
    def delete(self):
        self.ShowCashier()
        self.obj1.Delete(self.CashierID.get())
    def update(self):
        self.ShowCashier()
        self.obj1.Update(self.CashierName.get(),self.CashierID.get())

    def All_DataS(self):
        self.ShowSale()
        result=self.obj2.FetchAll()
        for r in result:
            print(r)
            self.SaleForm.insert("", tk.END, values=r)
    def All_DataC(self):
        self.ShowCashier()
        a=self.obj1.FetchAll()
        for r in a:
            print(r)
            self.CashierForm.insert("", tk.END, values=r)

    def onlyone_Data(self):
        self.ShowCashier()
        a=self.obj1.FetchOne(self.Search.get())
        for r in a:
            print(r)
            self.CashierForm.insert("",tk.END,values=r)
    def logout(self):
        self.root.quit()
        # ob1=LOGIN()
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
# obj=Manager()