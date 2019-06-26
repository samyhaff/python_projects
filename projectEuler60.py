import math
import time
import itertools

#itertools.combination(iterable,n)

listePremiers = []

def timer(function):
    def function(*args):
        t0=time.time()
        result=function(*args)
        t1=time.time()
        return result
    return function.__name__+" took "+str(t1-t0)+"seconds."

# partitions

def parties1(l):
    def toBin(x, l):
        l += 1 # l correspond au nombre de digits
        s = ""
        y = x
        while y > 0:
            s = str(y % 2) + s
            y = y // 2
        r = ""
        for i in range(1, l - len(s)):
            r = r + "0"
        s = r + s
        return s

    parties = []
    cardinal = len(l)
    nbParties = 2 ** cardinal
    for i in range(0, nbParties):
        e = []
        index = toBin(i, cardinal)
        for j in range(cardinal):
            if index[j] == "1":
                e.append(l[j])
        parties.append(e)
    return parties

def parties2(A):
    # pas du tout efficace
    if A == []:
        return [[]]
    a = A[0]
    partiesPartielle = parties2(A[1:])
    reste = []
    for e in partiesPartielle:
        reste.append([a] + e)
    return reste + partiesPartielle

#Primes

def isPrime_(n):
    global listePremiers
    if listePremiers.count(n) > 0:
        return True
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    listePremiers.append(n)
    return True

def isPrime(n):
    if n==0 or n==1: return False
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False
    p=int(math.sqrt(n))+1
    for i in range(6,p,6):
        if n%(i-1)==0 or n%(i+1)==0:
            return False
    return True

def arePrimes(*l1):
    for e in l1:
        if not isPrime(e):
            return False
    return True

#Relations

def cond2(a, b, c, d, e):
    couples = []
    parties = parties1([a, b, c, d, e])
    if not isPrime(a) or not isPrime(b) or not isPrime(c) or not isPrime(d) or not isPrime(e):
        return False
    for partie in parties:
        if len(partie) == 2:
            p = [str(i) for i in partie]
            nb1 = int("".join(p))
            nb2 = int("".join(p[::-1]))
            if not isPrime(nb1) or not isPrime(nb2):
                return False
    return True

def relation2(a,b):
    # teste primalité concatenation
    return isPrime(int(str(a)+str(b))) and isPrime(int(str(b)+str(a)))

def relations(*l1):
    # teste tous les couples
    l=len(l1)
    for i in range(l):
        for j in range(i+1,l):
            if not relation2(l1[i],l1[j]):
                return False
    return True

def egalites(*l1):
    l=len(l1)
    for i in range(l):
        for j in range(i+1,l):
            if l1[i]!=l1[j]:
                return False
    return True

def cond(*l1):
    if egalites(*l1):
        return False
    if not arePrimes(*l1):
        return False
    return relations(*l1)

def main1():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    n = 1

    while not cond(a, b, c, d, e):
        e = (e + 1) % n
        if e % n == 0: # saute la 1iere itération mais on s'en fout
            d = (d + 1) % n
        if d % n == 0:
            c = (c + 1) % n
        if c % n == 0:
            b = (b + 1) % n
        if b % n == 0:
            a = (a + 1) % n
        if a % n == 0 and b % n == 0 and c % n == 0 and d % n == 0 and e % n == 0:
            n+=1
        print(a,b,c,d,e)
        time.sleep(0.5)

def premierSuivant(premier):
    premier+=2
    while not isPremier(premier):
        premier+=2
    return premier

def etendrePremiers(premiers,i):
    l=len(premiers)
    if l>i: return premiers
    for j in range(l-i):
        premiers.append(premierSuivant(premiers[-1]))
    return premiers


def main2():
    l1=premiers=etendrePremiers([],5)
    #l2 de taille 5, de somme n, et dans l'ordre lexicographique
    """
    l2=[0,1,2,3,4]
    l2=[0,1,2,3,5]

    l2=[0,1,2,4,5]
    l2=[0,1,2,4,6]

    l2=[0,1,3,5,6]
    l2=[0,1,3,4,6]
    l2=[0,1,3,4,7]

    l2=[0,1,3,5,6]
    """

    while not cond(l1):
        premiers=etendrePremiers(premiers,len(premiers)+1)
        l1[:-1]=premiers[-1]

if __name__=="__main__":
    main1()
