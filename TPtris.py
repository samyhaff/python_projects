### Tris du cours

import time
import random
import matplotlib.pyplot as plt

"""
t1 = time.time()
t2 = time.time(
u = t2 - t1
"""

def tri_selection(L):
    n=len(L)
    for i in range(n-1):
        imin=i
        for j in range(i+1,n):
            if L[j]<L[imin]:
              imin=j
        if i!=imin:
            L[i],L[imin]=L[imin],L[i]

def tri_bulles(L):
    p=len(L)
    pasfini=True
    while pasfini:
        pasfini=False
        for i in range(p-1):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
                pasfini=True
        p-=1

def tri_insertion(L):
    n=len(L)
    for i in range(1,n):
        j=i
        x=L[i]
        while j>0 and L[j-1]>x:
            L[j]=L[j-1]
            j-=1
        L[j]=x

def fusion(L1,L2):
    L=[]
    i1=0
    i2=0
    n1=len(L1)
    n2=len(L2)
    for i in range(n1+n2):
        if i2==n2 or i1<n1 and L1[i1]<=L2[i2]:
            L.append(L1[i1])
            i1+=1
        else:
            L.append(L2[i2])
            i2+=1
    return L

def tri_fusion(L):
    n=len(L)
    m=len(L)//2
    if n<=1:
        return L[:]
    else:
        return fusion(tri_fusion(L[:m]),tri_fusion(L[m:]))

def partition(L,g,d):
    pivot=L[g]
    m=g
    for i in range(g+1,d):
        if L[i]<pivot:
            m+=1
            if i>m:
                L[i],L[m]=L[m],L[i]
    if m>g:
        L[m],L[g]=L[g],L[m]
    return m

def tri_rapide(L):
    def aux(g,d):
        if g<d-1:
            m=partition(L,g,d)
            aux(g,m)
            aux(m+1,d)
    aux(0,len(L))

def genererListe(n):
    l = [random.randint(1, 10001) for _ in range(n)]
    return l

X = [i for i in range(1, 1001)]
Y = []
for i in range(1, 1001):
    l = genererListe(i)
    t1 = time.time()
    tri_insertion(l)
    t2 = time.time()
    Y.append(t2 -t1)
plt.plot(X, Y, label = "insertion")

Y2 = []
for i in range(1, 1001):
    l = genererListe(i)
    t1 = time.time()
    tri_selection(l)
    t2 = time.time()
    Y2.append(t2 -t1)
plt.plot(X, Y2, label = "selection")
plt.show()

def drapeau(l):
    n = len(l)
    c = [0 for i in range(3)]
    for x in l:
        c[x] += 1
    l = []
    for i in range(3):
        l += [i] * c[i]

def bernoulli(p):
    x = random.random()
    if x <= p:
        return 1
    return 0

def simulation(v):
    x = random.random()
    y = v[0]
    i = 0
    while x > y:
        i += 1
        y += v[i]
    return i
 
