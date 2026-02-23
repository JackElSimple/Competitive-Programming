import sys

def solve():
    field_number = 1
    
    # Leemos todas las líneas de la entrada (el .txt que inyectamos)
    input_data = sys.stdin.read().split()
    idx = 0
    
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and m == 0:
            break
        
        # Leemos las n filas del tablero
        grid = []
        for _ in range(n):
            grid.append(list(input_data[idx]))
            idx += 1
            
        # Creamos el tablero de salida
        if field_number > 1:
            print() # Línea en blanco entre campos
            
        print(f"Field #{field_number}:")
        
        for r in range(n):
            row_output = ""
            for c in range(m):
                if grid[r][c] == '*':
                    row_output += '*'
                else:
                    mines = 0
                    # Revisar los 8 vecinos
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                                mines += 1
                    row_output += str(mines)
            print(row_output)
            
        field_number += 1

if __name__ == "__main__":
    solve()