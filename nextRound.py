import sys
n, k = list(map(int, sys.stdin.readline().split(' ')))
l = list(map(int, sys.stdin.readline().split(' ')))

if l[k - 1] > 0:
    i = k
    while l[i] == l[k-1] and k > 0:
        i+=1
    i-=1
else:
    i = k - 1
    while l[i] == 0 and i >= 0:
        i -= 1
print(i + 1)
