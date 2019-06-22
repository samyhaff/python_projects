""" CONSTRUCTION DE P(E)"""

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

def parties(l):
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
    if A == []:
        return [[]]
    a = A[0]
    partiesPartielle = parties2(A[1:])
    reste = []
    for e in partiesPartielle:
        reste.append([a] + e)
    return reste + partiesPartielle

print(parties2([1, 2, 3]))
