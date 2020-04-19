import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))

M = max(a)
c = [0] * (M + 1)
for x in a:
    c[x] += 1

def solve():
    s = [0, c[1]]
    for i in range(2, M + 1):
        s.append(max(s[i - 1], s[i - 2] + (c[i] * i)))
    return s[-1]

print(solve())
