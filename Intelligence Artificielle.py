from Fonctions import*
import math
import pygame
import numpy as np
from pygame.locals import *



#---------#
#Variables#
#---------#

#Archive

FichierDictionnaire="DictionnaireInfini.txt"
FichierHistoriqueUrl="HistoriqueUrl.txt"
FichierBaseDeDonnées="BaseDeDonnées.txt"
FichierRecherchés="Recherchés.txt"
FichierNonRecherchés="NonRecherchés.txt"
    
#Vif
FichierDictionnaireTuple="DictionnaireInfiniTuple"
FichierHistoriqueUrlTuple="HistoriqueUrlTuple"
FichierBaseDeDonnéesTuple="BaseDeDonnéesTuple"
FichierRecherchésTuple="RecherchésTuple"
FichierNonRecherchésTuple="NonRecherchésTuple"

#Initialisations

try:
    Dictionnaire=SortirTuple(FichierDictionnaireTuple)
    HistoriqueUrl=SortirTuple(FichierHistoriqueUrlTuple)
    BaseDeDonnées=SortirTuple(FichierBaseDeDonnéesTuple)
    Recherchés=SortirTuple(FichierRecherchésTuple)
    NonRecherchés=SortirTuple(FichierNonRecherchésTuple)
except:
    Dictionnaire=[]
    HistoriqueUrl=[]
    BaseDeDonnées=[]
    Recherchés=[]
    NonRecherchés=["Mot"]



#---------#
#Fonctions#
#---------#

def TestQuitter():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_ESCAPE:
                return True
    return False



#-------#
#Actions#
#-------#

while TestQuitter==False:
    Recherche=NonRecherchés[0]
    Recherchés.append(Recherche)
    del NonRecherchés[0]
    Urls=Rechercher(Recherche,10)
    HistoriqueUrl.append(Urls)
    Stocker(HistoriqueUrl[-1],FichierHistoriqueUrlTuple,a)
    ConvertirTupleEnTexte(FichierHistoriqueUrlTuple,FichierHistoriqueUrl,'a')
    for Url in Urls:
        Texte=RécupérerUnSite(Url)
        BaseDeDonnéesTuple.append(Texte)
        
        
    
        
    
    
    
    
    
