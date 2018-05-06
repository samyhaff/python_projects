import math
import random
import time

Liste=[1,3,4,6]
Obj=24

print(Liste)
print(Obj)

Nombres=[0]*4
Signes=[0]*3

for a in range(0,3):
    for b in range(0,2):
        for c in range(0,1):
            d=0
            Copie=Liste[:]
            Nombres[0]=Copie[a]
            del Copie[a]
            Nombres[1]=Copie[b]
            del Copie[b]
            Nombres[2]=Copie[c]
            del Copie[c]
            Nombres[3]=Copie[d]
            del Copie[d]
            for h in range(0,4):
                for i in range(0,4):
                    for j in range(0,4):
                        Signes[0]=h
                        Signes[1]=i
                        Signes[2]=j
                        R=Nombres[0]
                        for s in range(0,3):
                            if Signes[s]==0:
                                R=R+Nombres[s+1]
                            if Signes[s]==1:
                                R=R-Nombres[s+1]
                            if Signes[s]==2:
                                R=R*Nombres[s+1]
                            if Signes[s]==3:
                                R=R/Nombres[s+1]
                            if R==Obj:
                                Réponse=["("]*2+[Nombres[0]]
                                for r in range(0,3):
                                    if Signes[r]==0:
                                        Réponse.append("+")
                                    if Signes[r]==1:
                                        Réponse.append("-")
                                    if Signes[r]==2:
                                        Réponse.append("*")
                                    if Signes[r]==3:
                                        Réponse.append("/")
                                    Réponse.append(Nombres[r+1])
                                    Réponse.append(")")
                                Réponse.append(Nombres[r+1])
                                for r in range(0,10):
                                    print(Réponse[r],end="")
                                print(Réponse[10])
                                

                                        
                                            
                                    

                                    
                                    
                    
            


