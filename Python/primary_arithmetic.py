import sys

def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    
    while True:
        try:
            a_str = next(it)
            b_str = next(it)
        except StopIteration:
            break
            
        if a_str == '0' and b_str == '0':
            break
            
        # Rellenamos con ceros a la izquierda para que tengan el mismo largo
        # Ejemplo: '123' y '594' se quedan igual, pero '1' y '99' -> '01' y '99'
        max_len = max(len(a_str), len(b_str))
        a = a_str.zfill(max_len)
        b = b_str.zfill(max_len)
        
        carries = 0
        current_carry = 0
        
        # Iteramos desde el final (derecha) hacia el principio (izquierda)
        for i in range(max_len - 1, -1, -1):
            digit_a = int(a[i])
            digit_b = int(b[i])
            
            # Sumamos los dígitos más el acarreo anterior
            sum_digits = digit_a + digit_b + current_carry
            
            if sum_digits >= 10:
                carries += 1
                current_carry = 1
            else:
                current_carry = 0
                
        # Formateo de salida
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print("{} carry operations.".format(carries))

if __name__ == '__main__':
    solve()