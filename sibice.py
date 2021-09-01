n,w,h = input().split()

d = (int(w)**2 + int(h)**2) ** 0.5

for i in range(int(n)):
    if int(input()) > d:
        print('NE')
    else:
        print('DA')