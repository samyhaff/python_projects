from Fonctions import*


#Initialisation

try:
    with open("Dictionnaire", 'rb') as FichierDico:
        DicoDepickler = pickle.Unpickler(FichierDico)
        Dico = DicoDepickler.load()
except:
    with open("Dictionnaire", 'wb') as FichierDico:
        Dico=["je"]
        DicoPickler = pickle.Pickler(FichierDico)
        DicoPickler.dump(Dico)
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
        if TesterClassement(Mot,Dico):
            Dico=Classer(Mot,Dico)
        NouveauMot=False        
                   
FichierTexte.close()

#Rangement

DicoChaine=" ".join(Dico)
with open("Dictionnaire.txt", 'w', encoding="utf-8") as FichierDicotxt:
     FichierDicotxt.write(DicoChaine)

with open("Dictionnaire", 'wb') as FichierDico:
    DicoPickler = pickle.Pickler(FichierDico)
    DicoPickler.dump(Dico)
