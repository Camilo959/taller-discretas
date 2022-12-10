import numpy as np

class Limpiar:

    def __init__(self, contenido) -> None:
        self.contenido = contenido

    def for_matrix(self):

        s = []
        for i in self.contenido:

            grafo_limpio = []

            for j in i.split():
                try:
                    grafo_limpio.append(int(j))
                except ValueError:
                    pass

            s.append(grafo_limpio)
        
        return s


contenido = [ '2   4', '5', '5   6', '2', '4', '6']
# contenido = ['0   1   1   0   0', '1   0   0   0   0', '0   0   0   1   0', '1   0   0   0   0', '0   1   1   0   1']
grafo_2 = [[2, 4], [5], [5, 6], [2], [4], [6]]
obj = Limpiar(contenido)

c = [['0', '1', '1', '0', '0'], ['1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0'], ['1', '0', '0', '0', '0'], ['0', '1', '1', '0', '1']]

d = [['B'], [], ['A'], ['A', 'C']]


a=['1','2','3','4']
b = []
hola = obj.for_matrix()
# print(hola)

print(hola)