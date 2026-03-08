import sys

def solve():
    # Leemos todas las líneas del archivo
    lines = sys.stdin.readlines()
    
    # Procesamos de dos en dos (par de cadenas)
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break
            
        a = lines[i].strip()
        b = lines[i+1].strip()
        
        # Diccionarios de frecuencia para cada cadena
        count_a = {}
        count_b = {}
        
        for char in a:
            count_a[char] = count_a.get(char, 0) + 1
        for char in b:
            count_b[char] = count_b.get(char, 0) + 1
            
        res = []
        
        # Recorremos el abecedario en orden
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char in count_a and char in count_b:
                # El número de veces que aparece es el mínimo en ambas cadenas
                common_count = min(count_a[char], count_b[char])
                res.append(char * common_count)
        
        # Unimos e imprimimos el resultado alfabético
        print("".join(res))

if __name__ == "__main__":
    solve()