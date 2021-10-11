from tkinter import *
import json
from tkinter import messagebox
import random
def main_screen():
    root = Tk()
    root.geometry("400x150")
    root.title("MainPage")
    def toregister():
        root.destroy()
        register_screen()
    registerbutton = Button(root, text="Register",command=toregister).pack(anchor=CENTER)
    def tologin():
        root.destroy()
        login_screen()
    loginbutton = Button(root, text="Login",command=tologin).pack(anchor=CENTER)
    root.mainloop()
    
def register_screen():
    tkwindow = Tk()
    tkwindow.geometry("400x150")
    tkwindow.title("Register")
    mainlabel = Label(tkwindow, text="Register").grid(row=0, column=1)
    eLabel = Label(tkwindow, text="UserName").grid(row=1, column=0)
    username = StringVar()
    e = Entry(tkwindow, width=50)
    e.grid(row=1, column=1)
    fLabel = Label(tkwindow,text="Password").grid(row=2, column=0)
    password = StringVar()
    f = Entry(tkwindow,textvariable=password,show="*", width=50)
    f.grid(row=2, column=1)
    def save():
        if len(e.get()) > 10:
            messagebox.showerror("Length of username","Username is too long, you must have less than 10 characters")
        elif len(f.get()) < 8:
            messagebox.showerror("Length of password","Password is too short, you must have more than 8 characters")
        else:
            with open("user.json") as file:
                data = json.load(file)
                data[e.get()] = {"Username":e.get(),"Password":f.get(),"Money":0}
            with open("user.json","w") as file:
                json.dump(data,file)
        messagebox.showinfo("Saved","Your info has been saved to our database")   
    myButton = Button(tkwindow, text="Register",command=save).grid(row=4, column=1)
    def readytologin():
        tkwindow.destroy()
        login_screen()
    loginbuttonlabel = Label(tkwindow, text="if you registered succesfully click the button below").grid(row=7, column=1)
    Loginbuttonbottom = Button(tkwindow, text="login",command=readytologin).grid(row=8, column=1)
    tkwindow.mainloop()
def login_screen():
    root1 = Tk()
    root1.geometry("400x150")
    root1.title("Login")
    eLabel = Label(root1, text="UserName").grid(row=0, column=0)
    username = StringVar()
    e = Entry(root1, width=50)
    e.grid(row=0, column=1)
    fLabel = Label(root1,text="Password").grid(row=1, column=0)
    password = StringVar()
    f = Entry(root1,textvariable=password,show="*", width=50)
    f.grid(row=1, column=1)
    message_text = Label(root1,text="");message_text.grid(row=3, column=1)
    def login():
        with open("user.json") as file:
            data = json.load(file)
        if e.get() not in data:
            messagebox.showerror("Wrong Credentials","Info not in database")
        elif f.get() == data[e.get()]["Password"]:
            root1.destroy()
            bank_screen()
        else:
            message_text["text"] = "Something went wrong"
    firstbutton = Button(root1, text="login",command=login).grid(row=2, column=1)
    root1.mainloop()
def bank_screen():
    bank1 = Tk()
    bank1.geometry("400x150")
    bank1.title("Bank")
    klabel = Label(bank1, text="UserName").grid(row=0, column=0)
    k = Entry(bank1, width=50)
    k.grid(row=0, column=1)
    lLabel = Label(bank1,text="Amount").grid(row=1, column=0)
    l = Entry(bank1, width=50)
    l.grid(row=1, column=1)
    def add():
        with open("user.json") as file:
            data = json.load(file)
        if k.get() not in data:
            messagebox.showerror("Username not found","")
        else:
            data[k.get()]["Money"] += int(l.get())
            with open ("user.json","w") as file:
                json.dump(data,file)
            amount = data[k.get()]["Money"]
    addbutton = Button(bank1, text="Add",command=add).grid(row=2, column=1)
    def subtract():
        with open("user.json") as file:
            data = json.load(file)
        if k.get() not in data:
            messagebox.showerror("Username not found","")
        else:
            data[k.get()]["Money"] -= int(l.get())
            with open ("user.json","w") as file:
                json.dump(data,file)
            amount = data[k.get()]["Money"]
    subtract = Button(bank1, text="Subtract",command=subtract).grid(row=3, column=1)
    def view():
        with open("user.json") as file:
            data = json.load(file)
        if k.get() not in data:
            messagebox.showerror("Username not found","")
        else:
            f = data[k.get()]["Money"]
            messagebox.showinfo("Amount",f"Amount:${f}")  
    view1 = Button(bank1, text="View",command=view).grid(row=5, column=1)
    bank1.mainloop()
main_screen()