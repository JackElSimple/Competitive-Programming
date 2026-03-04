def main(): 
    N=8
    for t in range(1, N+1):
        counter = 0
        matrix = [[0]*(t) for _ in range(t)]
        print("Tablero de {t}x{t}:".format(t=t))
        print(matrix)
        
        A = []  # estados activos backtracking
        A.append(matrix) # estado inicial, tablero vacío

        while A:
            matrix = A.pop()
            explorar(matrix)

            for i in range(t):
                for j in range(t):
                    if matrix[i][j] == 0: # si la casilla está vacía
                        matrix[i][j] = 1 # colocar alfil
                    counter += 1


        while True:
            # colocar alfil en casilla vacía

            # counter += 1
            # sumar 1 a las diagonales

            break

if __name__ == "__main__":
    main()

# numero maximo de permutaciones de K alfiles en un tablero NxN 

# Otra forma de crear la matriz:
#m = []
#for i in range(9):
#    m.append([0]*9)