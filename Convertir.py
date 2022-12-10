# graph_list = [ 'GDLA', 'GDMA', 'GNLA', 'GNMI', 'GPMA', 'GNMA' ]

# Recibe una matriz

class Convertir: 

    def __init__(self, list_g, type_graph):
        self.list_g = list_g
        self.type_graph = type_graph
        self.n_vertex = len(list_g)

    # check
    def GDLA_f(self):

        list_adj = {}

        for i in range(self.n_vertex):
            list_adj.setdefault(i+1,self.list_g[i])
        
        return list_adj
    
    def GDMA_f(self):
        pass
    
    def GNLA_f(self):
        pass

    def GNMI_f(self):
        pass

    def GPMA_f(self):
        pass

    def GNMA_f(self):
        pass

grafo_2 = [[2, 4], [5], [5, 6], [2], [4], [6]]

objeto = Convertir(grafo_2, 'GDLA')

hola = objeto.GDLA_f()
print(hola)