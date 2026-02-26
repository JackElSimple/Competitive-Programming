import math

def solve():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        s = int(math.sqrt(n))
        if s * s == n:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    solve()
