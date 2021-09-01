l = input()
d = input()
x = input()

valores = []
for n in range(int(l),(int(d) + 1)):
    list_of_number = list(map(int, str(n).strip()))
    soma = sum(list_of_number)
    if soma == int(x):
        valores.append(n)

print(valores[0])
print(valores[-1])