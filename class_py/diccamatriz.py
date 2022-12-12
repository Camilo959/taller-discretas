
def diccionario_matriz(adj_list, vertex):
    # Creamos una lista de todos los vértices
    vertices = []
    for vertex in adj_list:
        vertices.append(vertex)
    vertices.sort()

    # Creamos una matriz de adyacencia llena de ceros
    adj_matrix = []
    for i in range(len(vertices)):
        adj_matrix.append([0] * len(vertices))

    # Rellenamos la matriz con la información de la lista de adyacencia
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if vertices[j] in adj_list[vertices[i]]:
                adj_matrix[i][j] = 1

    return adj_matrix

lista = {0: [1, 6, 8], 1: [0, 4, 6, 9], 2: [4, 6], 3: [4, 5, 8], 4: [1, 2, 3, 5, 9], 5: [3, 4], 6: [0, 1, 2], 7: [8, 9], 8: [0, 3, 7], 9: [1, 4, 7]}

hola = diccionario_matriz(lista, 10)

print(hola)