from os import system
 
system("color 0C")
limite = 2000
x = 0
 
for i in range(limite):
    if x < i*100/limite:
        system("cls")
        x = i*100/limite+1
        print x,"%"
         
system("cls")
print "[","|"*50,"]  ",100,"%"
 
raw_input("Pour terminer le programme, appuyez sur une touche .")
