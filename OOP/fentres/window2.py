from tkinter import *


class Fentre2:
    def afficher(self):
        f2 = Tk()
        f2.title = "fenetre 2"
        l = Label(f2, text="vous etes dans la 2eme fenetre")
        l.pack(padx=100, pady=20)

        btn3 = Button(f2, text="Quitter", command=f2.destroy)
        btn3.pack(padx=5, pady=5)
        f2.mainloop()


fen = Fentre2()
fen.afficher()
