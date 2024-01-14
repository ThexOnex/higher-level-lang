from tkinter import *
from window2 import Fentre2
import tkinter.messagebox


def deplace():
    f.destroy()
    f1 = Fentre2()
    f1.afficher()


def vider():
    txt.delete(0, END)
    txt1.delete(0, END)
    txt2.delete(0, END)


def Calculer():
    if txt.get() == "" or txt1.get() == "" or not txt.get().isdigit() or not txt1.get().isdigit():
        tkinter.messagebox.showinfo("Information", "il y a des champs vide")
    x = int(txt.get())
    y = int(txt1.get())
    if ITM.get() == '+':
        s = x + y
    if ITM.get() == '-':
        s = x - y
    if ITM.get() == '*':
        s = x * y
    if ITM.get() == '/':
        s = x / y
    txt2.insert(0, str(s))


f = Tk()
f.title = "Fentre 1"
f.resizable(width=False, height=False)

N = Label(f, text="Taper une valeur: ")
N.pack(padx=5, pady=5)  # manipulates dimentions

txt = Entry(f)
txt.pack(padx=5, pady=5)

N1 = Label(f, text="Taper une valeur: ")
N1.pack(padx=5, pady=5)

txt1 = Entry(f)
txt1.pack(padx=5, pady=5)

N2 = Label(f, text="resultat: ")
N2.pack(padx=5, pady=5)
txt2 = Entry(f)
txt2.pack(padx=5, pady=5)

btn = Button(f, text="Calcule", command=Calculer)
btn.pack(padx=5, pady=5, side=LEFT)

btn2 = Button(f, text="vider", command=vider)
btn2.pack(padx=5, pady=5, side=LEFT)

btn3 = Button(f, text="Quitter", command=f.destroy)
btn3.pack(padx=5, pady=5)

btn4 = Button(f, text="Fenetre 2", command=deplace)
btn4.pack(padx=5, pady=5)
op = ['*', '+', '-', '/']
ITM = StringVar()
cb = OptionMenu(f, ITM, *op)
cb.pack(padx=5, pady=5)

f.mainloop()
