contenido = ['2   4', '1   3   5', '2   4', '1   3   5', '2   4', '2   4']
s = []
otro_grafo = []

for i in contenido:

    grafo_limpio = []

    for j in i.split():
        try:
            grafo_limpio.append(int(j))
        except ValueError:
            pass

    s.append(grafo_limpio)

print(s)

contador = 1

for x in s:

    for y in x:
        ejemplo = []
        ejemplo.append(contador)
        ejemplo.append(y)

        otro_grafo.append(ejemplo)

    contador += 1

print(otro_grafo)


    
    



