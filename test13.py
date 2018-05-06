import pickle

with open("DicoVulgaireTuple", 'rb') as FichierDicoTuple:
    DicoTupleDepickler = pickle.Unpickler(FichierDicoTuple)
    DicoTuple = DicoTupleDepickler.load()
    Dico=""
    for Mot in DicoTuple:
        Dico=Dico+Mot+" "
    print(Dico)
