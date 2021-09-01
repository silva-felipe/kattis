plays = str(input())

posicao = 1

for play in plays:
    moves = list(plays)
    if play == 'A' and posicao == 1:
        posicao = 2
    elif play == 'A' and posicao == 2:
        posicao = 1
    elif play == 'B' and posicao == 2:
        posicao = 3
    elif play == 'B' and posicao == 3:
        posicao = 2
    elif play == 'C' and posicao == 1:
        posicao = 3
    elif play == 'C' and posicao == 3:
        posicao = 1

print(posicao)