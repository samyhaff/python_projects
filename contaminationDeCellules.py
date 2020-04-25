u0 = 123
u = [u0]
v = [u0]

def calcul_u(n):
    for i in range(len(u) - 1, n + 1):
        u.append((16365 * u[i]) % 65521)

def calcul_v(n):
    for i in range(len(v) - 1, n + 1):
        v.append((16379 * v[i]) % 65519)

calcul_u(13)
print(u)
