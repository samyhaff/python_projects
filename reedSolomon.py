"""Corps de Galois de cardinal 256"""

logTable = [i for i in range(255)]
expTable = [0] * 256
expTable[1] = 0b00000010

def add(x, y):
    return x ^ y

def sub(x, y):
    return add(x, y)

def mul(x,y):
    z = 0
    i = 0
    while (y>>i) > 0:
        if y & (1<<i):
            z ^= x<<i
        i+=1
    return z

def bit_length(n):
    bits = 0
    while n >> bits: bits += 1
    return bits

def div(dividend, divisor):
    dl1 = bit_length(dividend)
    dl2 = bit_length(divisor)
    if dl1 < dl2:
        return dividend
    # Else, align the most significant 1 of the divisor to the most significant 1 of the dividend (by shifting the divisor)
    for i in range(dl1 - dl2, -1,- 1):
        # Check that the dividend is divisible (useless for the first iteration but important for the next ones)
        if dividend & (1 << i + dl2 - 1):
            # If divisible, then shift the divisor to align the most significant bits and XOR (carry-less subtraction)
            dividend ^= divisor << i
    return dividend

def mul_mod(x, y, mod = 0b100011101):
    result = mul(x, y)
    if mod > 0:
        return div(result, mod)
    return result

def makeExpTable(prim = 0b100011101):
    global expTable
    x = 1
    for i in range(2, 255):
        expTable[i] = mulMod(expTable[i - 1], 0b00000010, prim)

def mul2(x, y):
    global logTable
    if x == 0 or y == 0:
        return 0
    a = logTable[x]
    b = logTable[y]
    return expTable(a + b)

def div2(x, y):
    if y == 0:
        raise ZeroDivisionError()
    if x == 0:
        return 0
    return expTable[(logTable[x] + 255 - gf_log[y]) % 255] # on s'assure que l'exposant est positif

def power(x, a):
    return expTable[(logTable[x] * power) % 255]

def inverse(x):
    return expTable[255 - logTable[x]]

"""Polynomes"""

def polynome_mulScalaire(p, x):
    r = [0] * len(p)
    for i in range(0, len(p)):
        r[i] = mul2(p[i], x)
    return r

def polynome_add(p, q):
    r = [0] * max(len(p), len(q))
    for i in range(0, len(p)):
        r[i+len(r)-len(p)] = p[i]
    for i in range(0,len(q)):
        r[i+len(r)-len(q)] ^= q[i]
    return r

def polynome_mul(p, q):
    r = [0] * (len(p)+len(q)-1)
    for j in range(0, len(q)):
        for i in range(0, len(p)):
            r[i+j] ^= mul2(p[i], q[j]) # equivalent to r[i + j] = gf_add(r[i+j], gf_mul(p[i], q[j]))
    return r

def polynome_eval(p, x):
    y = p[0]
    for i in range(1, len(p)):
        y = mul2(y, x) ^ p[i]
    return y

def rs_gen(nb_symboles):
    g = [1]
    for i in range(nb_symboles):
        g = polynome_mul(g, [1, power(2, i)])
    return g

def degree(p):
    d = len(p) - 1
    while p[d] == 0:
        d-=1
    return d

def polynome_division(dividend, divisor):
    R = list(dividend)
    B = list(divisor)
    Q = []
    while degree(R) >= degree(B):
        d = degree(R) - degree(B) + 1
        C = [0] * d
        C[-1] = div2(R[-1], B[-1])
        R = polynome_add(R, polynome_mul(B, C))
        Q = polynome_add(Q, C)
    return (Q, R)

def rs_encode_msg(msg_in, nb_symboles):
    gen = rs_gen(nb_symboles)
    _, remainder = polynome_div(msg_in, gen)
    msg_out = polynome_add(msg_in, remainder)
    return msg_out

def rs_calc_syndromes(msg, nb_symboles):
    synd = [0] * nb_symboles
    for i in range(0, nsym):
        synd[i] = polynome_eval(msg, power(2,i))
    return [0] + synd # pad with one 0 for mathematical precision (else we can end up with weird calculations sometimes)

def rs_check(msg, nsym):
    return ( rs_calc_syndromes(msg, nb_symboles) == 0 )

def rs_errasures_loc(e_pos):
    e_loc = [1]
    for i in e_pos:
        e_loc = polynome_mul( e_loc, polynome_add([1], [power(2, i), 0]) )
    return e_loc

def rs_eval(synd, err_loc, nb_symboles):
    _, remainder = polynome_div(polynome_mul(synd, err_loc), ([1] + [0]*(nb_symboles+1)))
    return remainder

def rs_correct_errasures(msg_in, synd, err_pos):
    pass 
