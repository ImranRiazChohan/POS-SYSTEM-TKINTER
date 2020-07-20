import tkinter as tk
from tkinter import *
from tkinter import  ttk

class Menu:
    def __init__(self,root):
        self.root=root
        self.title=Label(self.root,text="CALFORNIA POINT OF SALE SYSTEM",relief=RIDGE).pack(fill=X,ipady=20)

        #*******************FRAMES********************
        self.MenuForm=Frame(self.root,relief=FLAT,bd=12).place(x=0,y=80,height=550,width=300)
        self.RecieptForm = Frame(self.root, relief=FLAT,bd=12).place(x=310,y=80,height=550,width=300)
        self.OrderForm = Frame(self.root, relief=FLAT,bd=12).place(x=620,y=80,height=550,width=300)
        self.ButtonForm = Frame(self.root, relief=FLAT,bd=12).place(x=0,y=620,height=180,width=920)
        # #*******************RecieptText***********************
        self.RecieptText=Text(self.RecieptForm,relief=FLAT,bd=12).place(x=310,y=80,height=550,width=300)

        #*****************SET ALL BUTTONS IN MENU FORM**************************
        self.Deal1 = Button(self.MenuForm, text="Deal1").place(x=10, y=80, height=50, width=100)
        self.Deal2 = Button(self.MenuForm, text="Deal2").place(x=10, y=130, height=50, width=100)
        self.Deal3 = Button(self.MenuForm, text="Deal3").place(x=10, y=180, height=50, width=100)
        self.Deal4 = Button(self.MenuForm, text="Deal4").place(x=10, y=230, height=50, width=100)
        self.Deal5 = Button(self.MenuForm, text="Deal5").place(x=10, y=280, height=50, width=100)
        self.sevenUpDrink = Button(self.MenuForm, text="SevenUp").place(x=150, y=80, height=50, width=120)
        self.MarindaDrink = Button(self.MenuForm, text="Marinda").place(x=150, y=130, height=50, width=120)
        self.DewDrink = Button(self.MenuForm, text="DEW").place(x=150, y=180, height=50, width=120)
        self.PepsiDrink = Button(self.MenuForm, text="Pepsi").place(x=150, y=230, height=50, width=120)
        self.Salad = Button(self.MenuForm, text="Salad").place(x=150, y=280, height=50, width=120)
        self.LasagnePasta = Button(self.MenuForm, text="Lasagne Pasta").place(x=10, y=330, height=50, width=100)
        self.ChickenPasta = Button(self.MenuForm, text="Chicken Pasta").place(x=10, y=380, height=50, width=100)
        self.Pizza1 = Button(self.MenuForm, text="creamyTikka").place(x=10, y=430, height=50, width=100)
        self.Pizza2 = Button(self.MenuForm, text="superSupreame").place(x=10, y=480, height=50, width=100)
        self.Pizza3= Button(self.MenuForm, text="ChickenFajita").place(x=10, y=530, height=50, width=100)
        self.Pizza4 = Button(self.MenuForm, text="Beep and Peproni").place(x=150, y=330, height=50, width=120)
        self.Pizza5 = Button(self.MenuForm, text="Cheese Lover").place(x=150, y=380, height=50, width=120)
        self.Pizza6 = Button(self.MenuForm, text="Veggie Lover").place(x=150, y=430, height=50, width=120)
        self.Pizza7 = Button(self.MenuForm, text="ChickenTikka").place(x=150, y=480, height=50, width=120)
        self.Pizza8 = Button(self.MenuForm, text="FajitaScilian").place(x=150, y=530, height=50, width=120)
        self.Pizza9 = Button(self.MenuForm, text="ChickenSupreame").place(x=10, y=580, height=50, width=100)
        self.Pizza10 = Button(self.MenuForm, text="Beep Supreame").place(x=150, y=580, height=50, width=120)
        # **************************Set Button in OrderForm**********************************************
        self.CashierNameLabel=Label(self.OrderForm,text="CashierName: ").place(x=620,y=80,height=20,width=110)
        self.CashierEmailLabel=Label(self.OrderForm,text="CashierEMAIL: ").place(x=620,y=110,height=20,width=110)
        self.CashierIDLabel=Label(self.OrderForm,text="CashierID: ").place(x=620,y=140,height=20,width=110)
        self.CahierID=Label(self.OrderForm,text="none").place(x=750,y=140,height=20,width=110)
        self.CashierEmail=Label(self.OrderForm,text="none").place(x=750,y=110,height=20,width=110)
        self.CashierName=Label(self.OrderForm,text="none").place(x=750,y=80,height=20,width=110)
        self.Reciept_button=Button(self.OrderForm,text="Reciept").place(x=720,y=400,height=50,width=110)
        self.size_label=Label(self.OrderForm,text="Size: ").place(x=620,y=500,height=50,width=110)
        self.Quantity_label=Label(self.OrderForm,text="Quantity: ").place(x=620,y=550,height=50,width=110)
        self.size_combox=ttk.Combobox(self.OrderForm).place(x=720,y=515,height=20,width=130)
        self.Quantity_combox=ttk.Combobox(self.OrderForm).place(x=720,y=560,height=20,width=130)
        self.Logout_button=Button(self.OrderForm,text="LogOut").place(x=620,y=600,height=30,width=280)

        #*************************set Button in INPUTForm*************************************************
        self.add_Order=Button(self.ButtonForm,text="Add_Order").place(x=650,y=670,height=50,width=110)
        self.Change_Order=Button(self.ButtonForm,text="Change_Order").place(x=770,y=670,height=50,width=110)
        self.Cancel_order=Button(self.ButtonForm,text="Cancel_Order").place(x=710,y=730,height=50,width=110)




if __name__=="__main__":
    root=tk.Tk()
    menu=Menu(root)
    root.geometry("920x800")
    root.mainloop()