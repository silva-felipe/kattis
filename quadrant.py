x = int(input())
y = int(input())

coord = (x, y)

if coord[0] > 0 and coord[1] > 0:
    print('1')
if coord[0] < 0 < coord[1]:
    print('2')
elif coord[0] < 0 and coord[1] < 0:
    print('3')
elif coord[0] > 0 > coord[1]:
    print('4')