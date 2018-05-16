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
CaractèresSpéciaux="#@&°_¨^+-=*$¥€£`%§/:;?!.,<>\()\""
Nombres="0123456789"


Consonnes="bcçdfghjklmnpqrstvwxyÿz"
Voyelles=["a","à","æ","e","é","è","ê","ë","i","î","ï","o","ô","œ","u","ù","û","ü"]
SonsVoyelles=[["a","à","æ"],["e","œ"],["é"],["i","î","ï","y"],["o","ô"],["u","ù","û","ü"],["on"],["ou","oo"],["ai","ay","ei","ey","è","ê","ë"],["an","en"],["ain","ein","un","in"]]
SonsConsonnes=[["bb","b"],["qu","ck","cc","c","k","q"],["dd","d"],["ff","ph","f"],["gg","gu","g"]]

PronomsPersonnelsGroupés=[["je"],["tu"],["il,elle,on"],["nous"],["vous"],["ils,elles"]]
PronomsPersonnelsPrincipaux=["je","tu","il","nous","vous","ils"]
PronomsPersonnels=["je","tu","il","elle","on","nous","vous","ils","elles"]

Français=["le","la","les","de","des","un","une","et","à","il","ne","je",
              "son","que","se","qui","se","dans","en","du","elle","au","ce",
              "ces","pour","pas","vous","par","sur","faire","plus","dire",
              "mon","lui","nous","comme","mais","avec","tout","y"]
Anglais=["the","be","to","of","and","a","in","that","have","i","it","for"
             ,"not","with","he","as","you","do","at","this","but","his","by",
             "from","they","we","say","her","she","or","an","will","my","one",
             "all","would","there","their","what","so","up","out","if","about",
             "who","get","which","go","when","make","can","like","time",
             "no","just","him","know","take","people","into","year","your",
             "good","some","could","them","see","other","than","then","now",
             "look","only","come","its","over","think","also","back","after",
             "use","two","how","our","work","first","well","way","even","new",
             "want","because","any","these","give","day","most","us"]
  
Langues=[Français,Anglais]

CaractéristiquesMots=["Apparition totale","Apparition sur site","Synonyme","Précédé","Suivi","Langue"]

#https://www.notrefamille.com/dictionnaire/definition/manger/


#vide,français,autrelangue

#Fonctions

AfficherErreur=False


def ComparerLangue(Tuple,Langue):
    Nombre=0
    Intrus=[]
    for Mot in Langue:
        if Tuple.count(Mot)>0:
            Intrus.append(Mot*Tuple.count(Mot))
    return Intrus

def AjouterDictionnaire(Tuple,Dictionnaire):
    Réduction=Réduire(Tuple)
    for Mot in Réduction:
        if Dictionnaire.count(Mot)==0:
            Dictionnaire[Mot]=Réduction.count(Mot)
        else:
            Dictionnaire[Mot]=Dictionnaire[Mot]+Réduction.count(Mot)
    return Dictionnaire
        
    

def EliminerVide(Tuple):
    while Tuple.count([])>0:
        Tuple.remove([])
    return Tuple

def ExterminerVide(Tuple,Niveau):
    Base=1
    w
    
    
    

def ValiditéLangue(Tuple,Langue):
    Exceptions=0
    for LangueConsidérée in Langues:
        if LangueConsidérée!=Langue:
            Exceptions+=len(ComparerLangue(Tuple,LangueConsidérée))
    Validité=int(len(ComparerLangue(Tuple,Langue))/len(Tuple)*100)
    if Validité>5 and Exceptions==0:
        return True
    else:
        return False
    


def Erreur(Fonction):
    global AfficherErreur
    if AfficherErreur:
        print("La fonction",Fonction,"n'a pas pue être exécutée.")
    StockerTexte(Fonction+" ","Erreurs","a")

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

def DécomposerEnSyllables(Mot):
    Mot=Mot.lower()
    Tuple=[]
    Début=0
    if Consonnes.count(Mot[0])==1:
        ExceptionBool=True
    else:
        ExceptionBool=False
    for i in range(len(Mot)-1):
        if Consonnes.count(Mot[i])==1:
            if Voyelles.count(Mot[i+1])==1:
                if ExceptionBool==False:
                    Tuple.append(Mot[Début:i])
                    Début=i
                else:
                    ExceptionBool=False
        if Mot[i]==" ":
            Tuple.append(Mot[Début:i])
            Début=i+1
            if Consonnes.count(Mot[i+1])==1:
                ExceptionBool=True
            else:
                ExceptionBool=False                   
    Tuple.append(Mot[Début:])
    return Tuple



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
        Mot=Mot.lower()
        if Mot[-1]=="e" or Mot[-2:]=="e.":
            Syllables=-1
        else:
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

def Réduire(Entree):
    try:
        Sortie=[Entree[0]]
        for i in range(0,len(Entree)-1):
            if Entree[i]!=Entree[i+1]:
                Sortie.append(Entree[i+1])
        return Sortie
    except:
        Erreur("Réduire")

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

def PermuterAléatoirement(Entrée):
    Sortie=[]
    while Entrée!=[]:
        i=random.randint(0,len(Entrée)-1)
        Sortie.append(Entrée[i])
        del Entrée[i]
    return Sortie
        

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
        Erreur("ConvertirTexteEnTuple")

def TraduieTupleEnTexte(Nom,Mode):
    try:
        with open(Nom, 'rb') as FichierDicoTuple:
            DicoTupleDepickler = pickle.Unpickler(FichierDicoTuple)
            DicoTuple = DicoTupleDepickler.load()
            Dico=" ".join(DicoTuple)
        with open(Nom+".txt", Mode, encoding="utf-8") as FichierDicoTexte:
             ChaineDicoTexte=FichierDicoTexte.write(Dico)
    except:
        Erreur("ConvertirTupleEnTexte")

def SplitParagraphes(Chaine):
    try:
        return Chaine.split("\n \n")
    except:
        Erreur("SplitParagraphes")

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


def SplitMotsRaté(Chaine):
    try:
        Chaine=Chaine.lower()
        for i in CaractèresSpéciaux:
            Chaine=Chaine.replace(i," ")
        for i in Nombres:
            Chaine=Chaine.replace(i," ")
        Chaine=Chaine.replace("'"," ")
        return Chaine[0:len(Chaine)-1].split(" ")
    except:
        Erreur("SplitMotsRaté")

def SplitMots(Chaine):
    try:
        Chaine=Chaine.lower()
        Tuple=[]
        MotBool=False
        DébutBool=False
        for i in range(len(Chaine)):
            MotBool=False
            if AlphabetCompletMinuscules.count(Chaine[i])==1:
                MotBool=True
                if DébutBool==False:
                    DébutBool=True
                    Mot=""
            else:
                MotBool=False
            if MotBool:
                Mot+=Chaine[i]
            if DébutBool and MotBool==False:
                if len(Mot)>=2 and CompterSyllables(Mot)>0:
                    Tuple.append(Mot)
                DébutBool=False
                MotBool=False
        return Tuple
    except:
        Erreur("SplitMots")

def DicoDesSynos(Chaine):
    Tuple=[]
    MotBool=False
    for i in range(len(Chaine)-5):
        if Chaine[i:i+1]=="\">":
            MotBool=True
            Début=i+2
        if MotBool and AlphabetTrèsComplet.count(Chaine[i])==0:
            MotBool=False
        if Chaine[i:i+3]=="</a>" and MotBool:
            Tuple.append(Chaine[Début:i-1])
            MotBool=False
    print(Tuple)
            
            
            
        
        
    

def TrouverSynonymes(Mot):
    Tuple=[]
    Mot=Mot.lower()
    Url="https://www.notrefamille.com/dictionnaire/definition/"+Mot+"/"
    CodeSource=DéterminerCodeSource(Url)
    #Extraire("<a href=\"?mot=",[],">)
    Extraire("\">",[],"</a>")
    return Tuple
    
def TrouverDansChaine(SousChaine,Chaine):
    try:
        Len=len(Chaine)-len(SousChaine)
        for i in range(Len):
            if Chaine[i:i+len(SousChaine)]==SousChaine:
                return i
        return None
    except:
        Erreur("TrouverDansChaine")
        

def EliminerCopies(Liste):
    try:
        for i in Liste:
            while Liste.count(i)>1:
                Liste.remove(i)    
        return Liste
    except:
        Erreur("EliminerCopies")


def StockerVariable(Tuple,NomFichierTuple,Mode):
    try:
        with open(NomFichierTuple, Mode+'b') as FichierTuple:
            FichierTuplePickler = pickle.Pickler(FichierTuple)
            FichierTuplePickler.dump(Tuple)
    except:
        Erreur("StockerTuple")

def SortirVariable(NomFichierTuple):
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

def Sortir(Fichier):
    try:
        with open(Fichier, "r",encoding="utf-8") as FichierTexte:
            texte=FichierTexte.read()
        return texte
    except:
        Erreur("Sortir")

#Permutation

def prod(Liste):
    Nombre=1
    for i in Liste:
        Nombre*=i
    return Nombre

def sum(Liste):
    Nombre=1
    for i in Liste:
        Nombre+=i
    return Nombre

def size(Liste):
    Nombre=1
    Coefficient=1
    for i in Liste:
        Nombre+=i*Coefficient
        Coefficient*=i
    return Nombre
        
def AjouterSystème(Progression,Système,Ajout):
    Nombre=SortirSystème(Progression,Système)
    Nombre=(Nombre+Ajout)%size(Système)
    Progression=EntrerSystème(Nombre,Système)
    return Progression

def SortirSystème(Progression,Système):
    Nombre=0
    Coefficient=1
    for i in range(len(Système)):
        Nombre+=Progression[-i-1]*Coefficient
        Coefficient*=Système[-i-1]
    return Nombre

def EntrerSystème(Nombre,Système):
    Progression=[]
    Coefficient=prod(Système)
    for i in range(len(Système)):
        Coefficient//=Système[i]
        Progression.append(Nombre//Coefficient)
        Nombre=Nombre%Coefficient
    return Progression

#IA

def MoyenneParagraphes(Structure):
    Nombre=0
    for i in Structure:
        Nombre+=len(i)
    return Nombre/len(Structure)

#Statistiques

def Statistiques(Liste):
    Liste.sort()
    Indice1erQuartile=len(Liste)//4
    IndiceMédianne=len(Liste)//2
    Indice3eQuartile=(3*len(Liste))//4
    Statistiques={}
    Moyenne=0
    v1erQuartile=0
    Médianne=0
    v3eQuartile=0
    for i in range(len(Liste)):
        Moyenne+=Liste[i]
        if i==Indice1erQuartile:
            v1erQuartile=Liste[i]
        if i==IndiceMédianne:
            Médianne=Liste[i]
        if i==Indice3eQuartile:
            v3eQuartile=Liste[i]
    Moyenne=Moyenne/len(Liste)
    Réduite=Réduire(Liste)
    Maximum=0
    Majorité=0
    for i in Réduite:
        if Liste.count(i)>Maximum:
            Maximum=Liste.count(i)
            Majorité=i
    Statistiques["Moyenne"]=Moyenne
    Statistiques["Médianne"]=Médianne
    Statistiques["Majorité"]=Majorité
    Statistiques["1er Quartile"]=v1erQuartile
    Statistiques["3e Quartile"]=v3eQuartile
    Statistiques["Ecart-Type"]=v3eQuartile-v1erQuartile
    Statistiques["Minimum"]=Liste[0]
    Statistiques["Maximum"]=Liste[-1]
    Statistiques["Etendu"]=Liste[-1]-Liste[0]
    
    return Statistiques
    
def StatsParagraphes(Structure):
    Liste=[]
    for i in Structure:
        Liste.append(len(i))
    return Liste

    
    


#Ancien

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
