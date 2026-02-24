import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n_cases = int(input_data[0])

    current_idx = 1
    
    for _ in range(n_cases):
        # Cada caso tiene un x y un y
        x = int(input_data[current_idx])
        y = int(input_data[current_idx + 1])
        current_idx += 2
        
        d = y - x
        
        # Caso base
        if d == 0:
            print(0)
            continue
            
        # n = sqrt(d) truncado
        n = int(math.sqrt(d))
        
        # Casos
        if d <= n**2:
            print(2 * n - 1)
        elif d <= (n**2 + n):
            print(2 * n)
        else:
            print(2 * n + 1)

if __name__ == "__main__":
    solve()