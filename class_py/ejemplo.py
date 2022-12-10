# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # asigna memoria para la lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph dirigido
        for (src, dest) in edges:
            # asignar nodo en la lista de adyacencia de src a dest
            self.adjList[src].append(dest)
 
 
# Función para imprimir la representación de lista de adyacencia de un graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # imprime el vértice actual y todos sus vértices vecinos
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
 
if __name__ == '__main__':
 
    # Entrada #: aristas en un graph dirigido
    edges = [[0, 1], [1, 2], [2, 0],[2,3] ,[2, 1], [3, 2], [4, 5], [5, 4]]
    # Nº de vértices (etiquetados de 0 a 5)
    n = 6
 
    # construye un graph a partir de una lista dada de aristas
    graph = Graph(edges, n)
 
    # imprime la representación de la lista de adyacencia del graph
    printGraph(graph)
 