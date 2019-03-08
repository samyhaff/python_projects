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
