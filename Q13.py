i = int(input(f'Digite o número de linhas da matriz:'))
z = int(input(f'Digite o número de colunas da matriz:'))
matrix = []

for j in range(i):
    c = []
    for k in range(z):
        k = int(input("Escolha um número para posição "+ "[" + str(j) +"]" + "[" + str(k) +"]" + ":"))
        c.append(k)
    print ()
    matrix.append(c)

for l in range(i):
    for m in range(z):
        print (matrix[l][m], end = " ")
    print ()






