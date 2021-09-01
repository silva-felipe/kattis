t = int(input())

distance = []

walk_total = []

for case in range(t):
    n_stores = int(input())
    l_stores = input().split()
    for s in l_stores:
        distance.append(int(s))
    distance.sort()
    walk = (distance[-1] - distance[0]) * 2
    distance.clear()
    walk_total.append(walk)

for w in walk_total:
    print(w)