n, k = map(int, input().split())

rates = []

for _ in range(k):
    rates.append(int(input()))

min_rate = (sum(rates) + (n - k) * -3) / n

max_rate = (sum(rates) + (n - k) * 3) / n

print(min_rate, max_rate)