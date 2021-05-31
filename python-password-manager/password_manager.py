import pandas as pd
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import string
import json

# Retrieving saved passwords
def search_website():
    website = entry_website.get()
    try:
        with open(r'passwords.json', 'r') as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        tkinter.messagebox.showerror(title='Error',
                                     message="The database is empty!")
    else:
        if website in data:
            tkinter.messagebox.showinfo(title=f"{website}",
                                        message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        elif website=='':
            tkinter.messagebox.showerror(title='Error',
                                         message="Please enter the website name.")
        else:
            tkinter.messagebox.showerror(title='Error',
                                         message="Nothing found.")

# Generating a password
def generate_password(pass_len=10):
    letters=string.ascii_letters
    numbers='0123456789'
    special_chars='!$%&()*+,-.:;<=>?@[]^_`{|}~'
    sep=''
    password=sep.join([random.choice(letters+special_chars+numbers) for _ in range(pass_len)])
    entry_password.delete(0, END)
    entry_password.insert(END,string=password)

# Adding a new password
def add_entry():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    entry = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if website == '' or password == '':
        tkinter.messagebox.showerror(title='Error',message="Please don't leave any fields empty!")
    else:
        MsgBox=tkinter.messagebox.askquestion(message=f'{email}\n{password}')
        if MsgBox == 'yes':
            try:
                with open(r'passwords.json','r') as passwords:
                    data=json.load(passwords)
            except FileNotFoundError:
                with open(r'passwords.json', 'w') as passwords:
                    json.dump(entry, passwords, indent=4)
            else:
                data.update(entry)
                with open(r'passwords.json', 'w') as passwords:
                    json.dump(data, passwords, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
        else:
            pass

# Setting up the UI
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=25)

canvas=Canvas(width=200,height=190)
logo=PhotoImage(file='logo.png')
canvas.create_image(100,95,image=logo)
canvas.grid(row=0,column=1,columnspan=1,sticky=W+E)

entry_website=Entry(width=20)
entry_website.grid(row=1,column=1,columnspan=2,sticky=W)

label_website=Label(text="Website: ",font=('ARIAL',12))
label_website.grid(row=1,column=0)

entry_email=Entry(width=45)
entry_email.insert(END,string="user@mail.com")
entry_email.grid(row=2,column=1,columnspan=2,sticky=W)

label_email=Label(text="E-mail/Username: ",font=('ARIAL',12))
label_email.grid(row=2,column=0)

entry_password=Entry(width=20)
entry_password.grid(row=3,column=1,sticky=W)

label_password=Label(text="Password: ",font=('ARIAL',12))
label_password.grid(row=3,column=0)

button_generate=Button(text="Search",width=15,command=search_website)
button_generate.grid(row=1,column=1,columnspan=2,sticky=E)

button_generate=Button(text="Generate Password",width=15,command=generate_password)
button_generate.grid(row=3,column=1,columnspan=2,sticky=E)

button_add=Button(text="Add",width=38,command=add_entry)
button_add.grid(row=4,column=1,columnspan=2,sticky=W)
window.mainloop()