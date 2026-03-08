import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        num_test_cases = int(next(it))
    except StopIteration:
        return
        
    for _ in range(num_test_cases):
        try:
            # 
            # número de parientes
            r = int(next(it))
            # calles
            streets = []
            for _ in range(r):
                streets.append(int(next(it)))
            
            # Ordenar las calles para encontrar la mediana
            streets.sort()
            
            # La mediana es el punto óptimo
            vito_house = streets[r // 2]
            
            # Calcular la suma total de distancias
            total_distance = sum(abs(vito_house - s) for s in streets)
            
            print(total_distance)
            
        except StopIteration:
            break

if __name__ == "__main__":
    solve()