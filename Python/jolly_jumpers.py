import sys

def solve():
    # Leemos la entrada estándar línea por línea
    for line in sys.stdin:
        data = list(map(int, line.split()))
        if not data:
            continue
        
        n = data[0]
        sequence = data[1:]
        
        # Si n es 1, es Jolly por definición
        if n == 1:
            print("Jolly")
            continue
            
        # Conjunto para rastrear las diferencias encontradas
        found_diffs = [False] * n
        is_jolly = True
        
        for i in range(n - 1):
            diff = abs(sequence[i] - sequence[i+1])
            
            # La diferencia debe estar entre 1 y n-1
            if 1 <= diff < n:
                found_diffs[diff] = True
            else:
                # Si una diferencia se sale del rango, no puede ser Jolly
                is_jolly = False
                break
        
        # Verificamos si todas las diferencias del 1 al n-1 están marcadas
        if is_jolly:
            for i in range(1, n):
                if not found_diffs[i]:
                    is_jolly = False
                    break
        
        if is_jolly:
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    solve()