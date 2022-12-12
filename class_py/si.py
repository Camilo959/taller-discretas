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