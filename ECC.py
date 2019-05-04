import serial
import random
import numpy
import matplotlib
import scipy

#ser = serial.Serial("/dev/cu.usbmodem141301")
chaine = "i"

"""
READ SERIAL:

with Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
    if port_serie.isOpen():
        while True:
            ligne = port_serie.read_line()
            print ligne
"""

def toBin(n):
    bin = []
    while n // 2 > 0 or len(bin) < 8:
        bin.append(n % 2)
        n = n // 2
    bin.reverse()
    return ''.join(str(c) for c in bin)

def simulationErreurs(n):
    indices = random.sample([i for i in range(0, len(message))], n)
    result = ""
    for i in range(0, len(message)):
        if indices.count(i) > 0:
            result += str((int(message[i]) + 1) % 2)
        else:
            result += message[i]
    return result

message = ""
for c in chaine:
    message += ''.join(str(toBin(ord(c))))

reception = simulationErreurs(len(message))

#er.write(message.encode('utf-8'))
print(message)
print(reception)
