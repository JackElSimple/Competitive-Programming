import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n_cases = int(input_data[0])

    for i in range(1, n_cases + 1):
        n = int(input_data[i])
        n2 = n * n
        n3 = n2 * n
        n4 = n3 * n
        res = (n4 - 6*n3 + 23*n2 - 18*n + 24) // 24
        print(res)

if __name__ == '__main__':
    solve()
