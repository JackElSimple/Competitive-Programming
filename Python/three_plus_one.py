import sys

# Aumentar el límite de recursión es vital para números grandes
sys.setrecursionlimit(10000)

# Diccionario global para cachear resultados
memo = {1: 1}

def get_cycle_length(n):
    # Si ya lo calculamos antes, lo devolvemos inmediatamente
    if n in memo:
        return memo[n]
    
    # Aplicamos la regla de la conjetura
    if n % 2 == 0:
        res = 1 + get_cycle_length(n // 2)
    else:
        # Optimización: (3n + 1) siempre es par, así que saltamos un paso
        res = 2 + get_cycle_length((3 * n + 1) // 2)
    
    # Guardamos en el cache y devolvemos
    memo[n] = res
    return res

def solve():
    # Leemos todo el input de una vez y dividimos por cualquier espacio
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    # Usamos ptr + 1 para asegurar que hay una pareja (i, j)
    while ptr + 1 < len(input_data):
        try:
            i_orig = int(input_data[ptr])
            j_orig = int(input_data[ptr + 1])
            ptr += 2
            
            low = min(i_orig, j_orig)
            high = max(i_orig, j_orig)
            
            max_cycle = 0
            
            # Calculamos el ciclo para cada número en el rango
            for n in range(low, high + 1):
                c = get_cycle_length(n)
                if c > max_cycle:
                    max_cycle = c
            
            # Formato exacto requerido por UVa
            print(f"{i_orig} {j_orig} {max_cycle}")
            
        except (IndexError, ValueError):
            break

if __name__ == '__main__':
    solve()