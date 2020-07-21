import tkinter as tk
from tkinter import *
from tkinter import  ttk

class MenuFORM:
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
        self.Reciept_Frame.place(x=1200, y=100, height=550, width=300)
        self.Reciept_label=Label(self.Reciept_Frame,text="Reciept",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).pack(fill=X)
        self.scrol_y=Scrollbar(self.Reciept_Frame,orient=VERTICAL)
        self.Reciept_text=Text(self.Reciept_Frame,yscrollcommand=self.scrol_y.set)
        self.scrol_y.pack(side=RIGHT,fill=Y)
        self.scrol_y.config(command=self.Reciept_text.yview)
        self.Reciept_text.pack(fill=BOTH,expand=1)
    #****************ButtonForm********************************
        self.Button_Frame=Frame(self.root,bg="blue", relief=GROOVE)
        self.Button_Frame.place(x=0,y=660,width=1500,height=150)
        self.Add_button = Button(self.Button_Frame,command=self.TotalAmmount, text="Add", font=("times new roman", 13, 'bold')).place(x=200,y=40,width=100,height=60)
        self.Cancel_button = Button(self.Button_Frame, text="Cancel",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=40,y=40,width=100,height=60)
        self.Change_button = Button(self.Button_Frame, text="Change", font=("times new roman", 14, 'bold'), width=11,relief=SUNKEN).place(x=360,y=40,width=100,height=60)
        self.Logout_button = Button(self.Button_Frame, text="LogOut", font=("times new roman", 14, 'bold'), width=11,relief=SUNKEN).place(x=520,y=40,width=100,height=60)
        self.Size_lable=Label(self.Button_Frame,text="Size",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=750,y=40,width=150,height=20)
        self.Size_Combox=ttk.Combobox(self.Button_Frame,width=20)
        self.Size_Combox["values"]=("small","larger","pan","regular","jumbo")
        self.Size_Combox.place(x=920,y=40,width=150,height=20)
        self.Reciept_button=Button(self.Button_Frame,text="Reciept",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=750,y=70,width=150,height=40)

        self.casheirNameLabel=Label(self.Button_Frame,text="ChasierName",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=40,width=160,height=20)
        self.casheirNameEntry = Label(self.Button_Frame,text="Name",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=40,width=150,height=20)
        self.casheirIDLabel=Label(self.Button_Frame,text="CashierID",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=70,width=160,height=20)
        self.casheirIDEntry = Label(self.Button_Frame,text="ID",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=70,width=150,height=20)
        self.casheirEmailLabel=Label(self.Button_Frame,text="CashierEmail",bg="black",fg="white",font=("times new roma",16,"bold"),relief=GROOVE).place(x=1080,y=100,width=160,height=20)
        self.casheirEmailEntry = Label(self.Button_Frame,text="Email",font=("times new roman", 14, 'bold'), width=11, relief=SUNKEN).place(x=1250,y=100,width=150,height=20)
        self.total=IntVar()
        self.TotalLabel=Label(self.Button_Frame,textvariable=self.total,bg="white",fg="green",font=("times new roma",16,"bold"), width=11, relief=FLAT).place(x=920,y=70,width=150,height=40)
    # def TotalAmmount(self):
    #     self.deals={"deal1":{"price":349,"Detail":"abc"}}
    #     self.total_ammount=(
    #         (self.deal1.get()*self.deals["deal1"]["price"])+(self.deal2.get()*200)+(self.deal3.get()*200)+(self.deal4.get()*200)+(self.deal5.get()*200)+(self.deal6.get()*200))
    #         # (self.Pizza1.get())+(self.Pizza2.get())+(self.Pizza3.get())+(self.Pizza4.get())+(self.Pizza5.get())+(self.Pizza6.get())+(self.Pizza7.get())+(self.Pizza8.get())+(self.Pizza9.get())+(self.Pizza10.get())+
    #         # (self.Drink1.get())+(self.Drink2.get())+(self.Drink3.get())+(self.Drink4.get())+(self.Drink5.get())+(self.Drink6.get())+
    #         # (self.Other1.get())+(self.Other2.get())+(self.Other3.get()))
    #     self.total.set(str(self.total_ammount))
class MainMenu(MenuFORM):
    def __init__(self,root):
        super().__init__(root)
    def Menu(self):
        super().Menu()
    def TotalAmmount(self):
        self.deals={"deal1":{"price":349,"Detail":"6Inch PIzza & Cold Drink(345ml)"},
                    "deal2":{"price":949,"Detail":"RegularPizza & 2Drinks(345ml)"},
                    "deal3":{"price":1349,"Detail":"12Inch Large Pizza & Drink(1.5ltr"},
                    "deal4":{"price":2349,"Detail":"16Inch JumboPizza & Drink(1.5ltr)"},
                    "deal5":{"price":599,"Detail":"LasagnePasta & Drink(345ml)"},
                    "deal6":{"price":3449,"Detail":"2LargePizza & 5Drink(345ml)"}}

        self.Drinks={"Drink1":{"Price":100,"Name":"Sevenup"},
                     "Drink1":{"Price":100,"Name":"Pepsi"},
                     "Drink1":{"Price":100,"Name":"Dew"},
                     "Drink1":{"Price":100,"Name":"Marinda"},
                     "Drink1":{"Price":100,"Name":"Coke"},
                     "Drink1":{"Price":100,"Name":"Sprite"}}

        self.Others={"Other1":{"Price":300,"Name":"Salad"},
                     "Other1":{"Price":500,"Name":"LasagnaPast"},
                     "Other1":{"Price":700,"Name":"ChickenTikka"}}

        self.Size={"large":{"Price":1500},
                     "regular":{"Price":500},
                     "jumbo":{"Price":1800},
                     "345ml": {"Price": 50},
                     "1.5ml": {"Price": 90},
                     "2.15ml": {"Price": 160}}
        self.total_ammount=(
                ((self.deal1.get()*self.deals["deal1"]["price"])+
            (self.deal2.get()*self.deals["deal2"]["price"])+
            (self.deal3.get()*self.deals["deal3"]["price"])+
            (self.deal4.get()*self.deals["deal4"]["price"])+
            (self.deal5.get()*self.deals["deal5"]["price"])+
            (self.deal6.get()*self.deals["deal6"]["price"]))+
            # (self.Pizza1.get()*self.Size)+(self.Pizza2.get())+(self.Pizza3.get())+(self.Pizza4.get())+(self.Pizza5.get())+(self.Pizza6.get())+(self.Pizza7.get())+(self.Pizza8.get())+(self.Pizza9.get())+(self.Pizza10.get())+
                ((self.Drink1.get()*self.Drinks["Drink1"]["Price"])+(self.Drink2.get()*self.Drinks["Drink2"]["Price"])+
            (self.Drink3.get()*self.Drinks["Drink3"]["Price"])+(self.Drink4.get()*self.Drinks["Drink4"]["Price"])+
            (self.Drink5.get()*self.Drinks["Drink5"]["Price"])+(self.Drink6.get()*self.Drinks["Drink6"]["Price"]))+
            (self.Other1.get()*self.Others["Other1"]["Price"])+(self.Other2.get()*self.Others["Other2"]["Price"])+
                (self.Other3.get()*self.Others["Other3"]["Price"]))
        self.total.set(str(self.total_ammount))




if __name__=="__main__":
    root=tk.Tk()
    # menu=Menu(root)
    # menu.Menu()
    m1=MainMenu(root)
    m1.Menu()
    root.mainloop()