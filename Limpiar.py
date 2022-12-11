class Limpiar:

    def _init_(self) -> None:
        pass

    def clean_content(self, contenido):
        graph = []
        for i in contenido:
            if not i.startswith('#'):
                graph.append(i.split())
        return graph

    def for_matrix(self, contenido):
        grafo_4 = []
        for i in contenido:
            grafo_4.append([int(x) for x in i])
        return grafo_4