import itertools

def queensAttack(n, k, r_q, c_q, obstacles):
    directions=[[x,y] for x in [-1,0,1] for y in [-1,0,1] if (x,y)!=(0,0)]
    a=0
    for direction in directions:
        dx,dy=direction
        x,y=r_q+dx,c_q+dy
        while (1<=x<=n and 1<=y<=n):
            if [x,y] in obstacles:
                break
            x+=dx
            y+=dy
            a+=1
    return a

def stones(n, a, b):
    if n == 0:
        return [0]
    return [a + x for x in stones(n - 1, a, b)] + [b + x for x in stones(n - 1, a, b)]

def stones(n, a, b):
    l=list(range(n*min(a,b),n*max(a,b)))
    return list(filter(lambda e:(e%a)%b==0,l))

a = 2
b = 3
0 0
1 2 3
2 4 5 6
3

def stones(n, a, b):
    ans = []
    borne = n * max(a, b)
    for i in range(0, borne + 1):
        for j in range(0, borne + 1):
            if i + j == n:
                ans.append(a * i + b * j)
    return sorted(set(ans))

for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1]= a[j]
        j-=1
    a[j + 1] = key
    print(*a)

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

def closestNumbers(arr):
    min_distance = float("inf")
    arr.sort()
    pairs = []
    for i in range(n - 1):
        x = arr[i+1] - arr[i]
        if x < min_distance:
            pairs=[]
            min_distance = x
        if x == min_distance:
            min_distance = x
            pairs += [arr[i],arr[i+1]]
    return pairs

def findMedian(arr):
    return sorted(arr)[len(arr)//2]

def fact(n):
	def aux(n, acc):
		if n == 1:
			return acc
		return aux(n - 1, n * acc)
	return aux(n, 1)

nb_tests = int(input())

def fact(n):
	def aux(n, acc):
		if n == 1:
			return acc
		return aux(n - 1, n * acc)
	return aux(n, 1)

def fake_hash(s):
	ans = 1
	for i in range(0, n):
		ans *= fact(ord(s[i]) - ord("a") + 2)

for t in range(nb_tests):
	s1 = input().strip()
	n = len(s1)

def missingNumbers(arr, brr):
    while len(arr)>0:
        brr.remove(arr[0])
        del arr[0]
    return brr

def missingNumbers(arr, brr):
    for a in arr:
        brr.remove(a)
    return sorted(set(brr))

def balancedSums(arr):
    s = 0
    for i in range(n):
        for j in range(i + 1):
            s = arr[j] - arr[-j - 1]
        if s == 0:
            return "YES"
            break
    return "NO"

def balancedSums(arr):
    if n==0 or n==1:
        return "YES"
    s=sum(arr)
    a=0
    for i in range(n):
        a+=arr[i]
        if a==s-a-arr[i]:
            return "YES"
    return "NO"




def balancedSums(arr):
    if n==0 or n==1:
        return "YES"
    s=sum(arr)
    a=0
    for i in range(n):
        if a==s-a-arr[i]:
            return "YES"
        a+=arr[i]
    return "NO"


def jimOrders(orders):
    return [v[0]+1 for v in sorted(list(enumerate(orders)),key=lambda a:a[0]+a[1])]

def twoArrays(k, A, B):
    A.sort(reverse=True)
    B.sort()
    for i in range(n):
        if A[i]+B[i]<k:
            return "NO"
    return "YES"

def toBin(x, l):
    l += 1 # l correspond au nombre de digits
    s = ""
    y = x
    while y > 0:
        s = str(y % 2) + s
        y = y // 2
    r = ""
    for i in range(1, l - len(s)):
        r = r + "0"
    s = r + s
    return s

def flippingBits(n):
    n = toBin(n, 32)
    l = map(int, list(n))
    for i in range(0, 32):
        l[i] ^= l[i]
    return int("0b" + "".join(l))

def flippingBits(n):
    binary=lambda x,m:[(int(o)//2**(i-1))%2**i for i in range(m)]
    integer=lambda l:sum(map(lambda x:x**i),)
    l=b(n,32)
    #s="".join(map(str,l))
    xor=lambda x:1-x
    #l1=map(int,list(s))
    for i in range(0, 32):
        l[i] = l[i] ^ l[i]


def flippingBits(n):
    binary=lambda x,m:list(reversed([int((x%2**(i+1))//2**i) for i in range(m)]))
    xor=lambda l:list(map(lambda x:1-x,l))
    decimal=lambda l:sum([v*2**i for (i,v) in enumerate(list(reversed(l)))])

    n=binary(n,32)
    n=xor(n)
    n=decimal(n)

    return n

prod=lambda l:functools.reduce(lambda a,b:a*b,l)
a=prod(list(range(1,n+1)))
