import math
import numpy
import pickle

#Listes d'Alphabet

Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
AlphaBP=["a","à","æ","b","c","ç","d","e","é","è","ê","ë","f","g","h","i","î","ï","j","k","l","m","n","o","ô","œ","p","q","r","s","t","u","ù","û","ü","v","w","x","y","ÿ","z"]

#Fonctions

def Numérer(Mot):
    Valeur=float(0)
    for j in range(0,len(Mot)):
        Valeur=AlphaBP.index(Mot[j])/len(AlphaBP)**(j+1)+Valeur
    return Valeur

def Classer(Mot):

     truc=0

def TesterAjout(Mot,Liste):
    Valeur=True
    for k in Liste:
        if Mot==k:
            Valeur=False
    return Valeur

def Ajouter(Mot,Liste):
    MV=Numérer(Mot)
    l=0
    Recherche=True
    while Recherche:
        if l<len(Liste):
            if Numérer(Liste[l])>MV:
                Recherche=False
            else:
                l=l+1
        else:
            Recherche=False
    if l<len(Liste):
        if Numérer(Liste[l])>MV:
            Sortie=Liste[0:l]
            Sortie.append(Mot)
            Sortie.extend(Liste[l:len(Liste)])
            Liste=Sortie[:]
    else:
        Liste.append(Mot)
    return Liste
        
        

#Initialisation
        
#with open("Dictionnaire", 'wb') as FichierDico:
#    Dico=["je"]
#    DicoPickler = pickle.Pickler(FichierDico)
#    DicoPickler.dump(Dico)


with open("Dictionnaire", 'rb') as FichierDico:
    DicoDepickler = pickle.Unpickler(FichierDico)
    Dico = DicoDepickler.load()
    

#Ouverture de Fichiers

FichierTexte = open("Mme Bovary.txt", "r",encoding="utf-8")
Texte=FichierTexte.read()
TexteMn=Texte.lower()

#Boucle Principale

LettreNew=False
NouveauMot=False
m=0

for i in range(0,len(TexteMn)):
    LettreOld=LettreNew
    LettreNew=False
    for Lettre in AlphaBP:
        if TexteMn[i]==Lettre:
            LettreNew=True
    if LettreNew==True and LettreOld==False:
        MotD=i
    if LettreNew==False and LettreOld==True:
        MotF=i
        NouveauMot=True
    if NouveauMot==True:
        Mot=TexteMn[MotD:MotF]
        if TesterAjout(Mot,Dico):
            Dico=Ajouter(Mot,Dico)
        NouveauMot=False        
                   
FichierTexte.close()

#Rangement

DicoChaine=" ".join(Dico)
with open("Dictionnaire.txt", 'w', encoding="utf-8") as FichierDicotxt:
     FichierDicotxt.write(DicoChaine)

with open("Dictionnaire", 'wb') as FichierDico:
    DicoPickler = pickle.Pickler(FichierDico)
    DicoPickler.dump(Dico)
