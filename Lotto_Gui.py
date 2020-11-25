import tkinter
from tkinter import messagebox
from tkinter import *
import ImageTk, PIL, Image, os
from random import sample
import datetime
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
heading = Label(Lotto, text="Ithuba National Lottery")
heading.configure(font=("Courier", 16, "bold"))
heading.place(x=110, y=105)


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


e1 = Entry(Lotto)
e1.configure(bd=2, width=4)
e1.place(x=145, y=250)
e2 = Entry(Lotto)
e2.configure(bd=2, width=4)
e2.place(x=180, y=250)
e3 = Entry(Lotto)
e3.configure(bd=2, width=4)
e3.place(x=215, y=250)
e4 = Entry(Lotto)
e4.configure(bd=2, width=4)
e4.place(x=250, y=250)
e5 = Entry(Lotto)
e5.configure(bd=2, width=4)
e5.place(x=285, y=250)
e6 = Entry(Lotto)
e6.configure(bd=2, width=4)
e6.place(x=320, y=250)


def lotto_list():
    num1 = int(e1.get())
    num2 = int(e2.get())
    num3 = int(e3.get())
    num4 = int(e4.get())
    num5 = int(e5.get())
    num6 = int(e6.get())
    list_1 = num1, num2, num3, num4, num5, num6
    return list_1


#button
game = Button(Lotto, text="Generate Numbers")
game.configure()
game.place(x=10, y=450)
resetbtn = Button(Lotto, text="Reset")
resetbtn.place(x=450, y=450)


#heading for random numbers
head = Label(Lotto, text="Lotto numbers are")
head.configure(font=("Courier", 10, "bold"))
head.place(x=175, y=300)



#Display lables
ran_labl1 = Label(Lotto, width=4, bg="yellow")
ran_labl1.place(x=145, y=340)
ran_labl2 = Label(Lotto, width=4, bg="yellow")
ran_labl2.place(x=180, y=340)
ran_labl3 = Label(Lotto, width=4, bg="yellow")
ran_labl3.place(x=215, y=340)
ran_labl4 = Label(Lotto, width=4, bg="yellow")
ran_labl4.place(x=250, y=340)
ran_labl5 = Label(Lotto, width=4, bg="yellow")
ran_labl5.place(x=285, y=340)
ran_labl6 = Label(Lotto, width=4, bg="yellow")
ran_labl6.place(x=320, y=340)



def go():
    picks = sample(range(1, 49), 7)
    picks.sort()
    ran_labl6.configure(text=picks[5])
    ran_labl1.configure(text=picks[0], bg="white")
    ran_labl2.configure(text=picks[1], bg="white")
    ran_labl3.configure(text=picks[2], bg="white")
    ran_labl4.configure(text=picks[3], bg="white")
    ran_labl5.configure(text=picks[4], bg="white")
    ran_labl6.configure(text=picks[5], bg="red")
    game.configure(state=DISABLED)
    resetbtn.configure(state=NORMAL)


    count = 0
    for number in lotto_list():
        if number in picks:
            count += 1
    if count <= 1:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R0" )

    elif count == 2:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R20" )
    elif count == 3:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R100.50" )
    elif count == 4:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R2,384.00" )
    elif count == 5:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R8,584.00" )
    elif count == 6:
        message = "Attention"
        messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R10, 000 000.00" )
    return picks



now = datetime.datetime.now()


def append():
    # appending text
    f = open("Login.txt", "a+")
    f.write("Lotto Numbers are: " + str(go()) + " " + "User Numbers: " +
            str(lotto_list()) + " " + "Numbers Guessed right: " + " " + "Time: " + str(now))
    f.close()

def reset():
    ran_labl1.configure(text='', bg="Yellow")
    ran_labl2.configure(text='', bg="Yellow")
    ran_labl3.configure(text='', bg="Yellow")
    ran_labl4.configure(text='', bg="Yellow")
    ran_labl5.configure(text='', bg="Yellow")
    ran_labl6.configure(text='', bg="yellow")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    game.configure(state=NORMAL)
    resetbtn.configure(state=DISABLED)

game.configure(command=append)
resetbtn.configure(command = reset)

Lotto.configure(bg="Yellow")
Lotto.geometry('500x500')
Lotto.mainloop()