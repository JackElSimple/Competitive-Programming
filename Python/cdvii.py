import sys

def solve():
    # Leemos todo el input y filtramos líneas vacías al inicio y final
    input_data = [line.strip() for line in sys.stdin.readlines()]
    if not input_data:
        return
    
    idx = 0
    try:
        num_cases = int(input_data[idx])
        idx += 1
    except (ValueError, IndexError):
        return
    
    for case_idx in range(num_cases):
        # Saltar líneas en blanco antes de las tarifas
        while idx < len(input_data) and not input_data[idx]:
            idx += 1
            
        if idx >= len(input_data): break
        
        # Leer tarifas (24 enteros)
        fares = list(map(int, input_data[idx].split()))
        idx += 1
        
        # Leer fotos hasta línea en blanco o fin de input
        records = []
        while idx < len(input_data) and input_data[idx]:
            parts = input_data[idx].split()
            if len(parts) < 4: break # Por si acaso
            
            plate = parts[0]
            # Formato mm:dd:hh:mm -> lo convertimos a un objeto comparable
            time_parts = list(map(int, parts[1].split(':')))
            action = parts[2]
            dist = int(parts[3])
            
            records.append({
                'plate': plate,
                'time': time_parts, # [mm, dd, hh, mm]
                'action': action,
                'dist': dist
            })
            idx += 1
        
        # Procesar por vehículo
        vehicles = {}
        for r in records:
            if r['plate'] not in vehicles:
                vehicles[r['plate']] = []
            vehicles[r['plate']].append(r)
            
        # Ordenar placas alfabéticamente
        sorted_plates = sorted(vehicles.keys())
        output_lines = []
        
        for plate in sorted_plates:
            # Ordenar fotos de este vehículo por tiempo cronológico
            v_photos = sorted(vehicles[plate], key=lambda x: x['time'])
            
            total_cents = 0
            has_valid_trip = False
            
            i = 0
            while i < len(v_photos) - 1:
                curr = v_photos[i]
                nxt = v_photos[i+1]
                
                # Regla: Un "enter" seguido inmediatamente por un "exit" del mismo auto
                if curr['action'] == 'enter' and nxt['action'] == 'exit':
                    dist_traveled = abs(nxt['dist'] - curr['dist'])
                    hour_entry = curr['time'][2] # hh
                    
                    # Costo = (kms * tarifa_hora) +$1.00 (tasa de viaje)
                    cost = (dist_traveled * fares[hour_entry]) + 100
                    total_cents += cost
                    has_valid_trip = True
                    i += 2 # Saltar ambos porque ya fueron emparejados
                else:
                    i += 1 # No hay match, pasar al siguiente para intentar emparejarlo
            
            if has_valid_trip:
                # Sumar $2.00 de cargo fijo mensual
                total_dollars = (total_cents + 200) / 100.0
                output_lines.append("{} ${:.2f}".format(plate, total_dollars))
        
        # Imprimir resultados del caso
        for line in output_lines:
            print(line)
            
        # Imprimir línea en blanco entre casos, pero no después del último
        if case_idx < num_cases - 1:
            print()

if __name__ == "__main__":
    solve()