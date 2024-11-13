import os
from networkx import MultiDiGraph, shortest_path

# Clear the results file
with open('results.txt', 'w') as f:
        f.write('')


files = [file for file in os.listdir('data') if file.endswith('.txt')]

for file in files:
    path = os.path.join('data', file)
    with open(path, 'r') as f:
        n, m, r = [int(x) for x in  f.readline().strip().split()]
        s, t = f.readline().strip().split()
        graph = MultiDiGraph()

        directed = False
        vertices = {}
        for _ in range(n):
            vertex = f.readline().strip()
            if vertex.endswith('*'):
                red_vertex = vertex.removesuffix(' *')
                vertices[red_vertex] = True
            else:
                vertices[vertex] = False

        
        for vertex, red in vertices.items():
            graph.add_node(vertex, red=red)

        for _ in range(m):
            edge = f.readline()
            if ' -- ' in edge:
                u, v = edge.strip().split(' -- ')
                graph.add_edge(u, v, directed=False)
            elif ' -> ' in edge:
                u, v = edge.split(' -> ')
                graph.add_edge(u, v, directed=True)
                directed = True

        if not directed:
            graph = graph.to_undirected()

        # Identify red vertices
        red_vertices = [vertex for vertex, data in graph.nodes(data=True) if data.get('red', True)]

        graph.remove_nodes_from(red_vertices)

    result = ''
    try:
        path = shortest_path(graph, source=s, target=t)
        # Subtract 1 from the number of nodes in the path to get the number of edges
        result = str(len(path) - 1)
        print(result)
    except Exception as e:
        path = "No path"
        result = '-1'
        print(result)
    
    with open('results.txt', 'a') as f:
        f.write(f'{file}: {result} {path}\n')
        

    
    
