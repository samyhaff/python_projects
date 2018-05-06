from tkinter import *

fenetre = Tk()
champ_label = Label(fenetre, text="Ceci est un test.")
champ_label.pack()
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=50)
ligne_texte.pack()

var_case = IntVar()
case = Checkbutton(fenetre, text="Je suis utile.", variable=var_case)
case.pack()

if var_case.get():
    champ_label = Label(fenetre, text="Effectivement...")
else:
    champ_label = Label(fenetre, text="Non ce n'est pas possible.")

var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

var_choix.get()

bouton_quitter = Button(fenetre, text="Quitter pour regarder du foot...", command=fenetre.quit)
bouton_quitter.pack()



fenetre.mainloop()




