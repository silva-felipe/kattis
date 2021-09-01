n = input()

order = []
for a in range(int(n)):
    v = str(input())
    order.append(v)

order.reverse()

for i in order:
    print(i)