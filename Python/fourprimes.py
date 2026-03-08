import sys

# Precomputamos la Criba hasta 10^7
MAX_N = 10000000
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

def sieve():
    p = 2
    while p * p <= MAX_N:
        if is_prime[p]:
            for i in range(p * p, MAX_N + 1, p):
                is_prime[i] = False
        p += 1

# Ejecutamos la criba una sola vez al inicio
sieve()

def solve_goldbach(target):
    # Buscamos dos primos que sumen 'target'
    for p in range(2, target // 2 + 1):
        if is_prime[p] and is_prime[target - p]:
            return p, target - p
    return None

def main():
    input_data = sys.stdin.read().split()
    for line in input_data:
        n = int(line)
        
        if n < 8:
            print("Impossible.")
            continue
            
        if n % 2 == 0:
            # Caso Par
            p1, p2 = 2, 2
            remainder = n - 4
        else:
            # Caso Impar
            p1, p2 = 2, 3
            remainder = n - 5
            
        p3, p4 = solve_goldbach(remainder)
        print("{} {} {} {}".format(p1, p2, p3, p4))

if __name__ == '__main__':
    main()