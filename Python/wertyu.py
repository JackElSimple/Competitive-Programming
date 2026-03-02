import sys

def solve():
    # Definimos las filas del teclado QWERTY tal cual aparecen
    keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
    
    # Creamos un diccionario de traducción: cada tecla apunta a la de su izquierda
    # Ejemplo: 'W': 'Q', 'S': 'A', etc.
    decode_map = {}
    for i in range(1, len(keyboard)):
        decode_map[keyboard[i]] = keyboard[i-1]
    
    # añadimos manualmente el espacio
    decode_map[' '] = ' '

    # Leemos línea por línea hasta EOF
    for line in sys.stdin:
        translated_line = ""
        for char in line:
            if char in decode_map:
                translated_line += decode_map[char]
            else:
                # Si es un salto de línea (\n) u otro caracter no mapeado, lo dejamos igual
                translated_line += char
        
        # Imprimimos la línea traducida (usamos end="" porque la línea ya trae su \n)
        print(translated_line, end="")

if __name__ == '__main__':
    solve()