long = input()
names = long.split('-')
short = ''

for name in names:
    short += name[0]

print(short)