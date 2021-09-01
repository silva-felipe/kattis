exercises = input()
range_exe = exercises.split(';')

lista_exe = []

for extensao in range_exe:
    if len(extensao) == 1:
        lista_exe.append(extensao)
    elif len(extensao) != 1:
        ex_i_f = extensao.split('-')
        ex_i = int(ex_i_f[0])
        ex_f = int(ex_i_f[-1]) + 1
        for n_ex in range(ex_i,ex_f):
            lista_exe.append(n_ex)

print(int(len(lista_exe)))