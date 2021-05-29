from node import*
from edge import*

def bellmandFord_algo (departure_node,nodes,edges):
    print("hello world")
    print(nodes)
    distances = {}
    pathes = {}

    for node in nodes:
        distances[node] = 0 if node == departure_node else float('inf')
        pathes[node] = [node]
    n = len(nodes)
    for _ in range(1, n):
        for edge in edges:
            # If it can be relaxed, relax it
            if distances[edge.end_node] > distances[edge.begining_node] + edge.distance:
                distances[edge.end_node] = distances[edge.begining_node] + edge.distance
                pathes[edge.end_node] = pathes[edge.begining_node][:]
                pathes[edge.end_node].append(edge.end_node)

    return pathes

def bellmandFord (departure_node, ending_node, nodes, edges):
    pathes = bellmandFord_algo(departure_node,nodes,edges)
    shortest_path = pathes[ending_node]
    i = 0
    for i in len(shortest_path):
        for edge in edges:
            if(edge.begining_node == shortest_path[i] & edge.end_node == shortest_path[i+1]):
                edge.color = "blue"
                shortest_path[i].color = "blue"
                shortest_path[i+1] = "blue"
                break


#call bellmandFord() instead of bellmandFord_algo()