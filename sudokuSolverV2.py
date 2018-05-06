import random

board = []

with open("board.csv", "r") as boardFile:
    for line in boardFile:
        n = line.split(",")
        for i in range(0,9):
            board.append(n[i].strip())

for i in range(0, 81):
    board[i] = int(board[i])x

dboard = ["."] * 81
for i in range(0, 81):
    if board[i] == 0:
        dboard[i] = "."
    else:
        dboard[i] = board[i]

print("input:")
def affichage():
    print(dboard[0], dboard[1], dboard[2], "|", dboard[3], dboard[4], dboard[5], "|", dboard[6], dboard[7],dboard[8])
    print(dboard[9], dboard[10], dboard[11], "|", dboard[12], dboard[13], dboard[14], "|", dboard[15], dboard[16],dboard[17])
    print(dboard[18], dboard[19], dboard[20], "|", dboard[21], dboard[22], dboard[23], "|", dboard[24], dboard[25], dboard[26])
    print("------+-------+------")
    print(dboard[27], dboard[28], dboard[29], "|", dboard[30], dboard[31], dboard[32], "|", dboard[33], dboard[34], dboard[35])
    print(dboard[36], dboard[37], dboard[38], "|", dboard[39], dboard[40], dboard[41], "|", dboard[42], dboard[43],dboard[44])
    print(dboard[45], dboard[46], dboard[47], "|", dboard[48], dboard[49], dboard[50], "|",  dboard[51],dboard[52], dboard[53])
    print("------+-------+------")
    print(dboard[54], dboard[55], dboard[56], "|", dboard[57], dboard[58], dboard[59], "|", dboard[60], dboard[61], dboard[62])
    print(dboard[63], dboard[64], dboard[65], "|", dboard[66], dboard[67], dboard[68], "|", dboard[69], dboard[70], dboard[71])
    print(dboard[72], dboard[73], dboard[74], "|", dboard[75], dboard[76], dboard[77], "|", dboard[78], dboard[79], dboard[80])
affichage()





        
        

