game = input()
extra = 7
T, C, G = 0, 0, 0

for l in game:
    if l == 'T':
        T += 1
    elif l == 'C':
        C += 1
    elif l == 'G':
        G += 1

pts = pow(T, 2) + pow(C, 2) + pow(G, 2)

if T == 0 or C == 0 or G == 0:
    print(pts)
else:
    set = []
    set.append(T), set.append(C), set.append(G)
    pts_extra = int(min(set))
    print(pts + pts_extra*extra)