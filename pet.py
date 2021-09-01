contestants = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}

total_pts_jogadores = []

soma_notas = []

for entry in range(5):
    notas = input().split()
    for nota in notas:
        nota_int = int(nota)
        total_pts_jogadores.append(nota_int)
    soma_notas.append(sum(total_pts_jogadores))
    total_pts_jogadores.clear()

valor_maior = max(soma_notas)

indice = str(soma_notas.index(valor_maior) + 1)

print('{} {}'.format(contestants[indice], valor_maior))