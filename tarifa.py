mb = int(input())

meses_utilizados = int(input())

mb_restante = 0

for i in range(meses_utilizados):
    mb_utilizado = int(input())
    mb_restante += (mb - mb_utilizado)

print(mb + mb_restante)