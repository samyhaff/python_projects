import math

Liste1=[0]*5
Liste2=[0]*5

y=0
Liste2[2]=1

while y<=5:
    y=y+1
    i=1
    Liste1=Liste2
    while i<=3:
        Liste2[i]=1
        if Liste1[i-1]==0 and Liste1[i]==0 and Liste1[i+1]==0:
            Liste2[i]=0

        print(Liste1[2])
        Liste2[i]=0
        print(Liste1[2])
        print()
        
        i=i+1

