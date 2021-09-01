p = int(input())

second_stopped = []
index = 1
total_sec_mostrados = 0

for _ in range(p):
    t = int(input())
    second_stopped.append(t)

if p % 2 == 0:
    for _ in range(int(len(second_stopped)/2)):
        p = second_stopped[index] - second_stopped[index-1]
        total_sec_mostrados += p
        index += 2
    print(total_sec_mostrados)
else:
    print('still running')