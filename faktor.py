n = input().split()

A, I = int(n[0]), int(n[1])
C = A * I

for p in range(A - 1):
    C -= 1

print(C)