import tkinter as tk
from tkinter import ttk
class Login:
    def __init__(self,root):
        self.root=root

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
        pass
    def Cancel(self):
        self.root.quit()

if __name__=="__main__":

    root = tk.Tk()
    root.geometry("300x300")
    root.title("LOGIN")
    obj = Login(root)
    root.mainloop()
