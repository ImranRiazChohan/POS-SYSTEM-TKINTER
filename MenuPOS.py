import tkinter as tk
from tkinter import *
from tkinter import  ttk
import random
from datetime import datetime
from DataBase import  SalesDataBase
class MenuFORM:
    global pizzalist
    def __init__(self,root):
        self.root=root
        self.root.title("POS SYSTEM")
        self.root.geometry("1450x800")
        self.deal1 = IntVar()
        self.deal1 = IntVar()
        self.deal2 = IntVar()
        self.deal3 = IntVar()
        self.deal4 = IntVar()
        self.deal5 = IntVar()
        self.deal6 = IntVar()
        # ****************************
        self.Drink1 = IntVar()
        self.Drink2 = IntVar()
        self.Drink3 = IntVar()
        self.Drink4 = IntVar()
        self.Drink5 = IntVar()
        self.Drink6 = IntVar()
        # ****************************
        self.Pizza1 = IntVar()
        self.Pizza2 = IntVar()
        self.Pizza3 = IntVar()
        self.Pizza4 = IntVar()
        self.Pizza5 = IntVar()
        self.Pizza6 = IntVar()
        self.Pizza7 = IntVar()
        self.Pizza8 = IntVar()
        self.Pizza9 = IntVar()
        self.Pizza10 = IntVar()
        # ***************************
        self.Other1 = IntVar()
        self.Other2 = IntVar()
        self.Other3 = IntVar()
        self.s1 = SalesDataBase()

        self.casheirIDEntry_=IntVar()
        self.casheirNameEntry_=IntVar()
        self.casheirEmailEntry_=IntVar()

    def Menu(self):
        self.title_label=Label(self.root,text="CALIFORNIA POS SYSTEM",bg="red",relief=GROOVE,fg="white",font=("times new roman",30,'bold'),pady=20).pack(fill=X)
        #********************PIZZA DETAIL****************************)
        self.Pizza_Frame=LabelFrame(self.root,text="Pizza",bg="yellow",relief=GROOVE,font=("times new roman",20,'bold'))
        self.Pizza_Frame.place(x=0,y=100,height=550,width=398)
        self.pizza1_label=Label(self.Pizza_Frame,text="chickenFajita",font=("times new roman",13,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.pizza1_entry=Entry(self.Pizza_Frame,font=("times new roman",14,'bold'),textvariable=self.Pizza1,width=11,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        self.pizza1_combox=ttk.Combobox(self.Pizza_Frame,width=9,values=["large","jumbo","regular","345 ml","2.15 ml","1.5 ml"])
        self.pizza1_combox.grid(row=0,column=2)
        self.pizza2_label = Label(self.Pizza_Frame, text="ChickenTikka", font=("times new roman", 13, 'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        self.pizza2_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN,textvariable=self.Pizza2).grid(row=1,column=1,padx=10,pady=10)
        self.pizza2_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza2_combox.grid(row=1, column=2)
        self.pizza3_label=Label(self.Pizza_Frame,text="SuperSupreame",font=("times new roman",13,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        self.pizza3_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'),textvariable=self.Pizza3, width=11, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        self.pizza3_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza3_combox.grid(row=2, column=2)
        self.pizza4_label = Label(self.Pizza_Frame, text="ChickenSupreame", font=("times new roman", 13, 'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        self.pizza4_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), textvariable=self.Pizza4,width=11, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        self.pizza4_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza4_combox.grid(row=3, column=2)
        self.pizza5_label = Label(self.Pizza_Frame, text="Veggie Lover", font=("times new roman", 13, 'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        self.pizza5_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Pizza5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        self.pizza5_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza5_combox.grid(row=4, column=2)
        self.pizza6_label = Label(self.Pizza_Frame, text="BeefSupreame", font=("times new roman", 13, 'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        self.pizza6_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Pizza6, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        self.pizza6_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza6_combox.grid(row=5, column=2)
        self.pizza7_label = Label(self.Pizza_Frame, text="Cheese and Peproni", font=("times new roman", 13, 'bold')).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        self.pizza7_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11, textvariable=self.Pizza7,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        self.pizza7_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza7_combox.grid(row=6, column=2)
        self.pizza8_label = Label(self.Pizza_Frame, text="Cheese Lover", font=("times new roman", 13, 'bold')).grid(row=7,column=0,padx=10,pady=10,sticky="w")
        self.pizza8_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Pizza8, relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
        self.pizza8_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza8_combox.grid(row=7, column=2)
        self.pizza9_label = Label(self.Pizza_Frame, text="CreamyTikka", font=("times new roman", 13, 'bold')).grid(row=8,column=0,padx=10,pady=10,sticky="w")
        self.pizza9_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Pizza9, relief=SUNKEN).grid(row=8,column=1,padx=10,pady=10)
        self.pizza9_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza9_combox.grid(row=8, column=2)
        self.pizza10_label = Label(self.Pizza_Frame, text="fajitaScilian", font=("times new roman", 13, 'bold')).grid(row=9,column=0,padx=10,pady=10,sticky="w")
        self.pizza10_entry = Entry(self.Pizza_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Pizza10, relief=SUNKEN).grid(row=9,column=1,padx=10,pady=10)
        self.pizza10_combox = ttk.Combobox(self.Pizza_Frame, width=9,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.pizza10_combox.grid(row=9, column=2)
    #*******************************Deal Detail*************************
        self.Deal_Frame = LabelFrame(self.root, text="Deal", bg="ORANGE", relief=GROOVE,font=("times new roman", 20, 'bold'))
        self.Deal_Frame.place(x=399, y=100, height=550, width=200)
        self.Deal1_label = Label(self.Deal_Frame, text="deal1", font=("times new roman", 13, 'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.Deal1_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.deal1, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        self.Deal2_label = Label(self.Deal_Frame, text="deal2", font=("times new roman", 13, 'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        self.Deal2_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.deal2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        self.Deal3_label = Label(self.Deal_Frame, text="deal3", font=("times new roman", 13, 'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        self.Deal3_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.deal3, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        self.Deal4_label = Label(self.Deal_Frame, text="deal4", font=("times new roman", 13, 'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        self.Deal4_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11, textvariable=self.deal4,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        self.Deal5_label = Label(self.Deal_Frame, text="deal5", font=("times new roman", 13, 'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        self.Deal5_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11, textvariable=self.deal5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        self.Deal6_label = Label(self.Deal_Frame, text="deal6", font=("times new roman", 13, 'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        self.Deal6_entry = Entry(self.Deal_Frame, font=("times new roman", 14, 'bold'), width=11, textvariable=self.deal6,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
    #***************************DRINKS DETAIL*****************************
        self.Drink_Frame=LabelFrame(self.root, text="Drink", bg="green", relief=GROOVE,font=("times new roman", 20, 'bold'))
        self.Drink_Frame.place(x=600, y=100, height=550, width=298)
        self.Drink1_label = Label(self.Drink_Frame, text="7UP", font=("times new roman", 13, 'bold')).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.Drink1_entry = Entry(self.Drink_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink1, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        self.Drink1_combox = ttk.Combobox(self.Drink_Frame, width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink1_combox.grid(row=0, column=2)
        self.Drink2_label = Label(self.Drink_Frame, text="Pepsi", font=("times new roman", 13, 'bold')).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        self.Drink2_entry = Entry(self.Drink_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        self.Drink2_combox = ttk.Combobox(self.Drink_Frame, width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink2_combox.grid(row=1, column=2)
        self.Drink3_label = Label(self.Drink_Frame ,text="DEW", font=("times new roman", 13, 'bold')).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        self.Drink3_entry = Entry(self.Drink_Frame ,font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink3, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        self.Drink3_combox = ttk.Combobox(self.Drink_Frame, width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink3_combox.grid(row=2, column=2)
        self.Drink4_label = Label(self.Drink_Frame ,text="Marinda", font=("times new roman", 13, 'bold')).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        self.Drink4_entry = Entry(self.Drink_Frame ,font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink4, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        self.Drink4_combox = ttk.Combobox(self.Drink_Frame,width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink4_combox.grid(row=3, column=2)
        self.Drink5_label = Label(self.Drink_Frame ,text="Coke", font=("times new roman", 13, 'bold')).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        self.Drink5_entry = Entry(self.Drink_Frame ,font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        self.Drink5_combox = ttk.Combobox(self.Drink_Frame, width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink5_combox.grid(row=4, column=2)
        self.Drink6_label = Label(self.Drink_Frame ,text="Sprite", font=("times new roman", 13, 'bold')).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        self.Drink6_entry = Entry(self.Drink_Frame ,font=("times new roman", 14, 'bold'), width=11,textvariable=self.Drink6, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        self.Drink6_combox = ttk.Combobox(self.Drink_Frame, width=5,values=["large", "jumbo", "regular", "345 ml", "2.15 ml", "1.5 ml"])
        self.Drink6_combox.grid(row=5, column=2)
    #***************otherDetail********************
        self.Other_Frame = LabelFrame(self.root, text="Other", bg="grey", relief=GROOVE,font=("times new roman", 20, 'bold'))
        self.Other_Frame.place(x=900, y=100, height=550, width=300)
        self.Salad_label = Label(self.Other_Frame, text="Salad", font=("times new roman", 13, 'bold')).grid(row=0, column=0,padx=10, pady=10,sticky="w")
        self.Salad_entry = Entry(self.Other_Frame, font=("times new roman", 14, 'bold'), width=11, textvariable=self.Other1,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        self.chickenPasta_label = Label(self.Other_Frame, text="ChickenPasta", font=("times new roman", 13, 'bold')).grid(row=1, column=0,padx=10, pady=10,sticky="w")
        self.chickenPast_entry = Entry(self.Other_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Other2, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        self.lasagna_label = Label(self.Other_Frame, text="lasagna pasta", font=("times new roman", 13, 'bold')).grid(row=2, column=0,padx=10, pady=10,sticky="w")
        self.lasagna_entry = Entry(self.Other_Frame, font=("times new roman", 14, 'bold'), width=11,textvariable=self.Other3, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

    #************Reciept************************
        self.Reciept_Frame = Frame(self.root, bg="white", relief=GROOVE)
        self.Reciept_Frame.place(x=1200, y=100, height=550, width=330)
        self.Reciept_label=Label(self.Reciept_Frame,text="Reciept",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).pack(fill=X)
        self.scrol_y=Scrollbar(self.Reciept_Frame,orient=VERTICAL)
        self.Reciept_text=Text(self.Reciept_Frame,yscrollcommand=self.scrol_y.set)
        self.scrol_y.pack(side=RIGHT,fill=Y)
        self.scrol_y.config(command=self.Reciept_text.yview)
        self.Reciept_text.pack(fill=BOTH,expand=1)
    #****************ButtonForm********************************
        self.Button_Frame=Frame(self.root,bg="blue", relief=GROOVE)
        self.Button_Frame.place(x=0,y=660,width=1500,height=150)
        self.Add_button = Button(self.Button_Frame,command=self.total_, text="Add", font=("times new roman", 13, 'bold')).place(x=200,y=40,width=100,height=60)
        self.Cancel_button = Button(self.Button_Frame, command=self.Clean,text="Cancel",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=40,y=40,width=100,height=60)
        self.Change_button = Button(self.Button_Frame, text="Change", font=("times new roman", 14, 'bold'), width=11,relief=SUNKEN).place(x=360,y=40,width=100,height=60)
        self.Logout_button = Button(self.Button_Frame, command=self.logout,text="LogOut", font=("times new roman", 14, 'bold'), width=11,relief=SUNKEN).place(x=520,y=40,width=100,height=60)
        self.Size_lable=Label(self.Button_Frame,text="Size",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=750,y=40,width=150,height=20)
        self.Size_Combox=ttk.Combobox(self.Button_Frame,width=20)
        self.Size_Combox["values"]=("small","larger","pan","regular","jumbo","1.5 ml","345 ml","2.15 ml")
        self.Size_Combox.place(x=920,y=40,width=150,height=20)
        self.Reciept_button=Button(self.Button_Frame,command=self.GenerateBill,text="Reciept",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=750,y=70,width=150,height=40)

        self.casheirNameLabel=Label(self.Button_Frame,text="ChasierName",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=40,width=160,height=20)
        self.casheirNameEntry = Label(self.Button_Frame,textvariable=self.casheirEmailEntry_,font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=40,width=150,height=20)
        self.casheirIDLabel=Label(self.Button_Frame,text="CashierID",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=70,width=160,height=20)
        self.casheirIDEntry = Label(self.Button_Frame,textvariable=self.casheirIDEntry_,font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=70,width=150,height=20)
        self.casheirEmailLabel=Label(self.Button_Frame,text="CashierEmail",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=100,width=160,height=20)
        self.casheirEmailEntry = Label(self.Button_Frame,textvariable=self.casheirEmailEntry_,font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=100,width=150,height=20)
        self.total=IntVar()
        self.TotalLabel=Label(self.Button_Frame,textvariable=self.total,bg="white",fg="green",font=("times new roma",16,"bold"), width=11, relief=FLAT).place(x=920,y=70,width=150,height=40)
    def RecieptGenerate_title(self):
        self.tokenNo=random.randrange(1001,2000)
        self.date=datetime.now()
        self.Reciept_text.delete("1.0",END)
        self.Reciept_text.insert(END,"\tSale Reciept")
        self.Reciept_text.insert(END, "\nCashier Name:")
        self.Reciept_text.insert(END, f"\nInvoice #:{self.tokenNo}")
        self.Reciept_text.insert(END, f"\nInvDate:{self.date}")
        self.Reciept_text.insert(END, "\nCostumer Name:Mr.Walking Costumer")
        self.Reciept_text.insert(END, "\n*************************************")
        self.Reciept_text.insert(END, "\nItemName   Price   Qty         Amount")
        self.Reciept_text.insert(END, "\n*************************************")

    def Clean(self):
        self.Drink6.set(0)
        self.Drink5.set(0)
        self.Drink2.set(0)
        self.Drink3.set(0)
        self.Drink1.set(0)
        self.Drink4.set(0)

        self.Other1.set(0)
        self.Other3.set(0)
        self.Other2.set(0)

        self.deal1.set(0)
        self.deal2.set(0)
        self.deal3.set(0)
        self.deal4.set(0)
        self.deal5.set(0)
        self.deal6.set(0)

        self.Pizza1.set(0)
        self.Pizza2.set(0)
        self.Pizza3.set(0)
        self.Pizza4.set(0)
        self.Pizza5.set(0)
        self.Pizza6.set(0)
        self.Pizza7.set(0)
        self.Pizza8.set(0)
        self.Pizza9.set(0)
        self.Pizza10.set(0)
        self.total.set(0)
        self.Reciept_text.delete("1.0",END)
    def Update(self):
        pass
    def logout(self):
        self.root.quit()
    def GenerateBill(self):
        self.RecieptGenerate_title()
        self.SalesTax=self.grand_total*.20
        self.totals=self.SalesTax+self.grand_total
        if self.deal1.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal1\t   {self.deals['deal1']['price'] }\t    {self.deal1.get()}\t\t{self.d1_p}")
        if self.deal2.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal2\t   {self.deals['deal2']['price'] }\t    {self.deal2.get()}\t\t{self.d2_p}")
        if self.deal3.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal3\t   {self.deals['deal3']['price'] }\t    {self.deal3.get()}\t\t{self.d3_p}")
        if self.deal4.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal4\t   {self.deals['deal4']['price'] }\t    {self.deal4.get()}\t\t{self.d4_p}")
        if self.deal5.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal5\t   {self.deals['deal5']['price'] }\t    {self.deal5.get()}\t\t{self.d5_p}")
        if self.deal6.get()!=0:
            self.Reciept_text.insert(END,f"\nDeal6\t   {self.deals['deal6']['price'] }\t    {self.deal6.get()}\t\t{self.d6_p}")
        #
        if self.Other1.get()!=0:
            self.Reciept_text.insert(END,f"\n{self.Others['Other1']['Name']}\t   {self.Others['Other1']['Price']}\t    {self.Other1.get()}\t\t{self.o1_p}")
        if self.Other2.get()!=0:
            self.Reciept_text.insert(END,f"\nD{self.Others['Other2']['Name']}\t   {self.Others['Other2']['Price']}\t   {self.Other2.get()}\t\t{self.o2_p}")
        if self.Other3.get()!=0:
            self.Reciept_text.insert(END,f"\n{self.Others['Other3']['Name']}\t   {self.Others['Other3']['Price']}\t    {self.Other3.get()}\t\t{self.o3_p}")
        # if self.Pizza1.get()!=0:
        #     if self.pizza1_combox.get()=="large":
        #         self.pizza1_amt=int(self.Pizza1.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza1']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza1.get()}\t\t{self.pizza1_amt}")
        #     elif self.pizza1.get()=="jumbo":
        #         self.pizza1_amt = int(self.Pizza1.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza1']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza1.get()}\t\t{self.pizza1_amt}")
        #     elif self.pizza1_combox=="regular":
        #         self.pizza1_amt = int(self.Pizza1.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza1']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza1.get()}\t\t{self.pizza1_amt}")
        #     else:
        #         return 0
        # if self.Pizza2.get()!=0:
        #     if self.pizza2_combox.get()=="large":
        #         self.pizza2_amt=int(self.Pizza2.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza2']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza2.get()}\t\t{self.pizza2_amt}")
        #     elif self.pizza2.get()=="jumbo":
        #         self.pizza2_amt = int(self.Pizza2.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza2']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza2.get()}\t\t{self.pizza2_amt}")
        #     elif self.pizza2_combox=="regular":
        #         self.pizza2_amt = int(self.Pizza2.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza2']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza2.get()}\t\t{self.pizza2_amt}")
        #     else:
        #         return 0
        # if self.Pizza3.get()!=0:
        #     if self.pizza3_combox.get()=="large":
        #         self.pizza3_amt=int(self.Pizza3.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza3']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza3.get()}\t\t{self.pizza3_amt}")
        #     elif self.pizza3.get()=="jumbo":
        #         self.pizza3_amt = int(self.Pizza3.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza3']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza3.get()}\t\t{self.pizza3_amt}")
        #     elif self.pizza3_combox=="regular":
        #         self.pizza3_amt = int(self.Pizza1.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza3']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza3.get()}\t\t{self.pizza3_amt}")
        #     else:
        #         return 0
        # if self.Pizza4.get()!=0:
        #     if self.pizza4_combox.get()=="large":
        #         self.pizza4_amt=int(self.Pizza4.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza4']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza4.get()}\t\t{self.pizza4_amt}")
        #     elif self.pizza4.get()=="jumbo":
        #         self.pizza4_amt = int(self.Pizza4.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza4']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza4.get()}\t\t{self.pizza4_amt}")
        #     elif self.pizza4_combox=="regular":
        #         self.pizza4_amt = int(self.Pizza4.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza4']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza4.get()}\t\t{self.pizza4_amt}")
        #     else:
        #         return 0
        # if self.Pizza5.get()!=0:
        #     if self.pizza5_combox.get()=="large":
        #         self.pizza5_amt=int(self.Pizza1.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza5']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza5.get()}\t\t{self.pizza5_amt}")
        #     elif self.pizza5.get()=="jumbo":
        #         self.pizza5_amt = int(self.Pizza5.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza5']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza5.get()}\t\t{self.pizza5_amt}")
        #     elif self.pizza5_combox=="regular":
        #         self.pizza5_amt = int(self.Pizza5.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza5']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza5.get()}\t\t{self.pizza5_amt}")
        #     else:
        #         return 0
        # if self.Pizza6.get()!=0:
        #     if self.pizza6_combox.get()=="large":
        #         self.pizza6_amt=int(self.Pizza6.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza6']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza6.get()}\t\t{self.pizza6_amt}")
        #     elif self.pizza6.get()=="jumbo":
        #         self.pizza6_amt = int(self.Pizza6.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza6']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza6.get()}\t\t{self.pizza6_amt}")
        #     elif self.pizza6_combox=="regular":
        #         self.pizza6_amt = int(self.Pizza6.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza6']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza6.get()}\t\t{self.pizza6_amt}")
        #     else:
        #         return 0
        # if self.Pizza7.get()!=0:
        #     if self.pizza7_combox.get()=="large":
        #         self.pizza7_amt=int(self.Pizza7.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza7']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza7.get()}\t\t{self.pizza7_amt}")
        #     elif self.pizza7.get()=="jumbo":
        #         self.pizza7_amt = int(self.Pizza7.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza7']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza7.get()}\t\t{self.pizza7_amt}")
        #     elif self.pizza7_combox=="regular":
        #         self.pizza7_amt = int(self.Pizza7.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza7']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza7.get()}\t\t{self.pizza7_amt}")
        #     else:
        #         return 0
        # if self.Pizza8.get()!=0:
        #     if self.pizza8_combox.get()=="large":
        #         self.pizza8_amt=int(self.Pizza8.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza8']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza8.get()}\t\t{self.pizza8_amt}")
        #     elif self.pizza8.get()=="jumbo":
        #         self.pizza8_amt = int(self.Pizza8.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza8']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza8.get()}\t\t{self.pizza8_amt}")
        #     elif self.pizza8_combox=="regular":
        #         self.pizza8_amt = int(self.Pizza8.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza8']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza8.get()}\t\t{self.pizza8_amt}")
        #     else:
        #         return 0
        # if self.Pizza9.get()!=0:
        #     if self.pizza9_combox.get()=="large":
        #         self.pizza9_amt=int(self.Pizza9.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza9']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza9.get()}\t\t{self.pizza9_amt}")
        #     elif self.pizza9.get()=="jumbo":
        #         self.pizza9_amt = int(self.Pizza9.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza9']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza9.get()}\t\t{self.pizza9_amt}")
        #     elif self.pizza9_combox=="regular":
        #         self.pizza9_amt = int(self.Pizza9.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza9']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza9.get()}\t\t{self.pizza9_amt}")
        #     else:
        #         return 0
        # if self.Pizza10.get()!=0:
        #     if self.pizza10_combox.get()=="large":
        #         self.pizza10_amt=int(self.Pizza10.get()*self.Size["large"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza10']['Name']}\t   {self.Size['large']['Price']}\t    {self.Pizza10.get()}\t\t{self.pizza10_amt}")
        #     elif self.pizza10.get()=="jumbo":
        #         self.pizza10_amt = int(self.Pizza10.get() * self.Size["jumbo"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza10']['Name']}\t   {self.Size['jumbo']['Price']}\t    {self.Pizza10.get()}\t\t{self.pizza10_amt}")
        #     elif self.pizza10_combox=="regular":
        #         self.pizza10_amt = int(self.Pizza10.get() * self.Size["regular"]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Pizzas['pizza10']['Name']}\t   {self.Size['regular']['Price']}\t    {self.Pizza10.get()}\t\t{self.pizza10_amt}")
        #     else:
        #         return 0
        # if self.Drink1.get()!=0:
        #     if self.Drink1_combox.get()=="345 ml":
        #         self.dr1_amt=int(self.Drink1.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink1']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr1_amt}")
        #     elif self.Drink1_combox.get()=="1.5 ml":
        #         self.dr1_amt=int(self.Drink1.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink1']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr1_amt}")
        #     elif self.Drink1_combox.get() == "2.15 ml":
        #         self.dr1_amt = int(self.Drink1.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink1']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr1_amt}")
        #     else:
        #         return 0
        # if self.Drink2.get()!=0:
        #     if self.Drink2_combox.get()=="345 ml":
        #         self.dr2_amt=int(self.Drink2.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink2']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr2_amt}")
        #     elif self.Drink2_combox.get()=="1.5 ml":
        #         self.dr2_amt=int(self.Drink2.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink2']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr2_amt}")
        #     elif self.Drink2_combox.get() == "2.15 ml":
        #         self.dr2_amt = int(self.Drink2.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink2']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink1.get()}\t\t{self.dr2_amt}")
        #     else:
        #         return 0
        # if self.Drink3.get()!=0:
        #     if self.Drink3_combox.get()=="345 ml":
        #         self.dr3_amt=int(self.Drink3.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink3']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink3.get()}\t\t{self.dr3_amt}")
        #     elif self.Drink3_combox.get()=="1.5 ml":
        #         self.dr3_amt=int(self.Drink3.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink3']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink3.get()}\t\t{self.dr3_amt}")
        #     elif self.Drink3_combox.get() == "2.15 ml":
        #         self.dr3_amt = int(self.Drink3.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink3']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink3.get()}\t\t{self.dr3_amt}")
        #     else:
        #         return 0
        # if self.Drink4.get()!=0:
        #     if self.Drink4_combox.get()=="345 ml":
        #         self.dr4_amt=int(self.Drink4.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink4']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink4.get()}\t\t{self.dr4_amt}")
        #     elif self.Drink4_combox.get()=="1.5 ml":
        #         self.dr4_amt=int(self.Drink4.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink4']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink4.get()}\t\t{self.dr4_amt}")
        #     elif self.Drink4_combox.get() == "2.15 ml":
        #         self.dr4_amt = int(self.Drink4.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink4']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink4.get()}\t\t{self.dr4_amt}")
        #     else:
        #         return 0
        # if self.Drink5.get()!=0:
        #     if self.Drink5_combox.get()=="345 ml":
        #         self.dr5_amt=int(self.Drink5.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink5']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink5.get()}\t\t{self.dr5_amt}")
        #     elif self.Drink5_combox.get()=="1.5 ml":
        #         self.dr5_amt=int(self.Drink5.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink5']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink5.get()}\t\t{self.dr5_amt}")
        #     elif self.Drink5_combox.get() == "2.15 ml":
        #         self.dr5_amt = int(self.Drink5.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink5']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink5.get()}\t\t{self.dr5_amt}")
        #     else:
        #         return 0
        #
        # if self.Drink6.get()!=0:
        #     if self.Drink6_combox.get()=="345 ml":
        #         self.dr6_amt=int(self.Drink6.get()*self.Size["345 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink6']['Name']}\t   {self.Size['345 ml']['Price']}\t    {self.Drink6.get()}\t\t{self.dr6_amt}")
        #     elif self.Drink6_combox.get()=="1.5 ml":
        #         self.dr6_amt=int(self.Drink6.get()*self.Size["1.5ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink6']['Name']}\t   {self.Size['1.5 ml']['Price']}\t    {self.Drink6.get()}\t\t{self.dr6_amt}")
        #     elif self.Drink6_combox.get() == "2.15 ml":
        #         self.dr6_amt = int(self.Drink6.get() * self.Size["2.15 ml "]["Price"])
        #         self.Reciept_text.insert(END,f"\n{self.Drinks['Drink6']['Name']}\t   {self.Size['2.15 ml']['Price']}\t    {self.Drink6.get()}\t\t{self.dr6_amt}")
        #     else:
        #         return 0
        self.Reciept_text.insert(END,f"\n\nTotal\t\t{self.grand_total}\nSales Tax\t\t{self.SalesTax}\nNet Amount\t\t{self.totals}")
        self.detail_tuple = (self.tokenNo,self.date, self.totals)

        self.s1.Insert(self.detail_tuple[0],self.detail_tuple[2],self.detail_tuple[1])
        self.total_()
    def total_(self):
        # self.GenerateBill()
        self.deals = {"deal1": {"price": 349, "Detail": "6Inch PIzza & Cold Drink(345ml)"},
                        "deal2":{"price":949,"Detail":"RegularPizza & 2Drinks(345ml)"},
                        "deal3":{"price":1349,"Detail":"12Inch Large Pizza & Drink(1.5ltr"},
                        "deal4":{"price":2349,"Detail":"16Inch JumboPizza & Drink(1.5ltr)"},
                        "deal5":{"price":599,"Detail":"LasagnePasta & Drink(345ml)"},
                        "deal6":{"price":3449,"Detail":"2LargePizza & 5Drink(345ml)"}}

        #
        # self.Drinks={"Drink1":{"Name":"Sevenup"},
        #                 "Drink2":{"Name":"Pepsi"},
        #                 "Drink3":{"Name":"Dew"},
        #                 "Drink4":{"Name":"Marinda"},
        #                 "Drink5":{"Name":"Coke"},
        #                 "Drink6":{"Name":"Sprite"}}

        self.Others={"Other1":{"Price":300,"Name":"Salad"},
                         "Other2":{"Price":500,"Name":"LasagnaPasta"},
                         "Other3":{"Price":700,"Name":"ChickenPasta"}}
        #
        # self.Size={"large":{"Price":1500},
        #                  "regular":{"Price":500},
        #                  "jumbo":{"Price":1800},
        #                  "345 ml": {"Price": 50},
        #                  "1.5 ml": {"Price": 90},
        #                  "2.15 ml": {"Price": 160}}
        # self.Pizzas={"pizza1":{"Name":"ChickenTikka"},"pizza2":{"Name":"ChickenFajita"},"pizza3":{"Name":"BeepSupreame"},
        #              "pizza4":{"Name":"SuperSupreame"},"pizza5":{"Name":"CheeseLover"},"pizza6":{"Name":"VeggieLover"},
        #              "pizza7":{"Name":"ChickenSupreame"},"pizza8":{"Name":"FajitaScilian"},
        #              "pizza9":{"Name":"CreamyTikka"},"pizza10":{"Name":"Cheese and Peproni"}}

        self.d1_p=self.deal1.get()*self.deals["deal1"]["price"]
        self.d2_p=self.deal2.get()*self.deals["deal2"]["price"]
        self.d3_p=self.deal3.get()*self.deals["deal3"]["price"]
        self.d4_p=self.deal4.get()*self.deals["deal4"]["price"]
        self.d5_p=self.deal5.get()*self.deals["deal5"]["price"]
        self.d6_p=self.deal6.get()*self.deals["deal6"]["price"]

        self.o1_p=self.Other1.get()*self.Others["Other1"]["Price"]
        self.o2_p = self.Other2.get() * self.Others["Other2"]["Price"]
        self.o3_p = self.Other3.get() * self.Others["Other3"]["Price"]

        self.total_others=float(self.o1_p+self.o2_p+self.o3_p)
        self.total_deals=float(self.d1_p+self.d2_p+self.d3_p+self.d4_p+self.d5_p+self.d6_p)
        # self.total_drinks=float(self.dr1_amt+self.dr2_amt+self.dr3_amt+self.dr4_amt+self.dr4_amt+self.dr5_amt+self.dr6_amt)
        # self.total_pizzas=float(self.pizza1_amt+self.pizza2_amt+self.pizza3_amt+self.pizza3_amt+self.pizza4_amt+self.pizza5_amt+self.pizza6_amt+
        #                         self.pizza7_amt+self.pizza8_amt+self.pizza9_amt+self.pizza10_amt)
        self.grand_total=float(self.total_deals+self.total_others)
        self.total.set("Rs: "+str(self.grand_total))



class MenuPos(MenuFORM):
    def __init__(self):
        root=tk.Tk()
        ob1=MenuFORM(root)
        ob1.Menu()
        root.mainloop()




# if __name__=="__main__":
#     # root=tk.Tk()
#     # menu=MenuFORM(root)
#     # menu.Menu()
#     # root.mainloop()
obj1=MenuPos()