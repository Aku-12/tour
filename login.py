from tkinter import *
from tkinter import messagebox

ak = Tk()

ak.title("Login Form")  
ak.geometry("700x500")
ak.resizable(1, 1)
ak.iconbitmap("train.ico")


def login():
    Username = "akash"
    Password = "12345"
    if User_entry.get() == Username and Password_entry.get() == Password:
        messagebox.showinfo(title="Login Success",
                            message="You succesfully logged in.")
        print("Succesfully logged in")
        ak.destroy()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
        print("Invalid login")


# Frame=ak.frame()
ak.configure(bg="black")
Login_Label = Label(ak, text="Tour and Travel Login    ", font=("fontstyle", 30, "bold"), fg="blue")
User_Label= Label(ak, text="Username", font=80)
User_entry = Entry(ak)
Password_Label = Label(ak, text="Password", font=80)
Password_entry= Entry(ak, show="*")
# d=Label(ak,text="Login",font=80)
Login_button = Button(ak, text="Login", fg="blue", command=login)
Login_Label.pack()
User_Label.place(x=75, y=75)
User_entry.place(x=175, y=80)
Password_Label.place(x=75, y=150)
Password_entry.place(x=175, y=155)
# d.pack(fill=X,expand=True)
Login_button.place(x=310, y=215)


ak.mainloop()
