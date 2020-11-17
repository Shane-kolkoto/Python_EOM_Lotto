from tkinter import *
from turtle import *
from random import sample, seed


win = Tk()
win.title("Lotto Number Generator")

#Welcome frame

Labl1 = Label(win, width=2)
Labl2 = Label(win, width=2)
Labl3 = Label(win, width=2)
Labl4 = Label(win, width=2)
Labl5 = Label(win, width=2)
Labl6 = Label(win, width=2)

ResetBtn = Button(win, text="Reset")
PickBtn = Button(win, text="Pick My Lucky Numbers")

Labl1.grid(row=1, column=1, padx=10)
Labl2.grid(row=1, column=2, padx=10)
Labl3.grid(row=1, column=3, padx=10)
Labl4.grid(row=1, column=4, padx=10)
Labl5.grid(row=1, column=5, padx=10)
Labl6.grid(row=1, column=6, padx=10)

ResetBtn.grid(row=2, column=6, columnspan=2)
PickBtn.grid(row=2, column=1, columnspan=5)


def reset():
    Labl1.configure(text='...')
    Labl2.configure(text='...')
    Labl3.configure(text='...')
    Labl4.configure(text='...')
    Labl5.configure(text='...')
    Labl6.configure(text='...', bg="yellow")
    PickBtn.configure(state=NORMAL)
    ResetBtn.configure(state=DISABLED)


def pick():
    picks = sample(range(1, 49), 7)
    Labl6.configure(text=picks[5])
    del picks[6]
    picks.sort()
    Labl1.configure(text=picks[0])
    Labl2.configure(text=picks[1])
    Labl3.configure(text=picks[2])
    Labl4.configure(text=picks[3])
    Labl5.configure(text=picks[4])
    Labl6.configure(text=picks[5])
    PickBtn.configure(state=DISABLED)
    ResetBtn.configure(state=NORMAL)


ResetBtn.configure(command=reset)
PickBtn.configure(command=pick)

reset()
win.geometry("250x60")
win.mainloop()