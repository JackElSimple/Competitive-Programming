import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Número de casos
    n_cases = int(input_data[0])
    # Múmeros a procesar
    test_numbers = input_data[1:n_cases + 1]
    
    for p_str in test_numbers:
        p = int(p_str)
        iterations = 0
        
        while True:
            # Revertimos el número convirtiéndolo a string
            reversed_p = int(str(p)[::-1])
            
            # Sumamos el original con su reverso
            p = p + reversed_p
            iterations += 1
            
            # palíndromo?
            result_str = str(p)
            if result_str == result_str[::-1]:
                print("{} {}".format(iterations, p))
                break
            
            if iterations >= 1000:
                break

if __name__ == '__main__':
    solve()