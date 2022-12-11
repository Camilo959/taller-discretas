class Convertir:

    def __init__(self, list_g, type_graph):
        self.list_g = list_g
        self.type_graph = type_graph
        self.n_vertex = len(list_g)

    # check
    def GDLA_f(self):
        list_adj = {}

        for i in range(self.n_vertex):
            list_adj.setdefault(i + 1, self.list_g[i])

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