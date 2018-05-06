from Fonctions import*

Recherche=input("Rechercher: ")
Urls=Rechercher(Recherche,10)
for Url in Urls:
    RécupérerUnSite(Url,Recherche)
