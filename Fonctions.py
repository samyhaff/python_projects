from bs4 import BeautifulSoup
import requests
import re
import math
import random
import numpy
import pickle
import selenium.webdriver as webdriver

#Listes d'Alphabet

Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
AlphaBP=["a","à","æ","b","c","ç","d","e","é","è","ê","ë","f","g","h","i","î","ï","j","k","l","m","n","o","ô","œ","p","q","r","s","t","u","ù","û","ü","v","w","x","y","ÿ","z"]

Consonnes=["b","c","ç","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","ÿ","z"]
Voyelles=["a","à","æ","e","é","è","ê","ë","i","î","ï","o","ô","œ","u","ù","û","ü"]
VoyellesGroupées=[["a","à","æ"],["e","œ"],["é"],["è","ê","ë"],["i","î","ï","y"],["o","ô"],["u","ù","û","ü"]]

PronomsPersonnelsGroupés=[["je"],["tu"],["il,elle,on"],["nous"],["vous"],["ils,elles"]]
PronomsPersonnelsPrincipaux=["je","tu","il","nous","vous","ils"]
PronomsPersonnels=["je","tu","il","elle","on","nous","vous","ils","elles"]

CombinaisonsVoyelles=[["on"],["ou","oo"],["ai","ay","ei","ey"]]

#Fonctions

def Numérer(Mot):
    Valeur=float(0)
    for j in range(0,len(Mot)):
        Valeur=AlphaBP.index(Mot[j])/len(AlphaBP)**(j+1)+Valeur
    return Valeur

def TesterClassement(Mot,Liste):
    Valeur=True
    for k in Liste:
        if Mot==k:
            Valeur=False
    return Valeur

def Classer(Mot,Liste):
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

def Voisinage(NuméroLettre,Mot):
    Voisins=[]
    Nl=NuméroLettre
    if Nl>0:
        Voisins.append(Mot[Nl-1])
    if Nl<len(Mot)-1:
        Voisins.append(Mot[Nl+1])
    return Voisins

def Syllables(Mot):
    Syllables=0
    NouvelleVoyelle=False
    n=0
    for Lettre in Mot:
        AncienneVoyelle=NouvelleVoyelle
        NouvelleVoyelle=False
        for Voyelle in Voyelles:
            if Lettre==Voyelle:
                NouvelleVoyelle=True
        if Lettre=="y":
            VoyelleSyllable=0
            for Voisin in Voisinage(n,Mot):
                for VoyelleY in Voyelles:
                    if Voisin==VoyelleY:
                        VoyelleSyllable=VoyelleSyllable+1
            if VoyelleSyllable==0:
                Syllables=Syllables+1
        if NouvelleVoyelle==True and AncienneVoyelle==False:
            Syllables=Syllables+1
        n=n+1
    return Syllables

def CompterCaractères(Eléments,Séquence):
    Nombre=0
    for i in range(0,len(CSéquence)-len(Eléments)+1):
        if Chaine[i:i+len(Eléments)]==Eléments:
                  Nombre=Nombre+1
    return Nombre

def Associer(Liste,Tuple):
    Séquence=[]
    for Elément in Liste:
        for i in range(0,len(Tuple)):
            for j in range(0,len(Tuple[i])):
                if Tuple[i][j]==Elément:
                       Séquence.append(i)
    return Séquence

def Réduire(Entrée):
    Sortie=[Entrée[0]]
    for i in range(0,len(Entrée)-1):
        if Entrée[i]!=Entrée[i+1]:
            Sortie.append(Entrée[i+1])
    return Sortie

def Rechercher(search, Nombre=1):
    url = "https://www.startpage.com"
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver")
    browser.get(url)
    search_box=browser.find_element_by_id("query")
    search_box.send_keys(search)
    search_box.submit()
    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
        links = browser.find_elements_by_xpath("//h3//a")
    Urls = []
    for link in links:
        href = link.get_attribute("href")
        Urls.append(href)
    browser.close()
    return Urls

def StockerUnSite(Url,FichierTexte,Mode):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        file = open(FichierTexte+".txt", Mode)
        file.write(str(y))
        file.close()
    except:
        print("Le site suivant n'a pas pu être récupéré:")
        print(Url)
        print("")

def RécupérerUnSite(Url):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        return y
    except:
        print("Le site suivant n'a pas pu être récupéré:")
        print(Url)
        print("")

def Soustraire(Dictionnaire1,Dictionnaire2,NouveauDico):
    NouveauDico=[]
    for Mot in Dictionnaire2:
        if Dictionnaire1.count(Mot)==0:
            NouveauDico.append(Mot)
    return NouveauDico

def ConvertirTexteEnTuple(DicoTexte,DicoTuple,Mode):
    try:
        with open(DicoTexte+".txt", 'r', encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.read()
             Dico=ChaineDicoTexte.split(" ")
        try:
            with open(DicoTuple, Mode+'b') as FichierDicoTuple:
                DicoTuplePickler = pickle.Pickler(FichierDicoTuple)
                DicoTuplePickler.dump(Dico)
        except:
            print("Ecriture impossible.")
    except:
        print("Lecture impossible.")

def ConvertirTupleEnTexte(DicoTuple,DicoTexte,Mode):
    try:
        with open(DicoTuple, 'rb') as FichierDicoTuple:
            DicoTupleDepickler = pickle.Unpickler(FichierDicoTuple)
            DicoTuple = DicoTupleDepickler.load()
            Dico=" ".join(DicoTuple)
        try:
            with open(DicoTexte+".txt", Mode, encoding="utf-8") as FichierDicoTexte:
                 ChaineDicoTexte=FichierDicoTexte.write(Dico)
        except:
            print("Ecriture impossible.")
    except:
        print("Lecture impossible.")

def StockerTuple(Tuple,NomFichierTuple,Mode):
    try:
        with open(NomFichierTuple, Mode+'b') as FichierTuple:
                FichierTuplePickler = pickle.Pickler(FichierTuple)
                FichierTuplePickler.dump(Tuple)
    except:
        print("Stockage en Tuple impossible.")

def SortirTuple(NomFichierTuple):
    try:
        with open(NomFichierTuple, 'rb') as FichierTuple:
                FichierTupleDepickler = pickle.Unpickler(FichierTuple)
                return DicoDepickler.load()
    except:
        print("Stockage en Tuple impossible.")
    

def GénérerUnDictionnaire(Fichier,Dictionnaire):
    try:
        with open(Dictionnaire, 'rb') as FichierDico:
            DicoDepickler = pickle.Unpickler(FichierDico)
            Dico = DicoDepickler.load()
    except:
        with open(Dictionnaire, 'wb') as FichierDico:
            Dico=["je"]
            DicoPickler = pickle.Pickler(FichierDico)
            DicoPickler.dump(Dico)
        with open(Dictionnaire, 'rb') as FichierDico:
            DicoDepickler = pickle.Unpickler(FichierDico)
            Dico = DicoDepickler.load()
    FichierTexte = open(Fichier+".txt", "r",encoding="utf-8")
    Texte=FichierTexte.read()
    TexteMn=Texte.lower()
    LettreNew=False
    NouveauMot=False
    m=0
    Dico=[]
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
    DicoChaine=" ".join(Dico)
    with open(Dictionnaire+".txt", 'w', encoding="utf-8") as FichierDicotxt:
         FichierDicotxt.write(DicoChaine)
    with open(Dictionnaire, 'wb') as FichierDico:
        DicoPickler = pickle.Pickler(FichierDico)
        DicoPickler.dump(Dico)
