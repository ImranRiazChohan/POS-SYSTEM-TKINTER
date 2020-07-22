import tkinter as tk
from tkinter import *
from tkinter import ttk

class ManagerPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Page")
        self.root.geometry("1000x800")
    def Form(self):
        self.leftbutton_frame=Frame(self.root,relief=RIDGE,bg="green").place(x=0,y=0,height=800,width=200)
        self.bottombutton_frame=Frame(self.root,relief=RIDGE,bg="orange").place(x=201,y=700,height=100,width=800)
        self.showdata_frame=Frame(self.root,relief=RIDGE,bg="grey").place(x=201,y=0,height=699,width=800)

        #******************buttons in LeftButton*****************************
        self.Cashier_Button=Button(self.leftbutton_frame,text="manage Cashier",command=self.ShowCashier,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=10,y=50,height=40,width=150)
        self.Sales_Button = Button(self.leftbutton_frame, text="Sale Information",command=self.ShowSale,font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey").place(x=10,y=101,height=40,width=150)
        self.Logout_Button=Button(self.leftbutton_frame, text="Logout ",font=("times new roman", 14, 'italic'), relief=FLAT, bg="grey").place(x=10,y=151,height=40,width=150)

        #****************buttons in BottomButton*****************************
        self.nameLabel=Label(self.bottombutton_frame,text="Name",font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=210,y=710,height=20,width=50)
        self.NameEntry=Entry(self.bottombutton_frame,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=270,y=710,height=20,width=100)
        self.EmailLabel = Label(self.bottombutton_frame, text="Email", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=390, y=710, height=20, width=50)
        self.EmailEntry = Entry(self.bottombutton_frame, font=("times new roman", 14, 'italic'), relief=FLAT,bg="grey").place(x=450, y=710, height=20, width=100)
        self.IdLabel = Label(self.bottombutton_frame, text="CashierID", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=570, y=710, height=20, width=100)
        self.IdEntry=Entry(self.bottombutton_frame,font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=680, y=710, height=20, width=100)

        self.add_button=Button(self.bottombutton_frame,text="ADD",font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=210,y=740,height=30,width=70)
        self.add_button = Button(self.bottombutton_frame, text="UPDATE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=300, y=740, height=30, width=70)
        self.add_button = Button(self.bottombutton_frame, text="DELETE", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=390, y=740, height=30, width=70)
        self.searchEntry=Entry(self.bottombutton_frame,font=("times new roman", 14, 'italic'),relief=FLAT,bg="grey").place(x=480,y=742,height=25,width=150)
        self.searchbutton=Button(self.bottombutton_frame,text="SEARCH", font=("times new roman", 14, 'italic'),relief=FLAT, bg="grey").place(x=650, y=740, height=30, width=100)

    def ShowCashier(self):
        # self.CashierListBox=Listbox(self.showdata_frame).place(x=201,y=0,height=699,width=800)
        CashierForm=ttk.Treeview(self.showdata_frame)
        CashierForm.place(x=201,y=0,height=699,width=800)
        CashierForm["columns"]=("one","two","three")

        CashierForm.column("#0",width=200,minwidth=250,stretch=tk.NO)
        CashierForm.column("one", width=200, minwidth=250, stretch=tk.NO)
        CashierForm.column("two", width=200, minwidth=250, stretch=tk.NO)
        CashierForm.column("three", width=300, minwidth=250, stretch=tk.NO)

        CashierForm.heading("#0",text="ID",anchor=tk.W)
        CashierForm.heading("one", text="CashierID", anchor=tk.W)
        CashierForm.heading("two", text="Name", anchor=tk.W)
        CashierForm.heading("three", text="Email", anchor=tk.W)
    def ShowSale(self):
        SaleForm=ttk.Treeview(self.showdata_frame)
        SaleForm.place(x=201, y=0, height=699, width=800)
        SaleForm["columns"]=("one","two","three","four")

        SaleForm.column("#0",width=170,minwidth=250,stretch=tk.NO)
        SaleForm.column("one", width=170, minwidth=250, stretch=tk.NO)
        SaleForm.column("two", width=170, minwidth=250, stretch=tk.NO)
        SaleForm.column("three", width=170, minwidth=250, stretch=tk.NO)
        SaleForm.column("four", width=170, minwidth=250, stretch=tk.NO)

        SaleForm.heading("#0",text="Reciept No",anchor=tk.W)
        SaleForm.heading("one", text="Total", anchor=tk.W)
        SaleForm.heading("two", text="Date/Time", anchor=tk.W)
        SaleForm.heading("three", text="ID", anchor=tk.W)
        SaleForm.heading("four", text="CashierName", anchor=tk.W)

if __name__=="__main__":
    root=tk.Tk()
    obj=ManagerPage(root)
    obj.Form()
    root.mainloop()