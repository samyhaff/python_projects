""" question 1
On peut utiliser une liste de booléens où la valeur True correspond à une voiture et la valeur false à une case vide """

""" question 2 """

A = [i in  [0, 2, 3, 10] for i in range(11)]

""" question 3 """

def occupe(L, i):
    return L[i]

""" question 4
Il y a 2^n files de longueur n possibles puisque chaque case peut soit contenir une voiture soit être vide """

""" question 5 """

def egal(L1, L2):
    return L1 == l2

#c'est-à-dire:
def egal(L1, L2):
    if len(L1) != len(L2):
        return False
    for i in range(L1):
        if L1[i] != L2[i]:
            return False
    return True

""" question 6
La complexité de cette fonction est 0(n) puisque dans le pire cas on itère la doucle n fois où n = len(L1) = len(L2)
avec des opérations en temps constant """

""" question 7
Cette fonction retourne un booléen """

""" question 8
avancer(A, False) renvoie [False, True, False, True, True, False, ..., False]
Donc avancer(avancer(A, False), True) renvoie [True, False, True, False, True, True, False, ..., False] """

""" question 9 """

def avancer_fin(L, m):
    return L[:m] + avancer(L[m:], False)

""" question 10 """

def avancer_debut(L, b, m):
    return avancer(L[:m + 1], b) + L[m + 1:]

""" question 11 """

def avancer_debut_bloque(L, b, m):
    i = m - 1
    while ocupe(L, i) and i >= 0:
        i -= 1
    return avancer_debut(L, b, i)

""" question 12 """

def avancer_files(L1, b1, L2, b2):
    m = len(L1) // 2
    A = avancer_fin(L1, m)
    B = avancer_fin(L2, m)
    R1 = avancer_debut(A, m)
    if occupe(R1, m):
        R2 = avancer_debut_bloque(B, b2, m)
    else:
        R2 = avancer_debut(B, b2, m)
    return [R1, R2]

""" question 13
on obtient R1 = [False, False, True, False, True] et R2 = [False, True, False, True, False] """

""" question 14
Si on rajoute toujours une voiture à la première case de L1 et que les autres cases avant le croisement sont déjà occupées par des voitures alors,
puisque L1 et prioritaire sur L2, aucune voiture de L2 ne poura passer le croisement, la file serait alors indéfiniment bloquée """

""" question 15
Le nombre minimum d'étapes permetant de passer de 4a) à 4b) vaut 9.
En effet, il faut 5 étapes pour que les 4 voitures de L1 passent le croisement puis,
si on ne rajoute pas de nouvelles voitures en L1, il faudra encore 5 étapes pour arriver à 4b) """

""" question 16
Non on ne peut pas passer de la 4a) à la 4c) puisque ce passage reviendrait à une situation où les voitures de L2 passeraient
le croisement avant celles de L1 ce qui est impossible puisque la file L1 est prioritaire """

""" question 17 """

def elim_double(L):
    return list(set(L))

# c'est-à-dire

def elim_double(L):
    A = []
    y = None
    for x in L:
        if x != y:
            y = x
            A.append(x)
    return A

""" question 18
On obtient [1, 2, 3, 5] """

""" question 19
Non car cette fonction compare les élements consécutifs """

""" question 20
La fonction rechercher retourne des booléens
but est un état (liste de booléens)
espace est une liste d'états
successeurs retourne une liste d'états """

""" question 21
in2 est une rechercher dichotomique et in1 est une recherche linéaire,
il faut donc utiliser in2 qui est de plus faible complexité """

""" question 22 """

def versEntier(L):
    s = 0
    n = len(L)
    for i in range(n - 1, - 1, -1):
        s += L[ n - 1 - i] * (2 ** i) # multiplier par True revient à multiplier par 1 et par False revient à multiplier par 0
    return s

""" question 23
La valeur de taille doit être d'au moins E(log_2(n)) + 1
Il faut écrire while n > 0 en ligne 4 """

""" question 24
La fonction recherche s'arrête dès que stop = True
Invariant de boucle: nombre d'élements de espace uniques
stop passe à True dès que ce nombre ne change pas au cours d'une itèration
Or ce nombre est majoré et croissant donc stationaire
Donc stop passera à True
Donc recherche s'arrête """

""" question 25
on ajoute i = 0 avant la boucle, i += 1 à l'intérieur de la boucle et on retourne True et i ou False et None """

""" question 26
SELECT id_croisement_fin FROM Voie WHERE id_croisement_debut = c """

""" question 27
SELECT longitude, latitude FROM Voie JOIN Croisement ON Voie.id_croisement_fin = Croisement.id WHERE Voie.id_croisement_debut = c """

""" question 28
Cette requête renvoie les identifiants des croisements accessibles en 2 étapes depuis c """
