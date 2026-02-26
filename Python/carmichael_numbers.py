import sys

#  Criba para identificar primos 
def criba_eratostenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return sieve

# Exponenciación Binaria: (base^exp) % mod
def power(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res

def is_carmichael(n, is_prime):
    # Un número de Carmichael DEBE ser compuesto
    if is_prime[n]:
        return False
    
    # Debe cumplir a^n ≡ a (mod n) para todo 1 < a < n
    for a in range(2, n):
        if power(a, n, n) != a:
            return False
    return True

def solve():
    is_prime = criba_eratostenes(65000)
    
    carmichael_set = set()
    for i in range(2, 65000 + 1):
        if is_carmichael(i, is_prime):
            carmichael_set.add(i)

    input_data = sys.stdin.read().split()
    for x in input_data:
        n = int(x)
        if n == 0: break
        
        if n in carmichael_set:
            print("The number {} is a Carmichael number.".format(n))
        else:
            print("{} is normal.".format(n))

if __name__ == '__main__':
    solve()