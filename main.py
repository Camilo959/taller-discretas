
# ruta = input('Digite el nombre del archivo: ')

# ruta = 'Grafos\GD-LA-0003-001.txt'

# Grafos\GD-LA-0003-001.txt

'''
    try:
        with open(route, 'r') as f_obj:
            lines = f_obj.readlines()

        return lines
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        exit(0)    
'''

# Variables

route = 'Grafos\GD-LA-0003-001.txt'

# Abrir archivo
def open_file(route):

    with open(route, 'r') as f_obj:
        lines = f_obj.readlines()

    return lines

# Almacenar la información del txt
file_content = open_file(route)

# Extraer la informacion para trabajar con ella 
def clean_content(file_content):
    graph = []
    for i in file_content:
        if not i.startswith('#'):
            
            # i = i.replace('   ',',')
            # i = i.replace('\n','')
            graph.append(i.split())   # grande 
    return graph

new_content = clean_content(file_content)

type_graph = new_content[0]



def graph_representation(type_graph):

    graph_list = [ 'GDLA', 'GDMA', 'GNLA', 'GNMI', 'GPMA', 'GNMA' ]

    if type_graph == graph_list[0]:
        print('Es un grafo: Dirigido Lista de Adyacencia')

    if type_graph == graph_list[1]:
        print('Es un grafo: Dirigido Matriz de Adyacencia')
    if type_graph == graph_list[2]:
        print('Es un grafo: No Dirigido Lista de Adyacencia')
    if type_graph == graph_list[3]:
        print('Es un grafo: No Dirigido Matriz de Incidencia')
    if type_graph == graph_list[4]:
        print('Es un grafo: Ponderado Matriz de Adyacencia')
    if type_graph == graph_list[5]:
        print('Es un grafo: No Dirigido Matriz de Adyacencia')

# Presentar información sobre la cantidad de vértices, aristas y tipo de grafo que es presentado en la interfaz

def graph_info(graph_content):

    num_vertices = len(graph_content) - 1
    print('El numero de vertices es: ', num_vertices)

# A: B
# B: null
# C: A
# D: A C    

# (A -> B)
# (B)
# (C -> A)
# (D -> A) (D -> C)

print(new_content)

graph_representation(type_graph)

graph_info(new_content)



    
        


