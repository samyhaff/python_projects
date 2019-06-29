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

def pow(x, a):
    if a == 0:
        return 0b00000001
    returen mul(x, pow(x, a - 1))

def makeExpTable(prim):
    global expTable
    x = 1
    for i in range(2, 255):
        expTable[i] = mul(expTable[i - 1], 0b00000010)

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
