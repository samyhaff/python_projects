"""
f : mvts possibles -> prochain meilleur mvt

"""




l=[[1,2],[3,4]]


"""[1,2]=>2
[3,4]=>4
[2,4]
2"""


def minmax(arbre, level = 0, maxi = True):
    if type(arbre[0]) is not list:
        if max and level%2==0:
            return max(arbre)
        else:
            return min(arbre)
    else:
        if max and level%2==0:
            return max([minmax(e,level+1,maxi) for e in arbre])
        else:
            return min([minmax(e,level+1,maxi) for e in arbre])

print(minmax(l))
