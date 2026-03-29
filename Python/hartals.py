import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    ncases = int(next(it))
    for _ in range(ncases):
        days = int(next(it))
        num_parties = int(next(it))
        h_parameters = [int(next(it)) for _ in range(num_parties)]
        
        lost_days = 0
        # Iteramos desde el día 1 hasta el total de días
        for day in range(1, days + 1):
            # Regla: No hay hartals los viernes (día 6) ni sábados (día 7)
            # En ciclo de 7: viernes es day % 7 == 6, sábado es day % 7 == 0
            if day % 7 == 6 or day % 7 == 0:
                continue
            
            # Verificar si algún partido tiene huelga este día
            for h in h_parameters:
                if day % h == 0:
                    lost_days += 1
                    break # Solo se cuenta una vez por día
        
        print(lost_days)

if __name__ == "__main__":
    solve()