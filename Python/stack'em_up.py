import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        line = next(it)
        while not line.strip(): line = next(it)
        num_cases = int(line)
        # Saltamos la línea en blanco obligatoria tras el número de casos
        next(it)
    except (StopIteration, ValueError):
        return

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    master_deck = [f"{v} of {s}" for s in suits for v in values]

    for case_idx in range(num_cases):
        try:
            line = next(it)
            while not line.strip(): line = next(it)
            n_shuffles = int(line)
        except (StopIteration, ValueError):
            break
        
        # Leemos los shuffles (asegurando 52 números por cada uno)
        all_shuffles = []
        for _ in range(n_shuffles):
            s = []
            while len(s) < 52:
                s.extend(map(int, next(it).split()))
            all_shuffles.append(s)
        
        current_deck = list(range(1, 53))
        
        # Leemos las instrucciones de barajado (movimientos)
        while True:
            try:
                line = next(it).strip()
                if not line: break # Línea en blanco = fin del caso
                move_idx = int(line) - 1
                
                # Aplicar la permutación
                new_deck = [0] * 52
                for i in range(52):
                    # El número en la posición i del shuffle indica de dónde viene la carta
                    source_pos = all_shuffles[move_idx][i] - 1
                    new_deck[i] = current_deck[source_pos]
                current_deck = new_deck
            except (StopIteration, ValueError):
                break
        
        # Imprimir resultado del caso
        for idx in current_deck:
            print(master_deck[idx - 1])
        
        if case_idx < num_cases - 1:
            print()

if __name__ == "__main__":
    solve()