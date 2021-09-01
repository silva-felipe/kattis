v = int(input())

for _ in range(v):
    n = input()

    divisao = int(len(n) ** 0.5)
    split_string = []

    msg = []

    for index in range(0,len(n), divisao):
        split_string.append(n[index: index + divisao])

    for p in range(len(split_string)):
        index_invert = p + 1
        for c in split_string:
            # print(c)
            msg.append(c[-index_invert])

    secret_msg = ''.join(msg)

    print(secret_msg)