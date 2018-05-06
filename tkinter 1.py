"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

fenetre = Tk()
champ_label = Label(fenetre, text="Quittes la fenetre")
champ_label.pack()
fenetre.mainloop()


for a in range(1,10): 
    fenetre = Tk()
    champ_label = Label(fenetre, text="Essai encore!")
    champ_label.pack()
    fenetre.mainloop()


