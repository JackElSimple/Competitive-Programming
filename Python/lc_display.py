import sys

def solve():
    # Diccionario que define qué segmentos se activan para cada número (0-9)
    # Orden: [top, mid, bot, up_left, up_right, low_left, low_right]
    digits = {
        '1': [0, 0, 0, 0, 1, 0, 1],
        '2': [1, 1, 1, 0, 1, 1, 0],
        '3': [1, 1, 1, 0, 1, 0, 1],
        '4': [0, 1, 0, 1, 1, 0, 1],
        '5': [1, 1, 1, 1, 0, 0, 1],
        '6': [1, 1, 1, 1, 0, 1, 1],
        '7': [1, 0, 0, 0, 1, 0, 1],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 1, 0, 1],
        '0': [1, 0, 1, 1, 1, 1, 1]
    } # Ej: el número '0' tiene todo activado excepto el segmento medio

    input_data = sys.stdin.read().splitlines()
    
    for line in input_data:
        s_str, n_str = line.split()
        s = int(s_str)
        if s == 0: break
        
        # Cada dígito tiene 2s + 3 filas        
        results = []

        # Fila superior 
        row = []
        for char in n_str:
            comp = '-' if digits[char][0] else ' '
            row.append(' ' + comp * s + ' ')
        results.append(" ".join(row))

        # Filas verticales superiores
        for _ in range(s):
            row = []
            for char in n_str:
                left = '|' if digits[char][3] else ' '
                right = '|' if digits[char][4] else ' '
                row.append(left + ' ' * s + right)
            results.append(" ".join(row))

        # Fila media
        row = []
        for char in n_str:
            comp = '-' if digits[char][1] else ' '
            row.append(' ' + comp * s + ' ')
        results.append(" ".join(row))

        # Filas verticales inferiores
        for _ in range(s):
            row = []
            for char in n_str:
                left = '|' if digits[char][5] else ' '
                right = '|' if digits[char][6] else ' '
                row.append(left + ' ' * s + right)
            results.append(" ".join(row))

        # Fila inferior
        row = []
        for char in n_str:
            comp = '-' if digits[char][2] else ' '
            row.append(' ' + comp * s + ' ')
        results.append(" ".join(row))

        # Imprimir el número completo y una línea en blanco
        print("\n".join(results))
        print()

if __name__ == "__main__":
    solve()