
# Python3 program to implement
# the above approach
  
# Function to insert vertices
# to adjacency list
def insert(adj, u, v):
 
    # Insert a vertex v to vertex u
    adj[u].append(v)
    return
 
# Function to display adjacency list
def printList(adj, V):
     
    for i in range(V):
        print(i+1, end = '')
         
        for j in adj[i]:
            print(' --> ' + str(j), end = '')
             
        print()
         
    print()
         
# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):
 
    # Initialize a matrix
    matrix = [[0 for j in range(V)]
                 for i in range(V)]
     
    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1
     
    return matrix
  
# Function to display adjacency matrix
def printMatrix(adj, V):
     
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end = ' ')
             
        print()
         
    print()
         
# Driver code
if __name__=='__main__':
 
    V = 6
  
    adjList = [[] for i in range(V)]
    # adjList = [ [1,6,8], [0,4,6,9], [4,6], [4,5,8], [1,2,3,5,9], [3,4], [0,1,2], [8,9], [0,3,7], [1,4,7]]
    adjList = [[2, 4], [1, 3, 5], [2, 4], [1, 3, 5], [2, 4], [2, 4]]
  
    # Inserting edges
    '''
    insert(adjList, 0, 2)
    insert(adjList, 0, 4)
    insert(adjList, 1, 1)
    insert(adjList, 1, 3)
    insert(adjList, 1, 5)
    insert(adjList, 2, 2)
    insert(adjList, 2, 4)
    insert(adjList, 3, 1)
    insert(adjList, 3, 3)
    insert(adjList, 3, 5)
    insert(adjList, 4, 2)
    insert(adjList, 4, 4)
    insert(adjList, 5, 2)
    insert(adjList, 5, 4)
'''
    print(adjList)
  
    # Display adjacency list
    print("Adjacency List: ")
    printList(adjList, V)
  
    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adjList, V)
  
    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)
  
# This code is contributed by rutvik_56
