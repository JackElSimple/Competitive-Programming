    carmichael_numbers = []

    for linea in raw_data.strip().split('\n'):
        partes = linea.split()
        if len(partes) == 2:
            carmichael_numbers.append(int(partes[1]))

    while True:
        n = int(input())
        if n == 0:
            break
        if n in carmichael_numbers:
            print("The number {} is a Carmichael number.".format(n))
        else:
            print("{} is normal.".format(n))