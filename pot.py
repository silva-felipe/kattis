c = input()

soma = 0

for n in range(int(c)):
    v = input()
    base = int(v[:-1])
    power = int(v[-1])
    soma += pow(base, power)

print(soma)