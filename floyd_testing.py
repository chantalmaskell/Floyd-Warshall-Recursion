# Package imports
import itertools
import sys

# Speed performance testing
import timeit

INF = sys.maxsize

# Imperative function to determine shortest distance between each graph node

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance[0])
    for intermediate, start_node,end_node in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
    # Assume that if start_node and end_node are the same
    # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
            
        # Return all possible paths and find the minimum
    
        distance[start_node][end_node] = min(distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node] )
        
        #Any value that have sys.maxsize has no path
        
# Recursive function to determine shortest distance between each graph node
def floyd_recursive(graph):
    """
    Function for recursive implementation of Floyd Warshall Algorithm
    """
    INF = sys.maxsize
    MAX_LENGTH = len(graph[0])
    
    # Creates a template distance matrix which is the same size as the input graph
    distance = []
    for _ in range(MAX_LENGTH):
        distance.append([INF, INF, INF, INF])
    
    # Replaces the values in distance with the corresponding value in graph
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            distance[start_node][end_node] = graph[start_node][end_node]

    # Checks that new graph (distance) is equal to the original graph (graph)         
    assert distance == graph
    
    # Nested recursive function that enables parent function to call itself
    def update_distances(start_node, end_node, intermediate):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            return
        
        distance[start_node][end_node] = min(distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node] )
        
        # Updates the distance matrix by considering all possible intermediate 
        # vertices between the start node and end node
        if intermediate > MAX_LENGTH-1:
            update_distance(start_node, end_node, intermediate+1)
            update_distance(start_node, intermediate, intermediate+1)
            update_distance(intermediate, end_node, intermediate+1)
    
    # Itertools allows iteration through each node in one line rather than through nested for loops
    # This loop updates the graph to represent distances
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        update_distances(start_node, end_node, intermediate)
        
    return distance


def test_floyd_1():
    """
    Function to check recursive output matches imperative graph
    """
    # Imperative values will replace the values in graph 1
    graph_1 = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]]
    
    floyd(graph_1)

    # Recursive values will output a new graph (graph 2) which will then be used to check against graph 1
    # to confirm values are correct
    graph_2 = [[0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]]
    
    # Assert is used to check graph_2 values match imperative values populated in graph_1
    assert graph_1 == floyd_recursive(graph_2)
    
    
def test_floyd_2():
    # Imperative values will replace the values in graph 1
    graph_3 = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
    
    floyd(graph_3)

    # Recursive values will output a new graph (graph 2) which will then be used to check against graph 1
    # to confirm values are correct
    graph_4 = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
    # Assert is used to check graph_2 values match imperative values populated in graph_1
    assert graph_3 == floyd_recursive(graph_4)
    
def test_floyd_3():
    # Imperative values will replace the values in graph 1
    graph_5 = [[0, 5, INF, INF],
        [50, 0, 15, 5],
        [30, INF, 0, 15],
        [15, INF, 5, 0]
        ]
    
    floyd(graph_5)

    # Recursive values will output a new graph (graph 2) which will then be used to check against graph 1
    # to confirm values are correct
    graph_6 = [[0, 5, INF, INF],
        [50, 0, 15, 5],
        [30, INF, 0, 15],
        [15, INF, 5, 0]
        ]
    # Assert is used to check graph_2 values match imperative values populated in graph_1
    assert graph_5 == floyd_recursive(graph_6)
    

test_floyd_1()
test_floyd_2()
test_floyd_3()

    

