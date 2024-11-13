import networkx as nx

def create_network(file):

    G = nx.Graph()

    with open(file) as graph_file:

        Lines = graph_file.readlines()
        Head = Lines[0].split()
        Start_Destination = Lines[1].split()
        
        N_Nodes, N_Edges, N_Cards = int(Head[0]), int(Head[1]), int(Head[2])
        Start, Destination = Start_Destination[0], Start_Destination[1]
        
        Nodes_End = N_Nodes + 2
        for N in range(2, Nodes_End):

            Node = Lines[N].split()
            
            if len(Node) == 1: 
                G.add_node(Node[0], color = "black")
            
            else:
                G.add_node(Node[0], color = "red")
        
        
        

        if "->" in Lines[Nodes_End]:
            G.to_directed()
            
        for N in range(Nodes_End, Nodes_End + N_Edges): 

            Edge = Lines[N].split()

            G.add_edge(Edge[0], Edge[2])

        return [G, Start, Destination]