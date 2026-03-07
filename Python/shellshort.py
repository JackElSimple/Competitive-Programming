import sys

def solve():
    # Leer todo el input y dividirlo en líneas
    input_data = sys.stdin.read().splitlines()
    
    ptr = 0
    n_cases = int(input_data[ptr])
    ptr += 1

    for case_id in range(n_cases): # Para cada caso
        
        n_turtles =  int(input_data[ptr].strip())
        ptr += 1

        # Leer origen
        origin_indices = {}
        for i in range(n_turtles):
            name = input_data[ptr].strip()
            origin_indices[name] = i # clave: nombre, valor: posición original
            ptr += 1

        # Leer Target 
        target_stack = []
        for _ in range(n_turtles):
            target_stack.append(input_data[ptr].strip())
            ptr += 1

        # indice previo para comparar
        prev_index = n_turtles + 1
        move_from = -1
        for i in range(n_turtles - 1, -1, -1): # Revisar de abajo hacia arriba
            target_turtle = target_stack[i]
            origin_pos = origin_indices[target_turtle]

            if origin_pos < prev_index:
                prev_index = origin_pos
            else:
                move_from = i # si encontramos un número mayor, entonces el movimiento empieza desde aquí
                break   

        # Imprimir desde move_from hasta el final del stack target
        if move_from != -1:
            for i in range(move_from, -1, -1):
                print(target_stack[i])

        # Línea en blanco entre casos
        print("")

if __name__ == '__main__':
    solve()
'''
Origin:                     Target:                  Output:
0. Yertle(0*)               0. Yertle                2->2 Sir Lancelot
1. DukeofEarl(3)            5. Richard M. Nixon      5->1 Richard M. Nixon
2. SirLancelot(2*)          2. Sir Lancelot          0->0 Yertle
3. Elizabeth Windsor(4)     1. Duke of Earl
4. Michael Eisner(5)        3. Elizabeth Windsor
5. Richard M. Nixon(1*)     4. Michael Eisner
6. Mr. Rogers(6)            6. Mr. Rogers
7. Ford Perfect(7)          7. Ford Perfect
8. Mack(8)                  8. Mack            

5 -> 1 : 4
4 -> 5 : -1
3 -> 4 : -1
2 -> 2 : 0
1 -> 3 : -2
0 -> 0 : 0
hashtable dict
asignar target position y nombre y posicion original
revisar diferencia descendente.
8,7,6,4,3,1,* 2,5,0
* aqui el siguiente numero es mayor (2>1): hay que printar 2,5,0 (todos desde ahí)
'''