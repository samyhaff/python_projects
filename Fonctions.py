from bs4 import BeautifulSoup
import requests
import re
import math
import random
import numpy
import pickle
import selenium.webdriver as webdriver

#Listes d'Alphabet
Alphabet="abcdefghijklmnopqrstuvwxyz"
Minuscules="abcdefghijklmnopqrstuvwxyz"
Majuscules="ABCDEGHIJKLMNOPQRSTUVWXYZ"
AlphabetCompletMinuscules="aàæbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿz"
AlphabetCompletMajuscules="AÀÆBCÇDEÉÈÊËFGHIÎÏJKLMNOÔŒPQRSTUÙÛÜVWXYŸZ"
AlphabetTrèsComplet="aàæbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿzAÀÆBCÇDEÉÈÊËFGHIÎÏJKLMNOÔŒPQRSTUÙÛÜVWXYŸZ"
Fin=".!?"
Ponctuation=",.;!?':()-"
CaractèresSpéciaux="#@&°_¨^+-=*$¥€£`%§/:;?!.,<>()"
Nombres="0123456789"


Consonnes=["b","c","ç","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","ÿ","z"]
Voyelles=["a","à","æ","e","é","è","ê","ë","i","î","ï","o","ô","œ","u","ù","û","ü"]
VoyellesGroupées=[["a","à","æ"],["e","œ"],["é"],["è","ê","ë"],["i","î","ï","y"],["o","ô"],["u","ù","û","ü"]]

PronomsPersonnelsGroupés=[["je"],["tu"],["il,elle,on"],["nous"],["vous"],["ils,elles"]]
PronomsPersonnelsPrincipaux=["je","tu","il","nous","vous","ils"]
PronomsPersonnels=["je","tu","il","elle","on","nous","vous","ils","elles"]

CombinaisonsVoyelles=[["on"],["ou","oo"],["ai","ay","ei","ey"]]

#Fonctions

AfficherErreur=False
Erreurs=[]


def Erreur(Fonction):
    global AfficherErreur,Erreurs
    if AfficherErreur:
        print("La fonction",Fonction,"n'a pas pue être exécutée.")
    Erreurs.append(Fonction)

def Numerer(Mot):
    try:
        Mot=Mot.lower()
        Valeur=float(0)
        for j in range(0,len(Mot)):
            Valeur=AlphabetComplet.index(Mot[j])/len(AlphabetComplet)**(j+1)+Valeur
        return Valeur
    except:
        Erreur("Numerer")

def Classer(Mot,Liste):
    try:
        MV=Numerer(Mot)
        l=0
        Recherche=True
        while Recherche:
            if l<len(Liste):
                if Numerer(Liste[l])>MV:
                    Recherche=False
                else:
                    l=l+1
            else:
                Recherche=False
        if l<len(Liste):
            if Numerer(Liste[l])>MV:
                Sortie=Liste[0:l]
                Sortie.append(Mot)
                Sortie.extend(Liste[l:len(Liste)])
                Liste=Sortie[:]
        else:
            Liste.append(Mot)
        return Liste
    except:
        Erreur("Classer")

def Voisinage(NuméroLettre,Mot):
    try:
        Voisins=[]
        Nl=NuméroLettre
        if Nl>0:
            Voisins.append(Mot[Nl-1])
        if Nl<len(Mot)-1:
            Voisins.append(Mot[Nl+1])
        return Voyelles
    except:
        Erreur("Voisinage")

def CompterSyllables(Mot):
    try:
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
    except:
        Erreur("CompterSyllables")

def Associer(Liste,Tuple):
    try:
        Sequence=[]
        for Element in Liste:
            for i in range(0,len(Tuple)):
                if Tuple[i].count(Element)==1:
                    Sequence.append(i)
        return Sequence
    except:
        Erreur("Associer")

def Reduire(Entree):
    try:
        Sortie=[Entree[0]]
        for i in range(0,len(Entree)-1):
            if Entree[i]!=Entree[i+1]:
                Sortie.append(Entree[i+1])
        return Sortie
    except:
        Erreur("Reduire")

def RechercherUrl(search):
    try:
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
    except:
        Erreur("RechercherUrl")

def StockerSite(Url,FichierTexte,Mode):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        liste=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(liste)
        print(y)
        file = open(FichierTexte+".txt", Mode)
        file.write(str(y))
        file.close()
    except:
        Erreur("StockerSite")

def RécupérerSite(Url):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        liste=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(liste)
        return y
    except:
        Erreur("RécupérerSite")

def ConvertirListeEnNombre(Liste):
    try:
        Chaine=""
        for i in Liste:
            Chaine+=str(i)
        return int(Chaine)
    except:
        Erreur("ConvertirListeEnNombre")

def Désincanter(Tuple):
    Sortie=[]
    for i in Tuple:
        for j in i:
            Sortie.append(j)
    return Sortie

def StockerTexte(Chaine,NomFichier,Mode):
    try:
        with open(NomFichier+".txt", Mode, encoding="utf-8") as Fichier:
            Fichier.write(Chaine)
    except:
        Erreur("StockerTexte")

def Soustraire(Dictionnaire1,Dictionnaire2):
    try:
        NouveauDico=[]
        for Mot in Dictionnaire1:
            if Dictionnaire2.count(Mot)==0:
                NouveauDico.append(Mot)
        return NouveauDico
    except:
        Erreur("Soustraire")

def TraduireTexteEnTuple(Nom,Mode):
    try:
        with open(Nom+".txt", 'r', encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.read()
             Dico=ChaineDicoTexte.split(" ")
        try:
            with open(Nom, Mode+'b') as FichierDicoTuple:
                DicoTuplePickler = pickle.Pickler(FichierDicoTuple)
                DicoTuplePickler.dump(Dico)
        except:
            print("Ecriture impossible.")
    except:
        Erreur("TraduireTexteEnTuple")

def TraduireTupleEnTexte(Nom,Mode):
    try:
        with open(Nom, 'rb') as FichierDicoTuple:
            DicoTupleDepickler = pickle.Unpickler(FichierDicoTuple)
            DicoTuple = DicoTupleDepickler.load()
            Dico=" ".join(DicoTuple)
        with open(Nom+".txt", Mode, encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.write(Dico)
    except:
        Erreur("TraduireTupleEnTexte")

def SplitParagraphes(Chaine):
    return Chaine.split("\n \n")

def SplitPhrases(Chaine):
    try:
        Tuple=[]
        PhraseBool=False
        DebutBool=False
        for i in range(len(Chaine)):
            PhraseBool=False
            if AlphabetCompletMinuscules.count(Chaine[i])==1 or Ponctuation.count(Chaine[i])==1 or Chaine[i]==" " or Nombres.count(Chaine[i])==1:
                PhraseBool=True
            else:
                PhraseBool=False
                DebutBool=False
            if i<len(Chaine)-2:
                if CaractèresSpéciaux.count(Chaine[i])==1 and CaractèresSpéciaux.count(Chaine[i+1])==1:
                    PhraseBool=False
                    DebutBool=False
            if AlphabetCompletMajuscules.count(Chaine[i])==1:
                DebutBool=True
                PhraseBool=True
                Phrase=""
            if PhraseBool:
                Phrase+=Chaine[i]
            if DebutBool and PhraseBool and Fin.count(Chaine[i])==1:
                if len(Phrase)>=3:
                    Tuple.append(Phrase)
                DebutBool=False
                PhraseBool=False
        return Tuple
    except:
        Erreur("SplitPhrases")

def AssocierCaractère(Caractère):
    if AlphabetTrèsComplet.count(Caractère)==1:
        return "Alphabet"
    elif CaractèresSpéciaux.count(Caractère):
        return "CaractèresSpéciaux"
    else:
        return "Autre"

def SplitEléments(Chaine):
    try:
        Début=0
        Tuple=[]
        for i in range(len(Chaine)-1):
            if AssocierCaractère(Chaine[i])!=AssocierCaractère(Chaine[i+1]):
                Tuple.append(Chaine[Début:i+1])
                Début=i+1
        Tuple.append(Chaine[-1])
        return Tuple
    except:
        Erreur("SplitEléments")


def SplitMots(Chaine):
    try:
        Chaine=Chaine.lower()
        for i in CaractèresSpéciaux:
            Chaine=Chaine.replace(i," ")
        return Chaine[0:len(Chaine)-1].split(" ")
    except:
        Erreur("SplitMots")


def StockerTuple(Tuple,NomFichierTuple,Mode):
    try:
        with open(NomFichierTuple, Mode+'b') as FichierTuple:
            FichierTuplePickler = pickle.Pickler(FichierTuple)
            FichierTuplePickler.dump(Tuple)
    except:
        Erreur("StockerTuple")

def SortirTuple(NomFichierTuple):
    try:
        with open(NomFichierTuple, 'rb') as FichierTuple:
            FichierTupleDepickler = pickle.Unpickler(FichierTuple)
            try:
               Tuple=[]
               while True:
                   Tuple.append(FichierTupleDepickler.load())
            except:
                return Tuple
    except:
        Erreur("SortirTuple")

def SortirTexte(Fichier):
    try:
        with open(Fichier+".txt", "r",encoding="utf-8") as FichierTexte:
            texte=FichierTexte.read()
        return texte
    except:
        Erreur("SortirTexte")

    

def GenererDictionnaire(Fichier,Dictionnaire):
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
