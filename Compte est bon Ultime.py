import math
import random
import time

Liste=[random.randint(1,9)]+[random.randint(1,9)]+[random.randint(1,9)]+[random.randint(1,9)]+[random.randint(1,9)]+[random.randint(10,20)]+[random.randint(10,20)]
Obj=random.randint(500,1000)

print(Liste)
print(Obj)

Nombres=[0]*7
Signes=[0]*6

for a in range(0,7):
    for b in range(0,6):
        for c in range(0,5):
            for d in range(0,4):
                for e in range(0,3):
                    for f in range(0,2):
                        g=0
                        Copie=Liste[:]
                        Nombres[0]=Copie[a]
                        del Copie[a]
                        Nombres[1]=Copie[b]
                        del Copie[b]
                        Nombres[2]=Copie[c]
                        del Copie[c]
                        Nombres[3]=Copie[d]
                        del Copie[d]
                        Nombres[4]=Copie[e]
                        del Copie[e]
                        Nombres[5]=Copie[f]
                        del Copie[f]
                        Nombres[6]=Copie[g]
                        del Copie[g]

                        for h in range(0,4):
                            for i in range(0,4):
                                for j in range(0,4):
                                    for k in range(0,4):
                                        for l in range(0,4):
                                            for m in range(0,4):
                                                Signes[0]=h
                                                Signes[1]=i
                                                Signes[2]=j
                                                Signes[3]=k
                                                Signes[4]=l
                                                Signes[5]=m
                                                R=Nombres[0]
                                                for s in range(0,6):
                                                    if Signes[s]==0:
                                                        R=R+Nombres[s+1]
                                                    if Signes[s]==1:
                                                        R=R-Nombres[s+1]
                                                    if Signes[s]==2:
                                                        R=R*Nombres[s+1]
                                                    if Signes[s]==3:
                                                        R=R/Nombres[s+1]
                                                    if R==Obj:
                                                        Réponse=["("]*(m-2)+[Nombres[0]]
                                                        for r in range(0,m-1):
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
                                                        for r in range(0,4*m-6):
                                                            print(Réponse[r],end="")
                                                        print(Réponse[len(Réponse)-1])
                                                        s=6
                                                    
                                                        
                                                

                                                
                                                
                                
                        

