import math
import numpy

#Listes d'Alphabet

Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ABP=["a","à","æ""b","c","ç","d","e","é","è","ê","ë","f","g","h","i","î","ï","j","k","l","m","n","o","ô","œ","p","q","r","s","t","u","ù","û","ü","v","w","x","y","ÿ","z"]

#Ouverture de Fichiers

FichierTexte = open("Mme Bovary 2.txt", "r")
Texte=FichierTexte.read()
TexteMn=Texte.lower()

#Boucle Principale

LettreNew=False
m=0
for i in range(0,len(TexteMn)):
    LettreOld=LettreNew
    for Lettre in ABP:
        if TexteMn[i]==Lettre
            LettreNew=True
        else:
            LettreNew=False
    if LettreNew=True and LettreOld=False:
        MotD=i
    if LettreNew=False and LettreOld=True:
        MotF=i
        Mot=TexteMn[MotD:MotF]
        if 
        









        
        
        
        
    

            Dico.append(Message[m:i])
        m=i+1
Mots.close()
