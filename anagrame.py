def anagrame(mot):
    if len(mot) == 1:
        return [mot]
    mot2 = mot[1:len(mot)]
    lettre = mot[0]
    anagrames2 = anagrame(mot2)
    anagrames = []
    for a in anagrames2:
        for i in range(0, len(a) + 1):
            anagrames.append(a[0:i] + lettre + a[i:len(a)])
    return list(anagrames)

print(anagrame("abc"))
