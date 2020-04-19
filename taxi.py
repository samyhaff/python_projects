n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split(" ")))
nb = [0, 0, 0, 0]

def solve():
    for x in s:
        nb[x - 1] += 1

    if nb[1] % 2 == 1:
        nb[0] -= 2
    nb[0] = max(0, nb[0] - nb[2])
    if nb[0] % 4 == 0:
        x = nb[0] // 4
    else:
        x = nb[0] // 4 + 1

    return nb[3] + (nb[1] // 2) + (nb[1] % 2) + nb[2] + x

print(solve())
