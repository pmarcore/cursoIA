
a = [[1,-2,5],[5,-3,9],[12,-4,-6]]
b = [[3,3,-1],[7,-12,11],[21,1,0]]


def suma_matrices(m1,m2):
    suma=[]
    for i in range(len(m1)):
        fila=[]
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        suma.append(fila)
    return suma

resultado = suma_matrices(a,b)
print(resultado)
