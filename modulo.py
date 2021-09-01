n = range(10)
d = []

for i in n:
    i = int(input()) % 42
    d.append(i)
print(len(set(d)))