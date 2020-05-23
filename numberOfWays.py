import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))

def countways(a, n):
    cnt = [0 for i in range(n)]
    s = 0
    s = sum(a)

    if (s % 3 != 0):
        return 0

    s //= 3
    ss = 0
    for i in range(n - 1, -1, -1):
        ss += a[i]
        if (ss == s):
            cnt[i] = 1
    for i in range(n - 2, -1, -1):
        cnt[i] += cnt[i + 1]

    ans = 0
    ss = 0
    for i in range(0, n - 2):
        ss += a[i]
        if (ss == s):
            ans += cnt[i + 2]
    return ans

print(countways(a, n))
