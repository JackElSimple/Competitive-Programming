import sys

def permutacions(lst):
    return 0

def solve():
    # Number of cases
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    ptr = 0
    n_cases = int(input_data[ptr])
    ptr += 1

    for case_id in range(n_cases): # Para cada caso
        # recorrer líneas vacías
        while ptr < len(input_data) and not input_data[ptr].strip(): 
            ptr += 1

        n_candidates =  int(input_data[ptr])
        ptr += 1

        names = []
        for _ in range(n_candidates):
            names.append(input_data[ptr])
            ptr += 1

   
        # Línea en blanco entre casos
        if case_id < n_cases - 1:
            print("")

if __name__ == '__main__':
    solve()
