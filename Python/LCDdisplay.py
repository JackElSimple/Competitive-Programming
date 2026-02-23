import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    while input_data[0] != '0 0':
        size = int(input_data[0])
        number = input_data[1]

        print("Size"+size)
        print( "Number:"+ number)
    
        input_data = input_data[2:]

if __name__ == '__main__':
    solve()