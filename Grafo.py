class Grafo:

    def __init__(self) -> None:
        pass

    def list_adj(self,graph_l):
        
        contador = 0
        for i in graph_l.keys():
            for j in graph_l[i]:
                contador += 1
                
        return len(graph_l), contador

    def matrix_adj(self, graph_a):

        contador = 0
        for i in graph_a:
            for j in i:
                if j == 1:
                    contador += 1

        return len(graph_a), contador

    def matrix_inci(self,graph_i):

        return len(graph_i), len(graph_i[0])