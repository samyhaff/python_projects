from tkinter import *
import math
import random
import time

#Initialisation
Width = 500
Height = 500
cx=6
cy=6
L=Width//3//3//2+1
l=Height//3//3//2+1
Victoire=0
gameover=False
gameovertest=0
Player=0
IA=False
#Fin Initialisation

def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")

def affichage_grille(grille):
    global i,Xc,Yc
    for b in range(0,3):
        for a in range(0,3):
            i=a+3*b
            x=Width*(2*a+1)//6
            y=Height*(2*b+1)//6
            img.put("#000000",(x,y))
            rectangle = canvas.create_rectangle(x-L+cx, y-l+cy, x+L+cx, y+l+cy, fill="white")
            canvas.coords(rectangle, x-3*L+cx, y-3*l+cy, x+3*L+cx, y+3*l+cy)
            if grille[i]=="X":
                cross1 = canvas.create_line(x-L+cx, y-l+cy, x+L+cx, y+l+cy, fill="blue")
                cross2 = canvas.create_line(x-L+cx, y+l+cy, x+L+cx, y-l+cy, fill="blue")
                canvas.coords(cross1, x-L+cx, y-l+cy, x+L+cx, y+l+cy)
                canvas.coords(cross2, x-L+cx, y+l+cy, x+L+cx, y-l+cy)
            if grille[i]=="O":
                circle = canvas.create_oval(x-L+cx, y-l+cy, x+L+cx, y+l+cy, fill="white")
                canvas.coords(circle, x-L+cx, y-l+cy, x+L+cx, y+l+cy)
            canvas.pack()
    Xa=Width*(2*Xc+1)//6
    Ya=Height*(2*Yc+1)//6
    if Player==0:
        cross1 = canvas.create_line(Xa-L+cx, Ya-l+cy, Xa+L+cx, Ya+l+cy, fill="red")
        cross2 = canvas.create_line(Xa-L+cx, Ya+l+cy, Xa+L+cx, Ya-l+cy, fill="red")
        canvas.pack()
    else:
        circle = canvas.create_oval(Xa-L+cx, Ya-l+cy, Xa+L+cx, Ya+l+cy, fill="red")
        canvas.pack()
 
def tour(grille, joueur):
    print("C'est le tour du joueur "+str(joueur))
    colonne=input("Entrez le numero de la colonne : ")
    ligne=input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case ("+colonne+","+ligne+")")
    while grille[int(colonne)+int(ligne)*3]!=" ":
        afficher_grille(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
 
    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_grille(grille)
 
def est_gagnant(joueur):
    global Victoire
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]==joueur):
        Victoire=1
        Gagner(joueur)
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]==joueur):
        Victoire=2
        Gagner(joueur)
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]==joueur):
        Victoire=3
        Gagner(joueur)
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]==joueur):
        Victoire=4
        Gagner(joueur)
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]==joueur):
        Victoire=5
        Gagner(joueur)
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]==joueur):
        Victoire=6
        Gagner(joueur)
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]==joueur):
        Victoire=7
        Gagner(joueur)
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[1]==joueur):
        Victoire=8
        Gagner(joueur)
    

def reflexion_IA2():
    scores=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    if niveau>=1:
        i=0
        for case in grille:
            if case==' ':
                ligne_test=int((i)//3)
                colonne_test=int((i)%3)
                grille[int(colonne_test)+int(ligne_test)*3]="O"
                if est_gagnant(grille):
                    scores[int(colonne_test)+int(ligne_test)*3]+=100000
                else:
                    j=0
                    for case2 in grille:
                        if case2==' ':
                            ligne_test2=int((j)//3)
                            colonne_test2=int((j)%3)
                            grille[int(colonne_test2)+int(ligne_test2)*3]="X"
                            if est_gagnant(grille):
                                scores[int(colonne_test2)+int(ligne_test2)*3]+=10000
                            else:
                                if niveau>=2:
                                    k=0
                                    for case3 in grille:
                                        if case3==' ':
                                            ligne_test3=int((k)//3)
                                            colonne_test3=int((k)%3)
                                            grille[int(colonne_test3)+int(ligne_test3)*3]="O"
                                            if est_gagnant(grille):
                                                scores[int(colonne_test)+int(ligne_test)*3]+=1000
                                            else:
                                                l=0
                                                for case4 in grille:
                                                    if case4==' ':
                                                        ligne_test4=int((l)//3)
                                                        colonne_test4=int((l)%3)
                                                        grille[int(colonne_test4)+int(ligne_test4)*3]="X"
                                                        if est_gagnant(grille):
                                                            scores[int(colonne_test2)+int(ligne_test2)*3]+=100
                                                        else:
                                                            if niveau==3:
                                                                m=0
                                                                for case5 in grille:
                                                                    if case5==' ':
                                                                        ligne_test5=int((m)//3)
                                                                        colonne_test5=int((m)%3)
                                                                        grille[int(colonne_test5)+int(ligne_test5)*3]="O"
                                                                        if est_gagnant(grille):
                                                                            scores[int(colonne_test)+int(ligne_test)*3]+=10
                                                                        else:
                                                                            n=0
                                                                            for case6 in grille:
                                                                                if case6==' ':
                                                                                    ligne_test6=int((l)//3)
                                                                                    colonne_test6=int((l)%3)
                                                                                    grille[int(colonne_test6)+int(ligne_test6)*3]="X"
                                                                                    if est_gagnant(grille):
                                                                                        scores[int(colonne_test2)+int(ligne_test2)*3]+=1                                                                                            
                                                                                    grille[int(colonne_test6)+int(ligne_test6)*3]=' '
                                                                                n+=1
                                                                        grille[int(colonne_test5)+int(ligne_test5)*3]=' '
                                                                    m+=1
                                                                m=0                                                                                                                            
                                                        grille[int(colonne_test4)+int(ligne_test4)*3]=' '
                                                    l+=1
                                            grille[int(colonne_test3)+int(ligne_test3)*3]=' '
                                        k+=1
                                    k=0
                            grille[int(colonne_test2)+int(ligne_test2)*3]=' '
                        j+=1
                grille[int(colonne_test)+int(ligne_test)*3]=' '
            else:
                scores[i]=-100000000
            i+=1
        i=0
        resultat_max=-10000000000
        ligne_max=0
        colonne_max=0
        for resultat in scores:
            if int(resultat)>resultat_max:
                resultat_max=resultat
                ligne_max=int((i)//3)
                colonne_max=int((i)%3)
            i+=1
    grille[int(colonne_max)+int(ligne_max)*3]="O"
    afficher_grille(grille)

def reflexion_IA():
    scores=[0]*9
    scores2=[0]*9
    scores3=[0]*9
    scores4=[0]*9
    scores5=[0]*9
    scores6=[0]*9
    scores7=[0]*9
    scores8=[0]*9
    
    if niveau>=1:
        i=0
        for case in grille:
            if case==' ':
                ligne_test=int((i)//3)
                colonne_test=int((i)%3)
                grille[int(colonne_test)+int(ligne_test)*3]="O"
                if est_gagnant(grille):
                    scores[i]+=10000000
                else:
                    j=0
                    for case2 in grille:
                        if case2==' ':
                            ligne_test2=int((j)//3)
                            colonne_test2=int((j)%3)
                            grille[int(colonne_test2)+int(ligne_test2)*3]="X"
                            if est_gagnant(grille):
                                scores2[j]+=1000000
                            else:
                                if niveau>=2:
                                    k=0
                                    for case3 in grille:
                                        if case3==' ':
                                            ligne_test3=int((k)//3)
                                            colonne_test3=int((k)%3)
                                            grille[int(colonne_test3)+int(ligne_test3)*3]="O"
                                            if est_gagnant(grille):
                                                scores3[i]+=100000
                                            else:
                                                l=0
                                                for case4 in grille:
                                                    if case4==' ':
                                                        ligne_test4=int((l)//3)
                                                        colonne_test4=int((l)%3)
                                                        grille[int(colonne_test4)+int(ligne_test4)*3]="X"
                                                        if est_gagnant(grille):
                                                            scores4[j]+=10000
                                                        else:
                                                            if niveau>=3:
                                                                m=0
                                                                for case5 in grille:
                                                                    if case5==' ':
                                                                        ligne_test5=int((m)//3)
                                                                        colonne_test5=int((m)%3)
                                                                        grille[int(colonne_test5)+int(ligne_test5)*3]="O"
                                                                        if est_gagnant(grille):
                                                                            scores5[i]+=1000
                                                                        else:
                                                                            n=0
                                                                            for case6 in grille:
                                                                                if case6==' ':
                                                                                    ligne_test6=int((l)//3)
                                                                                    colonne_test6=int((l)%3)
                                                                                    grille[int(colonne_test6)+int(ligne_test6)*3]="X"
                                                                                    if est_gagnant(grille):
                                                                                        scores6[j]+=100
                                                                                    else:
                                                                                        if niveau==4:
                                                                                            o=0
                                                                                            for case7 in grille:
                                                                                                if case7==' ':
                                                                                                    ligne_test7=int((o)//3)
                                                                                                    colonne_test7=int((o)%3)
                                                                                                    grille[int(colonne_test7)+int(ligne_test7)*3]="O"
                                                                                                    if est_gagnant(grille):
                                                                                                        scores7[i]+=10
                                                                                                    else:
                                                                                                        p=0
                                                                                                        for case8 in grille:
                                                                                                            if case8==' ':
                                                                                                                ligne_test8=int((p)//3)
                                                                                                                colonne_test8=int((p)%3)
                                                                                                                grille[int(colonne_test8)+int(ligne_test8)*3]="X"
                                                                                                                if est_gagnant(grille):
                                                                                                                    scores8[j]+=1
                                                                                                                grille[int(colonne_test8)+int(ligne_test8)*3]=' '
                                                                                                            p+=1
                                                                                                        p=0
                                                                                                        resultat_max=-10
                                                                                                        for resultat in scores8:
                                                                                                            if int(resultat)>resultat_max:
                                                                                                                resultat_max=resultat
                                                                                                                pp=p
                                                                                                            p+=1
                                                                                                        scores7[pp]+=resultat_max
                                                                                                        scores8=[0]*9
                                                                                                    grille[int(colonne_test7)+int(ligne_test7)*3]=' '
                                                                                                o+=1
                                                                                            o=0
                                                                                            resultat_max=-10
                                                                                            for resultat in scores7:
                                                                                                if int(resultat)>resultat_max:
                                                                                                    resultat_max=resultat
                                                                                                    oo=o
                                                                                                o+=1
                                                                                            scores6[oo]+=resultat_max
                                                                                            scores7=[0]*9
                                                                                            o=0                                                                       
                                                                                    grille[int(colonne_test6)+int(ligne_test6)*3]=' '
                                                                                n+=1
                                                                            n=0
                                                                            resultat_max=-10
                                                                            for resultat in scores6:
                                                                                if int(resultat)>resultat_max:
                                                                                    resultat_max=resultat
                                                                                    nn=n
                                                                                n+=1
                                                                            scores5[nn]+=resultat_max
                                                                            scores6=[0]*9
                                                                        grille[int(colonne_test5)+int(ligne_test5)*3]=' '
                                                                    m+=1
                                                                m=0
                                                                resultat_max=-10
                                                                for resultat in scores5:
                                                                    if int(resultat)>resultat_max:
                                                                        resultat_max=resultat
                                                                        mm=m
                                                                    m+=1
                                                                scores4[mm]+=resultat_max
                                                                scores5=[0]*9                                                                                                                          
                                                        grille[int(colonne_test4)+int(ligne_test4)*3]=' '
                                                    l+=1
                                                l=0
                                                resultat_max=-10
                                                for resultat in scores4:
                                                    if int(resultat)>resultat_max:
                                                        resultat_max=resultat
                                                        ll=l
                                                    l+=1
                                                scores3[ll]+=resultat_max
                                                
                                                scores4=[0]*9
                                            grille[int(colonne_test3)+int(ligne_test3)*3]=' '
                                        k+=1
                                    k=0
                                    resultat_max=-10
                                    for resultat in scores3:
                                        if int(resultat)>resultat_max:
                                            resultat_max=resultat
                                            kk=k
                                        k+=1
                                    scores2[kk]+=resultat_max
                                    scores3=[0]*9
                                    k=0
                            grille[int(colonne_test2)+int(ligne_test2)*3]=' '
                        j+=1
                    j=0                       
                    resultat_max=-10
                    for resultat in scores2:
                        if int(resultat)>resultat_max:
                            resultat_max=resultat
                            jj=j
                        j+=1
                    scores[jj]+=resultat_max
                    scores2=[0]*9
                grille[int(colonne_test)+int(ligne_test)*3]=' '
            else:
                scores[i]=-100000000000000000
            i+=1
        i=0
        resultat_max=-1000000000000000000000000
        ligne_max=0
        colonne_max=0
        for resultat in scores:
            if int(resultat)>resultat_max:
                resultat_max=resultat
                ligne_max=int((i)//3)
                colonne_max=int((i)%3)
            i+=1
    grille[int(colonne_max)+int(ligne_max)*3]="O"

def est_match_nul(grille):
    if grille.count(" ")==0:
        window.quit()
 
def Gagner(joueur):
    global Victoire,gameover
    if Victoire==1:
        a=0
        b=2
    if Victoire==2:
        a=3
        b=5
    if Victoire==3:
        a=6
        b=8
    if Victoire==4:
        a=0
        b=6
    if Victoire==5:
        a=1
        b=7
    if Victoire==6:
        a=2
        b=8
    if Victoire==7:
        a=0
        b=8
    if Victoire==8:
        a=6
        b=2
    x1=a%3
    y1=a//3
    x2=b%3
    y2=b//3
    X1=Width*(2*x1+1)//6
    Y1=Height*(2*y1+1)//6
    X2=Width*(2*x2+1)//6
    Y2=Height*(2*y2+1)//6
    cross = canvas.create_line(X1+cx, Y1+cy, X2+cx, Y2+cy, fill="black")
    canvas.coords(cross, X1+cx,Y1+cy,X2+cx,Y2+cy)
    canvas.pack()
    gameover=True
    if joueur=="X":
        label = Label(window, text="Vous avez gagné.", bg="white")
        label.pack()
    if joueur=="O":
        label = Label(window, text="Vous avez perdu.", bg="white")
        label.pack()

def Oui():
    global IA,niveau
    label = Label(window, text="Veuillez sélectionner un niveau de difficulté", bg="white")
    label.pack()
    label.pack()
    bouton1=Button(window, text="1", command=Facile)
    bouton2=Button(window, text="2", command=Moyen)
    bouton3=Button(window, text="3", command=Difficile)
    bouton4=Button(window, text="4", command=Impossible)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()
    bouton4.pack()
    IA=True

def Facile():
    global niveau
    niveau=1
    window.quit()
def Moyen():
    global niveau
    niveau=2
    window.quit()
def Difficile():
    global niveau
    niveau=3
    window.quit()
def Impossible():
    global niveau
    niveau=4
    window.quit()
    
def Non():
    global IA
    Ia=False
    window.quit()

def clavier(event):
    global Xc,Yc,Player,IA
    touche=event.keysym
    if IA==True:
        if gameover==False:
            if touche=="Left" and Xc>0:
                Xc=Xc-1
            if touche=="Down" and Yc<2:
                Yc=Yc+1
            if touche=="Right" and Xc<2:
                Xc=Xc+1
            if touche=="Up" and Yc>0:
                Yc=Yc-1
            affichage_grille(grille)
            if touche=="Return":
                i=Xc+3*Yc
                grille[i]="X"
                est_gagnant("X")
                affichage_grille(grille)
                if gameover==False:
                    est_match_nul(grille)
                    reflexion_IA()
                    est_gagnant("O")
                    affichage_grille(grille)
                    est_match_nul(grille)
        else:
            window.quit()
    else:
        if gameover==False:
            if touche=="Left" and Xc>0:
                Xc=Xc-1
            if touche=="Down" and Yc<2:
                Yc=Yc+1
            if touche=="Right" and Xc<2:
                Xc=Xc+1
            if touche=="Up" and Yc>0:
                Yc=Yc-1
            affichage_grille(grille)
            if touche=="Return":
                i=Xc+3*Yc
                if Player==0:
                    grille[i]="X"
                    est_gagnant("X")
                    affichage_grille(grille)
                else:
                    grille[i]="O"
                    est_gagnant("O")
                    affichage_grille(grille)
                est_match_nul(grille)
                Player=(Player+1)%2
        else:
            window.quit()                
            

window=Tk()
niveau=0
label = Label(window, text="Voulez vous jouer contre la IA?", bg="white")
label.pack()
boutonO=Button(window, text="Oui", command=Oui)
boutonN=Button(window, text="Non", command=Non)
boutonO.pack()
boutonN.pack()
window.mainloop()
window.destroy()

window=Tk()
grille=[" "," "," "," "," "," "," "," "," "]
gagne=0
canvas = Canvas(window, width=Width+cx, height=Height+cy, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=Width+cx, height=Height+cy)
canvas.create_image((Width//2+cx, Height//2+cy), image=img, state="normal")
bouton=Button(window, text="Fermer", command=window.quit)
bouton.pack()
Xc=1
Yc=1
affichage_grille(grille)
canvas.focus_set()
canvas.bind("<Key>", clavier)
window.mainloop()
window.destroy()

print("La partie est finie.")
    
