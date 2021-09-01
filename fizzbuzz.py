ent = input().split()

x = int(ent[0])
y = int(ent[1])
n = int(ent[-1]) + 1

for numero in range(1,n):
    if (numero % x) == 0 and (numero % y) == 0:
        print('FizzBuzz')
    elif (numero % x) == 0:
        print('Fizz')
    elif (numero % y) == 0:
        print('Buzz')
    else:
        print(numero)