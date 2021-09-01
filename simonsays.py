c = int(input())

actions = []

sign = 'Simon says'

for comandos in range(c):
    comando = input()
    if sign in comando:
        i = len(sign) + 1
        print(comando[i:])