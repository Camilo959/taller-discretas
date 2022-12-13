import numpy as np


# Crea una matriz de adyacencia del grafo
adj_matrix = [[0, 1, 1, 0, 0], 
              [1, 0, 0, 0, 0], 
              [0, 0, 0, 1, 0], 
              [1, 0, 0, 0, 0], 
              [0, 1, 1, 0, 1]]

# Obtiene el número de vértices y aristas del grafo
vertices = len(adj_matrix)
edges = 0
for i in range(vertices):
    for j in range(vertices):
        if adj_matrix[i][j] == 1:
            edges += 1

# Crea una matriz de incidencia de tamaño V x E
incidence_matrix = [[0 for i in range(edges)] for j in range(vertices)]

# Recorre las aristas del grafo y marca un 1 en la columla correspondiente a cada arista
# y en la fila correspondiente a cada uno de los vértices que conecta
edge_index = 0
for i in range(vertices):
    for j in range(vertices):
        if adj_matrix[i][j] == 1:
            incidence_matrix[i][edge_index] = 1
            incidence_matrix[j][edge_index] = 1
            edge_index += 1

# Imprime la matriz de incidencia
#print(incidence_matrix)
'''
holis = [[1, 1, 1, 0, 1, 0, 0, 0], 
         [1, 0, 1, 0, 0, 1, 0, 0], 
         [0, 1, 0, 1, 0, 0, 1, 0], 
         [0, 0, 0, 1, 1, 0, 0, 0], 
         [0, 0, 0, 0, 0, 1, 1, 1]
         ]

holis_2 = [[-1, -1, 1, 0, 1, 0, 0, 0], 
           [1, 0, -1, 0, 0, 1, 0, 0], 
           [0, 1, 0, -1, 0, 0, 1, 0], 
           [0, 0, 0, 1, -1, 0, 0, 0], 
           [0, 0, 0, 0, 0, -1, -1, 1]]

def MA_MI(adj_matrix, vertex):

    edges = 0
    for i in range(vertex):
        for j in range(vertex):
            if adj_matrix[i][j] == 1:
                edges += 1
    incidence_matrix = [[0 for i in range(edges)] for j in range(vertex)]

    edge_index = 0
    for i in range(vertex):
        for j in range(vertex):
            if adj_matrix[i][j] == 1:
                incidence_matrix[i][edge_index] = 1
                incidence_matrix[j][edge_index] = 1
                edge_index += 1
    
    return incidence_matrix

adj_matrix_2 = [[0, 1, 1, 0, 0], 
              [1, 0, 0, 0, 0], 
              [0, 0, 0, 1, 0], 
              [1, 0, 0, 0, 0], 
              [0, 1, 1, 0, 1]]

holis = MA_MI(adj_matrix_2, len(adj_matrix_2))
print(holis)

'''

list_inci = [[1, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1]]

vertex = 4
edges = 4

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

           

# Define the edges in the graph
edges = [("A", "B"), ("A", "D"), ("B", "C"), ("C", "D")]

# Get the unique vertices in the graph
vertices = set()
for edge in edges:
    vertices.update(edge)

# Create the incidence matrix
inc_matrix = [[0 for _ in range(len(edges))] for _ in range(len(vertices))]

# Populate the incidence matrix
for col, edge in enumerate(edges):
    for row, vertex in enumerate(vertices):
        if vertex in edge:
            inc_matrix[row][col] = 1

# Print the incidence matrix

print(inc_matrix)


# Importamos la librería numpy

# Definimos nuestra matriz de incidencia como una matriz numpy
incidence_matrix = np.array([
    [1, 1, 1, 0], 
    [1, 0, 0, 0], 
    [0, 1, 0, 1], 
    [0, 0, 1, 1]
])

# Convertimos la matriz de incidencia en una matriz de adyacencia usando la función np.dot
adjacency_matrix = np.dot(incidence_matrix.T, incidence_matrix)

# Mostramos la matriz de adyacencia
print(adjacency_matrix)



matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


mostrar_gui = str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

matriss = []
contado = 0
for i in mostrar_gui:
    if i == ']':
        print('to')
    contado += 1
print(mostrar_gui)