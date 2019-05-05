import random
import numpy

def toBin(n):
    bin = []
    while n // 2 > 0 or len(bin) < 8:
        bin.append(n % 2)
        n = n // 2
    bin.reverse()
    return ''.join(str(c) for c in bin)

def simulationErreurs(n):
    if n == 0:
        return message
    indices = random.sample([i for i in range(0, len(message))], n)
    result = ""
    for i in range(0, len(message)):
        if indices.count(i) > 0:
            result += str((int(message[i]) + 1) % 2)
        else:
            result += message[i]
    return result

def toDecimal(n):
    output = 0
    for i in range(0, len(n)):
        output += int(n[i]) * (2 ** (7 - i))
    return output

def toStr():
    output = ""
    n = len(messageRecu) // 8
    for i in range(0, n):
        output += chr(int(toDecimal(messageRecu[8 * i : 8 * (i + 1) + 1])))
    return output

chaine = "Hello, World!"
message = ""
for c in chaine:
    message += ''.join(str(toBin(ord(c))))
messageRecu = simulationErreurs(2)
chaineRecue = toStr()

print(message)
print(chaine)
print(messageRecu)
print(chaineRecue)
