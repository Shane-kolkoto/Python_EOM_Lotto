import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import *
from tkcalendar import DateEntry
from random import sample


def game_time():
    Lotto = Tk()
    Lotto.title("Lotto")

    # heading frame
    heading = Label(Lotto, text="Ithuba National Lottery")
    heading.configure(font=("Courier", 16, "bold"), bg="yellow")
    heading.place(x=95, y=0)

    # rules
    l1 = Label(Lotto, text="Intructions", bg="yellow")
    l1.place(x=225, y=30)
    l2 = Label(Lotto, text="The rules are as follows:", bg="yellow")
    l2.place(x=190, y=50)
    l3 = Label(Lotto, text="1. Select only 6 numbers", bg="yellow")
    l3.place(x=190, y=70)
    l4 = Label(Lotto, text="2. Only choose numbers from 1 - 49", bg="yellow")
    l4.place(x=160, y=90)

    # Begin
    lbl1 = Label(Lotto, text="Please insert your numbers")
    lbl1.configure(font=("Courier", 10, "bold"))
    lbl1.place(x=145, y=120)

    e1 = Entry(Lotto)
    e1.configure(bd=2, width=4)
    e1.place(x=145, y=150)
    e2 = Entry(Lotto)
    e2.configure(bd=2, width=4)
    e2.place(x=180, y=150)
    e3 = Entry(Lotto)
    e3.configure(bd=2, width=4)
    e3.place(x=215, y=150)
    e4 = Entry(Lotto)
    e4.configure(bd=2, width=4)
    e4.place(x=250, y=150)
    e5 = Entry(Lotto)
    e5.configure(bd=2, width=4)
    e5.place(x=285, y=150)
    e6 = Entry(Lotto)
    e6.configure(bd=2, width=4)
    e6.place(x=320, y=150)

    def lotto_list():
        num1 = int(e1.get())
        num2 = int(e2.get())
        num3 = int(e3.get())
        num4 = int(e4.get())
        num5 = int(e5.get())
        num6 = int(e6.get())
        list_1 = num1, num2, num3, num4, num5, num6
        return list_1

    # heading for random numbers
    head = Label(Lotto, text="Lotto numbers are")
    head.configure(font=("Courier", 10, "bold"))
    head.place(x=175, y=180)

    # Display lables
    ran_labl1 = Label(Lotto, width=4, bg="yellow")
    ran_labl1.place(x=145, y=210)
    ran_labl2 = Label(Lotto, width=4, bg="yellow")
    ran_labl2.place(x=180, y=210)
    ran_labl3 = Label(Lotto, width=4, bg="yellow")
    ran_labl3.place(x=215, y=210)
    ran_labl4 = Label(Lotto, width=4, bg="yellow")
    ran_labl4.place(x=250, y=210)
    ran_labl5 = Label(Lotto, width=4, bg="yellow")
    ran_labl5.place(x=285, y=210)
    ran_labl6 = Label(Lotto, width=4, bg="yellow")
    ran_labl6.place(x=320, y=210)

    def draw():
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
        resetbtn2.configure(state=NORMAL)

        count = 0
        for number in lotto_list():
            if number in picks:
                count += 1
        if count <= 1:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R0")
        elif count == 2:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R20")
        elif count == 3:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R100.50")
        elif count == 4:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R2,384.00")
        elif count == 5:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R8,584.00")
        elif count == 6:
            message = "Attention"
            messagebox.showerror(message, str(count) + " " + "Numbers" + "\n payout = R10, 000 000.00")
        return picks

    now = datetime.datetime.now()

    def append():
        # appending text
        f = open("Lotto.txt", "a+")
        f.write("Lotto Numbers are: " + str(draw()) + " " + "User Numbers: " +
                str(lotto_list()) + " " + "Numbers Guessed right: " + " " + "Time: " + str(now) + "\n")
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
        resetbtn2.configure(state=DISABLED)

    # button
    game = Button(Lotto, text="Generate Numbers")
    game.configure()
    game.place(x=10, y=250)
    resetbtn2 = Button(Lotto, text="Reset")
    resetbtn2.place(x=450, y=250)
    game.configure(command=append)
    resetbtn2.configure(command=reset)

    Lotto.configure(bg="Yellow")
    Lotto.geometry('500x300')
    Lotto.mainloop()


import datetime
#Login Functions
now = datetime.datetime.now()


def calculate_age():
    #appending text
    f = open("Lotto.txt", "a+")
    f.write(name_ent.get() + " " + surname_ent.get() + " " + "DOB:" + birth_year_entry.get() + " " +
            birth_month_entry.get() + " " + birth_day_entry.get() +" " + "Logged on at: " + str(now) + "\n")
    f.close()


    #date of birth
    b_year = int(birth_year_entry.get())
    b_month = int(birth_month_entry.get())
    b_day = int(birth_day_entry.get())
    b_date = datetime.date(b_year, b_month, b_day)
    today = datetime.date.today()


    #age calculate
    age = today.year - b_date.year
    if age > 18:
        message = "Welcome"
        messagebox.showinfo(message, "Logged in")
        Login.destroy()
        game_time()

    else:
        message = "Declined"
        messagebox.showerror(message, "Denied" + " " + "Under Age")
        return age

def quit():
    Login.destroy()


#Login gui
Login = Tk()
Login.title("Login")

#Heading
head = Label(Login, text="Login forum")
head.configure(font=("Courier", 16, "bold"), bg="#fdcb08")
head.place(x=180, y=0)


#info frame
name = Label(Login, text="Name: ")
name.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
name.place(x=60, y=50)
name_ent = Entry(Login)
name_ent.configure(width=40)
name_ent.place(x=150, y=50)
surname = Label(Login, text="Surname: ")
surname.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
surname.place(x=30, y=90)
surname_ent = Entry(Login)
surname_ent.configure(width=40)
surname_ent.place(x=150, y=90)


#DOB
dob = Label(Login, text="Date Of Birth")
dob.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
dob.place(x=180, y=120)

birth_year = Label(Login, text="yyyy", font=("Helvetica", 10))
birth_month = Label(Login, text="mm", font=("Helvetica", 10))
birth_day = Label(Login, text="dd", font=("Helvetica", 10))

birth_day.configure(bg="#fdcb08")
birth_month.configure(bg="#fdcb08")
birth_year.configure(bg="#fdcb08")

birth_year.place(x=187, y=170)
birth_month.place(x=239, y=170)
birth_day.place(x=293, y=170)

birth_year_entry = Entry(Login, width=5)
birth_year_entry.place(x=187, y=150)

# / lable
stroke1 = Label(Login, text="/")
stroke1.configure(font=("Courier", 10, "bold"), bg="#fdcb08")
stroke1.place(x=221, y=150)
stroke2 = Label(Login, text="/")
stroke2.configure(font=("Courier", 10, "bold"), bg="#fdcb08")
stroke2.place(x=273, y=150)

birth_month_entry = Entry(Login, width=5)
birth_month_entry.place(x=237, y=150)

birth_day_entry = Entry(Login, width=5)
birth_day_entry.place(x=287, y=150)

#Buttons
login_btn = Button(Login, text="Login", command=calculate_age)
login_btn.configure(bd=2)
login_btn.place(x=190, y=200)
quit_btn = Button(Login, text="Quit")
quit_btn.configure(bd=2, command=quit)
quit_btn.place(x=260, y=200)


Login.config(bg="#fdcb08")
Login.geometry('500x250')
Login.mainloop()
