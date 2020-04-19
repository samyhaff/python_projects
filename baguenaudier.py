import sys

n = int(sys.stdin.readline())

l  = [1] * n


def viderTout(l,i):
    for j in reversed(range(i+1)):
        vider(l,j)

def vider(l,i):
    if l[i]:
        if i==1:
            remplir(l,0)
        elif i>1:
            remplir(l,i-1)
            viderTout(l,i-2)
        l[i] = 0
        print(i+1)

def remplir(l,i):
    if not l[i]:
        if i==1:
            remplir(l,0)
        elif i>1:
            remplir(l,i-1)
            viderTout(l,i-2)
        l[i] = 1
        print(i+1)

viderTout(l,n-1)
