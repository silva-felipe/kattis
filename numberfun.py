n = int(input())

for l in range(n):
    a, b, c = map(int, input().split())
    if a + b == c or a * b == c or a - b == c or b - a == c or a / b == c or b / a == c:
        print('Possible')
    else:
        print('Impossible')