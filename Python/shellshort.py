import sys

def solve():
    # Number of cases
    n_cases = sys.stdin.readline()
    if not n_cases:
        return
    
    n_cases = int(n_cases.strip())
    # Blank
    sys.stdin.readline()

    for case_id in range(n_cases):
        # Number of candidates
        n_candidates =  int(sys.stdin.readline())
                
        # Names of candidates
        origen = []
        target = []
        for _ in range(n_candidates):
            origen.append(sys.stdin.readline().strip())
        for _ in range(n_candidates):
            target.append(sys.stdin.readline().strip())

        while True:
            line = sys.stdin.readline()
            if not line or line.strip() == "":
                break
 
        # 5. Línea en blanco entre casos (regla de UVa)
        if case_id < n_cases - 1:
            print("")

if __name__ == '__main__':
    solve()

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