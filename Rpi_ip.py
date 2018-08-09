from sense_hat import SenseHat
import socket
import random

sense = SenseHat()
ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2$
ip = str(ip)

random_red = random.randint(0, 255)
random_green = random.randint(0, 255)
random_blue = random.randint(0, 255)

sense.show_message(ip)

SenseHat.clear()
