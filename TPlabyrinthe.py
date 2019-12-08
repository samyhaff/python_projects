## classe Pile
class Pile_liste:
    def __init__(self):
        self.contenu=[]

    def pile_vide(self):
        return self.contenu==[]

    def empiler(self,x):
        self.contenu.append(x)

    def sommet(self):
        assert not self.pile_vide(), "la pile est vide"
        return self.contenu[-1]

    def depiler(self):
        assert not self.pile_vide(), "la pile est vide"
        return self.contenu.pop()

## Classes Case et Labyrinthe
import matplotlib.pyplot as plt

class Case:
    def __init__(self):
        self.N = True
        self.W = True
        self.S = True
        self.E = True
        self.etat = False # indique si la case a ete visitee

class Labyrinthe:
    def __init__(self, larg, haut):
        self.haut = haut
        self.larg = larg
        self.tab = [[Case() for j in range(haut)] for i in range(larg)]

    def create_plot(self):
        """affiche le labyrinthe"""
        l, h = self.larg, self.haut
        plt.clf()
        # repere orthonorme
        plt.axis("equal")
        # gestion des bords
        plt.xlim((-1, self.larg + 1))
        plt.ylim((-1, self.haut + 1))
        # tracer des murs exterieurs
        plt.plot([0, 0, l, l, 0], [0, h, h, 0, 0], linewidth=2)
        # tracer des murs interieurs
        for x in range(l):
            for y in range(h):
                # tracer des murs interieurs horizontaux
                if y < h and self.tab[x][y].N:
                    plt.plot([x, x+1], [y+1, y+1], 'b')
                # tracer des murs interieurs verticaux
                if x < l and self.tab[x][y].E:
                    plt.plot([x+1, x+1], [y, y+1], 'b')

    def show(self):
        self.create_plot()
        plt.show()

    def clean(self):
    #    """'nettoie' le labyrinthe,
    #    i.e. supprime les traces d'un eventuel precedent parcours"""
        for i in range(self.larg):
            for j in range(self.haut):
                self.tab[i][j].etat = False

    #def solution(self):
    #    """trace le chemin solution du labyrinthe"""


## generation de labyrinthes parfaits
from random import randint, choice

def creation_labyrinthe(larg, haut):
#    """renvoie une instance de la classe Labyrinthe
#    representant un labyrinthe parfait de taille larg*haut"""
    # generation d'un labyrinthe aux murs fermes
    lab = Labyrinthe(larg, haut)
    # choix d'une case au hasard
    case = [choice([i for i in range(larg)]), choice([j for j in range(haut)])]
    # creation de la pile (des coordonnees) des cases a traiter
    pile = Pile_liste()
    pile.empiler(case)
    lab.tab[case[0]][case[1]].etat = True
    # Tant que la pile n'est pas vide...
    while not pile.pile_vide():
        # visite du sommet
        case = pile.sommet()
        lab.tab[case[0]][case[1]].etat = True
        # creation de la liste des cases adjacentes non visitees
        voisins = []
        x = case[0]
        y = case[1]
        if x > 0 and not lab.tab[x - 1][y].etat:
            voisins.append([x - 1, y])
        if y > 0 and not lab.tab[x][y - 1].etat:
            voisins.append([x, y - 1])
        if x < larg - 1 and if not lab.tab[x + 1][y].etat:
            voisins.append([x + 1, y])
        if y < haut - 1 and not lab.tab[x][y + 1].etat:
            voisins.append([x, y + 1])
        # Si toutes les cases adjacentes ont ete visitees
        if voisins == []:
            pile.depiler()
        # Sinon
        else:
            case = choice(voisins)
            lab.tab[case[0]][case[1]].etat = True
            if x - case[0] == 1:
                lab.tab[case[0]][case[1]].E = False
                lab.tab[x][y].W = False
            if x - case[0] == -1:
                lab.tab[case[0]][case[1]].W = False
                lab.tab[x][y].E = False
            if y - case[1] == 1:
                lab.tab[case[0]][case[1]].N = False
                lab.tab[x][y].S = False
            if y - case[1] == -1:
                lab.tab[case[0]][case[1]].S = False
                lab.tab[x][y].N = False
            pile.empiler(case)
    # on renvoie le labyrinthe (sans l'afficher)
    return lab

## Test
#maze = creation_labyrinthe(30,30)
#maze.show()

## recherche d'un chemin
def depthFirstSearch(maze):
    """parcourt le labyrinthe en profondeur,
    depuis le coin inferieur gauche jusqu'au coin superieur droit"""
    trajet = []
    # Nettoyage du labyrinthe (a quoi ça sert ?)
    maze.clean()
    # Creation et initialisation de la pile de trajet
    entree = [0, 0]
    sortie = [maze.larg - 1, maze.haut - 1]
    pile = Pile_liste()
    pile.empiler(entree)
    trajet.append(entree)
    # On marque la case (0,0) comme visitee
    maze.tab[entree[0]][entree[1]] = True
    # On cree un drapeau indiquant si la sortie a ete trouvee
    def sortie_trouvee = False
    # On continue tant qu'on n'a pas atteint la sortie
    while not sortie_trouvee:
        # on visite la derniere case empilee
        case = pile.sommet()
        maze.tab[case[0]][case[1]].etat = True
        # Si on trouve la sortie, c'est gagne !
        if case = sortie:
            sortie_trouvee = True
        # Sinon on teste successivement chacune des cases adjacentes
        # non visitees (et on marque la case !)
        accessibles = []
        if not (maze.tab[case[0]][case[1]].E and maze.tab[case[0] + 1][case[1]].etat):
            accessibles.append([case[0] + 1, case[1]])
        if not (maze.tab[case[0]][case[1]].W and maze.tab[case[0] - 1][case[1]].etat):
            accessibles.append([case[0] - 1, case[1]])
        if not (maze.tab[case[0]][case[1]].N and maze.tab[case[0]][case[1] + 1].etat):
            accessibles.append([case[0], case[1] + 1])
        if not (maze.tab[case[0]][case[1]].S and maze.tab[case[0]][case[1] - 1].etat):
            accessibles.append([case[0], case[1] - 1])
        if accessibles != []:
            for c in accessibles:
                pile.empiler(c)
                trajet.append(c)
                maze.tab[c[0]][c[1]].etat = True
        # Si toutes les cases testees sont visitees,
        # on est arrive a une impasse, la case actuelle
        # n'est pas donc sur le trajet !
        else:
            pile.depiler()
    # Une fois le chemin trouve, on nettoie le labyrinthe
    maze.clean()    
    # on renvoie le trajet
    return trajet

## Test
#maze.solution()

lab = creation_labyrinthe(25,30)
lab.show()
