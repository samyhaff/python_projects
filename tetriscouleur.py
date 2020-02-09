def creerGrille(largeur, hauteur):
    return [[VIDE for _ in range(hauteur)] for _ in range(largeur)]

def afficherGrille(grille):
    largeur = len(grille)
    hauteur = len(grille[0])
    for j in range(largeur):
        for i in range(hauteur):
            case = grille[largeur - i - 1][j]
            if case == VIDE:
                afficherBlanc()
            else:
                afficherCouleur(case)
            if j == :
                nouvelleLigne()
        nouvelleLigne()

def grilleLibre(grille, k):
    largeur = len(grille)
    hauteur = len(grille[0])
    for i in range(largeur):
        c = True
        for j in range(hauteur - 1, 0, -1):
            if grille[i][j] != VIDE:
                c = False
        if c:
            return True
    return False

# 0(largeur * hauteur)

def descnete(grille, y, k):
    
