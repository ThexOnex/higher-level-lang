from tkinter import *
import tkinter.messagebox
vraE = "lala@gmail.com"
vraP = "blabla"
times = 0


class Manage:
    times = 0

    def __init__(self) -> None:
        Manage.times += 1

    def blockAcc(self):
        return Manage.times


def vider():
    txt.delete(0, END)
    txt1.delete(0, END)


def quit():
    w.destroy()


def manage():
    # times += 1
    win = Manage()
    if txt.get() != vraE or txt1.get() != vraP:
        if win.blockAcc() >= 3:
            tkinter.messagebox.showinfo("BLOCKED", "ACCOUNT BLOCKED")
            w.quit()
        else:
            tkinter.messagebox.showinfo("Error", "Wrong Email or Password")
    else:
        tkinter.messagebox.showinfo(
            "Welcome", "Loged to the account successfully")


w = Tk()
w.title = "Log in"

email = Label(w, text="Email")
email.pack(padx=5, pady=5)

txt = Entry(w)
txt.pack(padx=5, pady=5)

pswd = Label(w, text="Password")
pswd.pack(padx=5, pady=5)

txt1 = Entry(w, show="*")
txt1.pack(padx=5, pady=5)

btn3 = Button(w, text="Envoyer", command=manage)
btn3.pack(padx=5, pady=5)

btn3 = Button(w, text="Vider", command=vider)
btn3.pack(padx=5, pady=5)

w.mainloop()
