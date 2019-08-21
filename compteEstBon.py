import copy

"""
objectif = int(input("saisir le nb a obtenir: "))
n = int(input("saisir la quantité de nombres disponibles: "))
nb = []
for i in range(n):
    nb.append(int(input().strip()))
"""

objectif = 8136
numbers = [4,5,6,7,8,9]

def couples(A):
    ans = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans.append([A[i], A[j]])
    return ans

toInt=lambda x:list(map(eval,x))
toStr=lambda x:list(map(str,x))

def operations(A):
    a, b = A
    ans = []
    ans=[]
    ans.append(a+"+"+b)
    ans.append(a+"-"+b)
    ans.append(b+"-"+a)
    if eval(b) != 0:
        ans.append(a+"/"+b)
    elif eval(a) != 0:
        ans.append(b+"/"+a)
    ans.append(a+"*"+b)
    ans=["("+a+")" for a in ans]
    return ans

def adapt(A, result, couple):
    B = A[:]
    a, b = couple
    B.remove(a)
    B.remove(b)
    B.append(result)
    return B

#"(5*2)+4*5-2"

#[1,5,6,2,9]
#["1","5","6","2","9"]


#[6,6,2,9]
#["1+5","6","2","9"]



#["1+5","6","11"]

#[6,6,11]


#[36,2,9]
#["(1+5)*6","2","9"]


[2,2,1]

def resoudre(nb, objectif):
    for couple in couples(nb):
        for result in operations(couple):
            nb_ = adapt(nb, result, couple)
            if eval(result) == objectif:
                print(result)
                return True
            if resoudre(nb_, objectif):
                return True
    return False



def resoudre2(nb, objectif):
    if resoudrePourAveugle(nb,objectif):
        return True
    else:
        for couple in couples(nb):
            for result in operations(couple):
                nb_ = adapt(nb, result, couple)
                if eval(result) == objectif:
                    print(result)
                    return True
                if resoudre(nb_, objectif):
                    return True
        return False


def resoudreTout(nb, objectif,historique=[]):
    for couple in couples(nb):
        for result in operations(couple):
            nb_ = adapt(nb, result, couple)
            if eval(result) == objectif:
                historique.append(objectif)
            if resoudreTout(nb_, objectif):
                return True
    return False

def resoudrePourAveugle(nb,objectif):
    l=toInt(nb)
    if objectif in l:
        i=l.index(objectif)
        print(nb[i])
        return True
    return False


if __name__ == "__main__":
    numbers=toStr(numbers)
    resolu=resoudrePourAveugle(numbers,objectif)
    if not resolu:
        resolu=resoudre(numbers, objectif)
    if resolu:
        print("Le compte est bon.")
    else:
        print("nope.")
