n = input()

t = input().split()

sub_zero = 0
for c in t:
    if int(c) < 0:
        sub_zero += 1

print(sub_zero)