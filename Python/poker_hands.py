import sys

def get_value(hand):
    # Asignar valores numéricos a las cartas
    val_map = {str(a): a for a in range(2, 10)}
    val_map.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})
    
    values = sorted([val_map[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    counts = {v: values.count(v) for v in set(values)}
    sorted_counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and (max(values) - min(values) == 4)
    
    # Retornamos una tupla (Ranking_Mano, Valores_para_Desempate)
    if is_straight and is_flush: return (8, values)
    if sorted_counts[0][1] == 4: return (7, [sorted_counts[0][0], sorted_counts[1][0]])
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2: return (6, [sorted_counts[0][0]])
    if is_flush: return (5, values)
    if is_straight: return (4, values)
    if sorted_counts[0][1] == 3: return (3, [sorted_counts[0][0]] + [v for v in values if v != sorted_counts[0][0]])
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        pairs = sorted([sorted_counts[0][0], sorted_counts[1][0]], reverse=True)
        kicker = [v for v in values if v not in pairs]
        return (2, pairs + kicker)
    if sorted_counts[0][1] == 2:
        pair = sorted_counts[0][0]
        kickers = [v for v in values if v != pair]
        return (1, [pair] + kickers)
    return (0, values)

def solve():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line: continue
        cards = line.split()
        black = get_value(cards[:5])
        white = get_value(cards[5:])
        
        if black > white: print("Black wins.")
        elif white > black: print("White wins.")
        else: print("Tie.")

if __name__ == "__main__":
    solve()