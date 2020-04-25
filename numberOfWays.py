import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))

c = [0] * n
c[0] = a[0]
for i in range(1, n):
    c[i] = c[i - 1] + a[i]

c2 = [0] * n
c2[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    c2[i] = c2[i + 1] + a[i]

S = sum(a)
s = S // 3

def solve():
    k = 0
    if S % 3 != 0:
        return k
    for i in range(0, n):
        if c[i] == s:
            k += c2[i + 2:].count(s)
    return k

print(solve())
