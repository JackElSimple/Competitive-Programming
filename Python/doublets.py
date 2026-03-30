import sys
from collections import deque

def get_path(start, end, dictionary):
    if start == end:
        return [start]
    if len(start) != len(end):
        return None
        
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        # Generar variaciones de la palabra actual
        for i in range(len(current)):
            original_char = current[i]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original_char:
                    continue
                
                next_word = current[:i] + c + current[i+1:]
                
                if next_word == end:
                    return path + [next_word]
                
                if next_word in dictionary and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, path + [next_word]))
    return None

def solve():
    # Leer todo el input de golpe para procesar rápido
    input_data = sys.stdin.read().splitlines()
    
    dictionary = set()
    idx = 0
    
    # 1. Cargar diccionario hasta la primera línea vacía
    while idx < len(input_data) and input_data[idx].strip() != "":
        dictionary.add(input_data[idx].strip())
        idx += 1
    
    # Saltar la línea vacía
    idx += 1
    
    first_case = True
    
    # 2. Procesar pares de palabras
    while idx < len(input_data):
        line = input_data[idx].strip()
        if not line:
            idx += 1
            continue
            
        parts = line.split()
        if len(parts) != 2:
            idx += 1
            continue
            
        start_w, end_w = parts
        
        # Formato de salida: Línea en blanco ENTRE casos, no al final
        if not first_case:
            print()
        first_case = False
        
        result = get_path(start_w, end_w, dictionary)
        
        if result:
            print("\n".join(result))
        else:
            print("No solution.")
            
        idx += 1

if __name__ == "__main__":
    solve()