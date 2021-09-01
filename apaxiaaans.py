nome = input()

nome_certo = ['']

for l in nome:
    if l == nome_certo[-1]:
        pass
    else:
        nome_certo.append(l)

nome_final = ''.join(nome_certo)

print(nome_final)