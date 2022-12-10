grafo = ['GDMA', '0   1   1   0   0', 
                 '1   0   0   0   0', 
                 '0   0   0   1   0', 
                 '1   0   0   0   0',    
                 '0   1   1   0   1']

def MA_funtion(graphMI):

    contador = 0
    for i in graphMI:
        for j in i:
            if j == '1':
                contador += 1
    
    print( 'La cantidad de vertices son: ', (len(graphMI) - 1 ) )
    print( 'La cantidad de aristas son : ', contador )

# test 
MA_funtion(grafo)

