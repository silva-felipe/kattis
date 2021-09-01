n = int(input())

binary = str(bin(n).split('0b')[-1])
b_inv = []

for b in binary:
    b_inv.insert(0,b)
    bin_str = ''.join(b_inv)

binario_invertido = int(bin_str,2)

print(binario_invertido)