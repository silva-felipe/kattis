c = int(input())

for n in range(c):
    numero = int(input())
    if numero % 2 == 0:
        print(f'{numero} is even')
    elif numero % 2 != 0:
        print(f'{numero} is odd')