import networkx as nx

def alternate(Graph):

    Nodes = nx.get_node_attributes(Graph, 'color')
    
    for Node_1, Node_2 in list(Graph.edges()):
    
        if Nodes[Node_2] == 'red' and Nodes[Node_1] == 'red':
        
            Graph.remove_edge(Node_1, Node_2)
            
        elif Nodes[Node_2] == 'black' and Nodes[Node_1] == 'black':
        
            Graph.remove_edge(Node_1, Node_2)
            
    return Graph
    
def find_path(Graph, Start, Destination):

    try: 
        shortest_path = nx.shortest_path(Graph, Start, Destination)
        
    except:
        return False
        
    return True
    
def find_path_alternate(Graph, Start, Destination):
    
    G = alternate(Graph)
    
    return find_path(G, Start, Destination)