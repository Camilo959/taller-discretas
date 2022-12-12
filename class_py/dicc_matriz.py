# Creamos una lista de adyacencia
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

# Creamos una lista de todos los vértices
vertices = []
for vertex in adj_list:
    vertices.append(vertex)


# Ordenamos la lista de vértices
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

# Mostramos la matriz de adyacencia
# print(adj_matrix)


def LA_MA(adj_list):
    # Creamos una lista de todos los vértices
    vertices = []
    for vertex in adj_list:
        vertices.append(vertex)

    # Ordenamos la lista de vértices
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

   
'''

# Crea la matriz de adyacencia
matriz = [[0, 1, 0, 0],
          [1, 0, 1, 1],
          [0, 1, 0, 0],
          [0, 1, 0, 0]]

# Inicializa la lista de adyacencia
lista = []

# Recorre cada fila de la matriz
for i in range(len(matriz)):
  # Crea una lista para el nodo i
  lista.append([])
  # Recorre cada columna de la fila i
  for j in range(len(matriz[i])):
    # Si hay una conexión entre los nodos i y j, agrega j a la lista de adyacencia de i
    if matriz[i][j] == 1:
      lista[i].append(j)

# Muestra la lista de adyacencia
print(lista)


import numpy as np

# Creamos un grafo con 4 vértices y 3 aristas
vertices = 4
aristas = 3

# Creamos una matriz de incidencia de ceros con 3 filas y 4 columnas
matriz = np.zeros((aristas, vertices))

# Iteramos sobre las filas y las columnas de la matriz de adyacencia
for i in range(vertices):
    for j in range(vertices):
        # Si hay una arista entre los vértices i y j,
        # establecemos un uno en la fila correspondiente
        # de la matriz de incidencia y en las columnas
        # correspondientes que representan a esos dos vértices
        if matriz_adyacencia[i][j] == 1:
            matriz[i][j] = 1
            matriz[j][i] = 1

# La matriz de incidencia quedaría así:
# 1 1 0 0
# 1 0 1 0
# 0 1 0 1
'''