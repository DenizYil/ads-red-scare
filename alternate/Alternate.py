import networkx as nx

def solve(n, m, r, s, t, vertices: list[str], edges: list[str]) -> bool:
    if n <= 0 or m <= 0 or s == t:
        return False

    G,s,t = create_network(n, m, r, s, t, vertices, edges)

    return find_path_alternate(G, s, t)

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

def create_network(n, m, r, s, t, vertices: list[str], edges: list[str]):

    G = nx.Graph()
        
    Nodes_End = n + 2
    for vertex_line in vertices:

        Node = vertex_line.split()
        
        if len(Node) == 1: 
            G.add_node(Node[0], color = "black")
        
        else:
            G.add_node(Node[0], color = "red")
    

    if "->" in edges[0]:
        G.to_directed()
        
    for edge in edges: 

        Edge = edge.split()

        G.add_edge(Edge[0], Edge[2])

    return [G, s, t]
