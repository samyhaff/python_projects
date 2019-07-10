t = int(input().strip())

for i in range(t):

    stalls = []
    N, C = input().split()
    N, C = int(N), int(C)
    for i in range(N):
        x = int(input())
        stalls.append(x)
    stalls = sorted(stalls)
    l = 0 # valeur vérifiant f(x) = 1
    r = stalls[N - 1] - stalls[0] # valeur vérifiant f(x) = 0

    def f(x):
        happy_cows = 1
        last_placed = 0
        for i in range(1, N):
            if stalls[i] - stalls[last_placed] - 1 >= x:
                happy_cows += 1
                last_placed = i
                if happy_cows >= C:
                    return True
        return False

    def binnary_search(l, r):
        mid = (r + l) // 2
        if r - l - 1 == 0:
            return l
        elif f(mid):
            binnary_search(mid, r)
        else:
            binnary_search(l, mid)

    # print(binnary_search(l, r))
