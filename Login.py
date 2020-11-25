import tkinter
from tkinter import *
import PIL
from PIL import ImageTk
import ImageTk, PIL, Image, os
from datetime import *
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox

now = datetime.datetime.now()

def calculate_age():
    #appending text
    f = open("Login.txt", "a+")
    f.write(name_ent.get() + " " + surname_ent.get() + " " + birth_year_entry.get() + " " +
            birth_month_entry.get() + " " + birth_day_entry.get() +" " + "Logged on at: " + str(now))
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
    else:
        message = "Declined"
        messagebox.showerror(message, "Denied" + "Under 18")
        return age


Login = Tk()
Login.title("Login")
Login.iconbitmap("images/nlc-logo-1.ico")

#big image
img = Image.open("images/images.jpg")
img = img.resize((500, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(Login, image=img)
panel.image = img
panel.place(x=0, y=0)

#small image
img = Image.open("images/18new.png")
img = img.resize((50, 50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(Login, image=img)
panel.image = img
panel.place(x=440, y=440)


#Heading
head = Label(Login, text="Login forum")
head.configure(font=("Courier", 16, "bold"), bg="#fdcb08")
head.place(x=180, y=105)


#info frame
name = Label(Login, text="Name: ")
name.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
name.place(x=60, y=150)
name_ent = Entry(Login)
name_ent.configure(width=40)
name_ent.place(x=150, y=150)
surname = Label(Login, text="Surname: ")
surname.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
surname.place(x=30, y=200)
surname_ent = Entry(Login)
surname_ent.configure(width=40)
surname_ent.place(x=150, y=200)


#DOB
dob = Label(Login, text="Date Of Birth")
dob.configure(font=("Courier", 13, "bold"), bg="#fdcb08")
dob.place(x=180, y=250)

birth_year = Label(Login, text="yyyy", font=("Helvetica", 10))
birth_month = Label(Login, text="mm", font=("Helvetica", 10))
birth_day = Label(Login, text="dd", font=("Helvetica", 10))

birth_day.configure(bg="#fdcb08")
birth_month.configure(bg="#fdcb08")
birth_year.configure(bg="#fdcb08")

birth_year.place(x=187, y=300)
birth_month.place(x=239, y=300)
birth_day.place(x=293, y=300)

birth_year_entry = Entry(Login, width=5)
birth_year_entry.place(x=187, y=280)
# / lable
stroke1 = Label(Login, text="/")
stroke1.configure(font=("Courier", 10, "bold"), bg="#fdcb08")
stroke1.place(x=221, y=280)
stroke2 = Label(Login, text="/")
stroke2.configure(font=("Courier", 10, "bold"), bg="#fdcb08")
stroke2.place(x=273, y=280)

birth_month_entry = Entry(Login, width=5)
birth_month_entry.place(x=237, y=280)

birth_day_entry = Entry(Login, width=5)
birth_day_entry.place(x=287, y=280)



#Buttons
login_btn = Button(Login, text="Login", command=calculate_age)
login_btn.configure(bd=2)
login_btn.place(x=190, y=330)
quit_btn = Button(Login, text="Quit")
quit_btn.configure(bd=2)
quit_btn.place(x=260, y=330)

#User agreement
agree = Label(Login, text="User agreement")
agree.configure(font=("Courier", 10, "bold"), bg="#fdcb08")
agree.place(x=0, y=402)
#agreement laws
agree1 = Label(Login, text="1. Must be 18 or older to enter.\n2. User must have a vaild ID.\n3. User must be a SA citizen.")
agree1.configure(bg="#fdcb08")
agree1.place(x=0, y=420)

Login.config(bg="#fdcb08")
Login.geometry('500x500')
Login.mainloop()
