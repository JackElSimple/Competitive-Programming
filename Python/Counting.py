import sys

def solve():
    # Precomputamos hasta 1000
    limit = 1000
    dp = [0] * (limit + 1)
    
    # Casos base
    dp[0] = 1 # {}
    dp[1] = 2 # {1, 2}
    dp[2] = 5 # {11, 12, 21, 3, 4}
    
    # Llenamos la tabla usando la relación "a(n) = 2*a(n-1) + a(n-2) + a*(n-3)"
    for i in range(3, limit + 1):
        dp[i] = 2 * dp[i-1] + dp[i-2] + dp[i-3]
    
    # Lectura hasta EOF 
    input_data = sys.stdin.read().split()
    for line in input_data:
        if line:
            n = int(line)
            print(dp[n])

if __name__ == "__main__":
    solve()