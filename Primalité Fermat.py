from Fonctions import*
p=int(input("Nombre: "))

a=2
while a<100 and a**(p-1)%p==1:
    a+=1
    

if a>=100:
    print("Premier")
else:
    print("Pas premier")
        
