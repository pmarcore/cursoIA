notas_alumnos = {
    "Pablo": 8.0,
    "Pedro":  7.5
}

with open("diccionario.txt", "w") as notas:
    for nombre, nota in notas_alumnos.items():
        notas.write("%s %f\n" %(nombre, nota))




