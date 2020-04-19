p, q = input().split(" ")
t = []

for i in range(int(p)):
    t.append(input().split(" "))

long = [[0 for i in range(int(q))] for j in range(int(p))]

for i in range(int(p)):
    for j in range(int(q)):
        if t[i][j] == "1":
            long[i][j] = 0
        elif i == 0 or j == 0:
            if t[i][j] == "0":
                long[i][j] = 1
            else:
                long[i][j] = 0
        else:
            long[i][j] = 1 + min([long[i][j - 1], long[i - 1][j], long[i - 1][j - 1]])

maxi = 0
for i in range(int(p)):
    for j in range(int(q)):
        if long[i][j] > maxi:
            maxi = long[i][j]

print(maxi)
