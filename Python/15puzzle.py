import sys

# Posiciones objetivo precomputadas (0 al final en 3,3)
TARGET_POS = {val: ((val-1)//4, (val-1)%4) for val in range(1, 16)}
TARGET_POS[0] = (3, 3)
OPPONENTS = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

def get_manhattan(state_list):
    distance = 0
    for i in range(16):
        val = state_list[i]
        if val != 0:
            tr, tc = TARGET_POS[val]
            distance += abs(i // 4 - tr) + abs(i % 4 - tc)
    return distance

def is_solvable(state_list):
    inversions = 0
    # Solo contamos inversiones de los números (sin el 0)
    flat = [x for x in state_list if x != 0]
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    
    # Hallar la fila del 0 contando desde ABAJO (1 a 4)
    # Índice 0-3 -> Fila 0, Índice 4-7 -> Fila 1...
    idx_cero = state_list.index(0)
    fila_desde_arriba = idx_cero // 4
    fila_desde_abajo = 4 - fila_desde_arriba
    
    # La suma de (inversiones + fila_desde_abajo) debe ser PAR
    return (inversions + fila_desde_abajo) % 2 == 0

def solve():
    raw_input = sys.stdin.read().split()
    if not raw_input:
        return
    
    it = iter(raw_input)
    try:
        num_puzzles = int(next(it))
    except (StopIteration, ValueError):
        return

    for _ in range(num_puzzles):
        state_list = []
        try:
            for _ in range(16):
                state_list.append(int(next(it)))
        except (StopIteration, ValueError):
            break

        if not is_solvable(state_list):
            print("This puzzle is not solvable.")
            continue

        found_flag = [False] # Usamos lista para poder modificarla en dfs
        path = []
        limit = get_manhattan(state_list)
        blank_start = state_list.index(0)

        def dfs(g, b_idx, threshold, prev_move, current_h):
            f = g + current_h
            if f > threshold or f > 50:
                return f
            if current_h == 0:
                found_flag[0] = True
                return -1

            min_threshold = 100
            r, c = b_idx // 4, b_idx % 4
            
            # Movimientos: Up, Down, Left, Right
            for dr, dc, move in [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]:
                if prev_move and move == OPPONENTS[prev_move]:
                    continue
                
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4:
                    new_idx = nr * 4 + nc
                    val = state_list[new_idx]
                    
                    # Manhattan Incremental
                    tr, tc = TARGET_POS[val]
                    old_dist = abs(nr - tr) + abs(nc - tc)
                    new_dist = abs(r - tr) + abs(c - tc)
                    next_h = current_h - old_dist + new_dist
                    
                    # Swap y recursión
                    state_list[b_idx], state_list[new_idx] = state_list[new_idx], state_list[b_idx]
                    path.append(move)
                    
                    res = dfs(g + 1, new_idx, threshold, move, next_h)
                    
                    if res == -1: return -1
                    if res < min_threshold: min_threshold = res
                    
                    # Backtrack
                    path.pop()
                    state_list[b_idx], state_list[new_idx] = state_list[new_idx], state_list[b_idx]
            
            return min_threshold

        # Bucle IDA*
        while limit <= 50:
            t = dfs(0, blank_start, limit, None, limit)
            if found_flag[0]:
                print("".join(path))
                break
            if t > 50:
                break
            limit = t
        
        if not found_flag[0]:
            print("This puzzle is not solvable.")

if __name__ == "__main__":
    solve()