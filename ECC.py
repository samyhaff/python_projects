import serial

#ser = serial.Serial("/dev/tty.usbmodem141101")
chaine = "Hello World!"
#ser.write([message])

"""
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

message = ""
for c in chaine:
    message += ''.join(str(toBin(ord(c))))
print(message)
