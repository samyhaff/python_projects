def FibonacciIteratif(n):
    a = 0
    b = 1
    for i in range(n - 1):
        c = b
        b = a + b
        a = c
    return b

# print(FibonacciIteratif(2))

def FiboRecursif(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FiboRecursif(n - 1) + FiboRecursif(n - 2)

# print(FiboRecursif(2))

def FiboRecursif2(n):
    def aux(n, acc1, acc2):
        if n == 1:
            return acc2
        return aux(n - 1, acc2, acc1 + acc2)
    return aux(n, 0, 1)

# print(FiboRecursif2(2))

# marche mieux en récursif
fibo = {}
def Fibonacci(n):
    global fibo
    fibo.update({0: 0})
    fibo.update({1: 1})
    if n in fibo:
        return fibo[n]
    fibo.update({n: Fibonacci(n - 1) + Fibonacci(n - 2)})
    return fibo[n]

print(Fibonacci(2))
