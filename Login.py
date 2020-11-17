import tkinter
from tkinter import *
import PIL
from PIL import ImageTk

def myfunction():
    age = YourAgeBox.get()
    ages = int(age)
    if ages >= 18:
        message = ("Welcome" + " " + YourNameBox.get() + " " + YourSurnameBox.get())

    elif ages < 18:
        message = ("Attention!!!!!" + " " + YourNameBox.get() + " " + YourSurnameBox.get() + " " + "Your are under age to enter")

    MyMessageLabel.config(text=message)

Win = Tk()
Win.title("Login")

#logo

#Namelables and frames
name_frame = Frame(Win)
name_frame.pack(side=TOP)
name_frame.configure(bg="light blue")
YourNameLabel = Label(name_frame, text="Name: ")
YourNameLabel.configure(font="ariel")
YourNameBox = Entry(name_frame)
YourNameBox.configure(width=50, bd=2)

#surname labels and frames
surname_frame = Frame(Win)
surname_frame.pack(side=TOP)
YourSurnameLabel = Label(surname_frame, text="Surname: ")
YourSurnameLabel.configure(font="ariel")
YourSurnameBox = Entry(surname_frame)
YourSurnameBox.configure(width=50, bd=2)

#Cell information labels and frames
contact_frame = Frame(Win)
contact_frame.pack(side=TOP)
CellNoLabel = Label(contact_frame, text="Cellphone No: ")
CellNoLabel.configure(font="ariel")
CellNoBox = Entry(contact_frame)
CellNoBox.configure(width=40, bd=2)

#E-mail label and frame
Email_frame = Frame(Win)
Email_frame.pack(side=TOP)
EmailLabel = Label(Email_frame, text="E-mail: ")
EmailLabel.configure(font="ariel")
EmailBox = Entry(Email_frame)
EmailBox.configure(width=50, bd=2)

#Age Label and frames
age_frame=Frame(Win)
age_frame.pack(side=TOP)
YourAgeLabel = Label(age_frame, text="Age: ")
YourAgeLabel.configure(font="ariel")
YourAgeBox = Entry(age_frame)
YourAgeBox.config(width=10, bd=2)

#check button label and frame
check_frame = Frame(Win)
check_frame.pack(side=TOP)
MyCheckButton = Button(check_frame, text="Login", command=myfunction)
MyCheckButton.config(bd=2, font="bold")

#message box frame
message_frame = Frame(Win)
message_frame.pack(side=TOP)
MyMessageLabel = Label(message_frame, text="Fill out form and press button")


YourNameLabel.pack(side=LEFT)
YourNameBox.pack(side=LEFT)
YourSurnameLabel.pack(side=LEFT)
YourSurnameBox.pack(side=LEFT)
CellNoLabel.pack(side=LEFT)
CellNoBox.pack(side=LEFT)
EmailLabel.pack(side=LEFT)
EmailBox.pack(side=LEFT)
YourAgeLabel.pack(side=LEFT)
YourAgeBox.pack(side=LEFT)
MyCheckButton.pack(side=LEFT)
MyMessageLabel.pack(side=LEFT)




Win.mainloop()
