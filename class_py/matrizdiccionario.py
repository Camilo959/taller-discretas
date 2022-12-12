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
