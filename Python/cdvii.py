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
        names = []
        for _ in range(n_candidates):
            names.append(sys.stdin.readline().strip())
        
        # Ballots: leer hasta línea vacía o fin de archivo
        ballots = []
        while True:
            line = sys.stdin.readline()
            if not line or line.strip() == "":
                break
            # Convertir a enteros y restar 1 para usar índices 0..n-1
            ballot = [int(x) - 1 for x in line.split()]
            ballots.append(ballot)
        print("ballots: ",ballots)
        counts = [0] * n_candidates
        n_voters = len(ballots[0])
        for ballot in ballots:
            counts[ballot[0]] += 1
        print("counts: ",counts)
        mayoria


        # 5. Línea en blanco entre casos (regla de UVa)
        if case_id < n_cases - 1:
            print("")

if __name__ == '__main__':
    solve()

 Each ”enter” record is paired with the chronologically next record for the same
vehicle provided it is an ”exit” record. ”enter” records that are not paired with an ”exit” record are
ignored, as are ”exit” records not paired with an ”enter” record.
tarifa unica por viaje de un vehiculo
si tiene solo Enter o solo Exit no se hace print(bill)