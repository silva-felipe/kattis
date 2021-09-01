a, b = map(str, input().split())

a = int(a[::-1])
b = int(b[::-1])
n = [a,b]

print(max(n))