from Lectura import Lectura

class Limpiar:

    def __init__(self):
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
            try:
                grafo_4.append([int(x) for x in i])
            except ValueError:
                try:
                    grafo_4.append([float(x) for x in i])
                except ValueError:
                    grafo_4.append([str(x) for x in i])
        return grafo_4
        
    '''
    def for_matrix(self, contenido):
        s = []
        for i in contenido:
            grafo_limpio = []
            for j in i.split():
                try:
                    grafo_limpio.append(int(j))
                except ValueError:
                    pass
            s.append(grafo_limpio)
        return s
    '''

route = 'Grafos\GD-LA-0003-003.txt'
file = Lectura()
content = file.read(route)

obj = Limpiar()
hola_2 = obj.clean_content(content)
hola_2.pop(0)

print(obj.for_matrix(hola_2))