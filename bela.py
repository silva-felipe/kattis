score = {'A': (11, 11), 'K': (4, 4), 'Q': (3, 3), 'J': (20, 2),
         'T': (10, 10), '9': (14, 0), '8': (0, 0), '7': (0, 0)}

plays = input()
hands = int(plays[:-1]) * 4
suit = plays[-1]

pts = 0

for n in range(hands):
    h = input()
    if h[-1] == suit:
        pts += score[h[0]][0]
    elif h[-1] != suit:
        pts += score[h[0]][1]

print(pts)