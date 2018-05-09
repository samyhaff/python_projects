from Fonctions import*


FichierDictionnaire="DictionnaireInfini.txt"
FichierDictionnaireTuple="DictionnaireInfinieTuple"

BaseDeDonnées="BaseDeDonnées.txt"
HistoriqueUrl="HistoriqueUrl.txt"

Tuple=["Mot"]

StockerTuple(Tuple,FichierDictionnaireTuple)
ConvertirTupleEnTexte(FichierDictionnaireTuple,FichierDictionnaire)
ConvertirTexteEnTuple(Dictionnaire,Tuple)



for Mot in Tuple:
    Urls=Rechercher(Mot,10)
    RécupérerUnSite(Url,BaseDeDonnées)
