import tkinter
from tkinter import messagebox
from tkinter import *
import ImageTk, PIL, Image, os
from random import sample
import random


Lotto = Tk()
Lotto.title("Lotto")
Lotto.iconbitmap("images/nlc-logo-1.ico")

#LOGO of lotto plus
img = Image.open("images/south-african-lotto.jpg")
img = img.resize((500, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(Lotto, image=img)
panel.image = img
panel.place(x=0, y=0)


#heading frame
heading = Label(Lotto, text="National Lottery App")
heading.configure(font=("Courier", 16, "bold"))
heading.place(x=120, y=105)


#rules
l1 = Label(Lotto, text="Intructions", bg="yellow")
l1.place(x=0, y=130)
l2 = Label(Lotto, text="The rules are as follows:", bg="yellow")
l2.place(x=0, y=150)
l3 = Label(Lotto, text="1. Select only 6 numbers", bg="yellow")
l3.place(x=0, y=170)
l4 = Label(Lotto, text="2. Only choose numbers from 1 - 49", bg="yellow")
l4.place(x=0, y=190)


#Begin
lbl1 = Label(Lotto, text="Please insert your numbers")
lbl1.configure(font=("Courier", 10, "bold"))
lbl1.place(x=140, y=220)


userNUmbers = []
for i in range(0, 6):
    number = Entry(Lotto)
    number.grid(row=0, column=i, pady=250, padx=5)
    number.configure(width=5)
    userNUmbers.append(number)


#button
b1 = Button(Lotto, text="Generate Numbers")
b1.configure()
b1.place(x=10, y=450)
resetBtn = Button(Lotto, text="Reset")
resetBtn.place(x=450, y=450)


#heading for random numbers
head = Label(Lotto, text="Lotto numbers are")
head.configure(font=("Courier", 10, "bold"))
head.place(x=175, y=300)



#Display lables
display_lbl = Label(Lotto)
display_lbl.place(x=155, y=330)


def pick():
    for i in range(6):
        Lott_list = [random.randint(1, 49) for _ in range(6)]
        display_lbl.configure(text=str(Lott_list), font=("Courier", 10, "bold"))



b1.configure(command=pick)
resetBtn.configure()

Lotto.configure(bg="Yellow")
Lotto.geometry('500x500')
Lotto.mainloop()


