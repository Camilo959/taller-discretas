'''
# Crea la matriz de adyacencia
matriz = [[0, 1, 0, 0],
          [1, 0, 1, 1],
          [0, 1, 0, 0],
          [0, 1, 0, 0]]

# Inicializa la lista de adyacencia
lista = []

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
'''


'''
def matriz_diccionario(list_matrix):

    adj_list = []

    for i in range(len(list_matrix)):
    # Crea una lista para el nodo i
      adj_list.append([])
      # Recorre cada columna de la fila i
      for j in range(len(list_matrix[i])):
          # Si hay una conexión entre los nodos i y j, agrega j a la lista de adyacencia de i
        if list_matrix[i][j] == 1:
          adj_list[i].append(j)

    return adj_list

ejemplo = [[0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
           [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
           [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
           ]

hola = matriz_diccionario(ejemplo)

print(hola)
'''
'''
def listadj_matrixadj(list_adj):

  n = len(list_adj)
  matriz = [[0 for i in range(n)] for j in range(n)]

  # Finalmente, recorremos la lista de adyacencia y rellenamos la matriz de adyacencia
  # con los valores correspondientes:

  for i, vértice in enumerate(list_adj):
    for vecino in list_adj[vértice]:
      matriz[i][vecino] = 1

  return matriz

lista = {0: [1, 2], 1: [0], 2: [3], 3: [0], 4: [1, 2, 4]}

print(listadj_matrixadj(lista))
'''


matriz = [[1, 0, 1, 1, 0], 
          [1, 1, 0, 0, 0], 
          [0, 1, 1, 0, 1], 
          [0, 0, 0, 1, 1]]

n = len(matriz)

matriz_2 = [[0 for i in range(n)] for j in range(n)]

print(n)
print(matriz_2)

for i in range(len(matriz_2)):
  for j in range(len(matriz_2[i])):
    if matriz[i][j] == 1:
      # matriz_2[i][j] = 1
      matriz_2[j][i] = 1
  
print(matriz_2)
# Finalmente, creamos un diccionario que represente la lista de adyacencia del
# grafo y rellenamos los valores correspondientes:

lista = {vértice: [] for vértice in range(n)}

print(lista)
for i, vértice in enumerate(lista):
  for j, vecino in enumerate(lista[vértice]):
    if matriz[i][j] == 1:
      lista.setdefault(0,vecino)


print(lista )


def incidence_to_adjacency(incidence_matrix):
    # Define la matriz de adyacencia como una matriz de ceros del mismo tamaño que la matriz de incidencia
    adjacency_matrix = [[0 for j in range(len(incidence_matrix[0]))] for i in range(len(incidence_matrix))]

    # Recorre la matriz de incidencia
    for i in range(len(incidence_matrix)):
        for j in range(len(incidence_matrix[0])):
            # Si el elemento es uno, asigna el valor uno a la posición correspondiente en la matriz de adyacencia
            if incidence_matrix[i][j] == 1:
                adjacency_matrix[i][j] = 1

    # Devuelve la matriz de adyacencia
    print(adjacency_matrix) 

# Define una matriz de incidencia
matriz_zzz = [[1, 0, 1, 1, 0], 
          [1, 1, 0, 0, 0], 
          [0, 1, 1, 0, 1], 
          [0, 0, 0, 1, 1]]

incidence_to_adjacency(matriz_zzz)
