# Para Lista de Adyacencia 
# https://www.techiedelight.com/es/graph-implementation-python/

import string

def listAlphabet():
  return list(string.ascii_uppercase)

letras = listAlphabet()

print(letras)

n = 4

contenido = ['B', '', 'A', 'A   C']

grafo = []

for i in range(n):

    lista1 = []
    lista1.append(letras[i])
    lista1.append(contenido[i])
    grafo.append(lista1)

print(grafo)