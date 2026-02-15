import sys

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

        vivos = [True] * n_candidates
        ballots = []
        # Leer boletas hasta encontrar línea vacía o fin del input
        while ptr < len(input_data) and input_data[ptr].strip(): 
            # Convertir a 0-indexed de una vez
            b = [int(x) - 1 for x in input_data[ptr].split()]
            ballots.append(b)
            ptr += 1

        n_voters = len(ballots)
        while True: # Bucle de rondas de conteo
            counts = [0] * n_candidates
            # conteo de votos (primero vivo)
            for b in ballots:
                for choice in b:
                    if vivos[choice]:
                        counts[choice] += 1
                        break
            # Extraer solo los votos de los candidatos que siguen vivos
            current_votes = [counts[i] for i in range(n_candidates) if vivos[i]]
            voto_max = max(current_votes)
            voto_min = min(current_votes)

            # Condición 1: Alguien tiene mayoría absoluta (> 50%)
            if voto_max > n_voters / 2:
                winner_idx = counts.index(voto_max)
                print(names[winner_idx])
                break

            # Condición 2: Empate total entre los que quedan
            if voto_max == voto_min:
                for i in range(n_candidates):
                    if vivos[i]:
                        print(names[i])
                break
                        
            # Condición 3: Eliminar a los que tienen el mínimo de votos
            for i in range(n_candidates):
                if vivos[i] and counts[i] == voto_min:
                    vivos[i] = False

        # 5. Línea en blanco entre casos (regla de UVa)
        if case_id < n_cases - 1:
            print("")

if __name__ == '__main__':
    solve()
