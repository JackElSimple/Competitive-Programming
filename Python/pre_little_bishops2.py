import sys

# La misma lógica de backtracking que definimos
def update_matrix(matrix, n, r, c, delta):
    for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nr, nc = r + dr, c + dc
        while 0 <= nr < n and 0 <= nc < n:
            matrix[nr][nc] += delta
            nr += dr
            nc += dc
    matrix[r][c] += delta

def backtrack(n, k, start_pos, k_colocados, matrix):
    if k_colocados == k: return 1
    total = 0
    for i in range(start_pos, n * n):
        r, c = i // n, i % n
        if matrix[r][c] == 0:
            update_matrix(matrix, n, r, c, 1)
            total += backtrack(n, k, i + 1, k_colocados + 1, matrix)
            update_matrix(matrix, n, r, c, -1)
    return total

# Generamos la tabla
results = {}
for n in range(1, 9):
    for k in range(n * n + 1):
        # Optimización: si k > 2n-1, es imposible
        if k > (2 * n - 1):
            results[(n, k)] = 0
        elif k == 0:
            results[(n, k)] = 1
        else:
            matrix = [[0] * n for _ in range(n)]
            results[(n, k)] = backtrack(n, k, 0, 0, matrix)

# ESTO ES LO QUE VAS A COPIAR
print(results)