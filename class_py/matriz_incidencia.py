graph = ['GNMI', '1   0   1   1   0', '1   1   0   0   0', '0   1   1   0   1', '0   0   0   1   1']

def MI_funtion(graphMA):

    graph_clean = []

    for i in graphMA:
        i = i.replace(' ','')
        graph_clean.append(i)

    cant_vertex = len(graph_clean) - 1
    cant_edge = len(graph_clean[1])
    
    print( 'La cantidad de vertices son: ', cant_vertex)
    print( 'La cantidad de aristas son: ', cant_edge )
    

# test
MI_funtion(graph)



