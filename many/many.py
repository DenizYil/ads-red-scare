from networkx import DiGraph, is_directed_acyclic_graph
from collections import defaultdict, deque

def solve(n, m, r, s, t, vertices: list[str], edges: list[str]) -> str:
    graph = DiGraph()

    # Parse nodes and their properties
    nodes = {}
    for vertex in vertices:
        if vertex.endswith('*'):
            red_vertex = vertex.removesuffix(' *')
            nodes[red_vertex] = True
        else:
            nodes[vertex] = False

    for vertex, red in nodes.items():
        graph.add_node(vertex, red=red)

    # Parse edges
    directed = False
    for edge in edges:
        if ' -- ' in edge:
            u, v = edge.strip().split(' -- ')
            graph.add_edge(u, v, directed=False)
        elif ' -> ' in edge:
            u, v = edge.split(' -> ')
            graph.add_edge(u, v, directed=True)
            directed = True

    if not directed:
        graph = graph.to_undirected()

    # only if its DAG
    if not is_directed_acyclic_graph(graph):
        return '?!'

    # BFS
    queue = deque([(s, 0)]) 
    max_red_count = -1
    visited = defaultdict(lambda: -1)
    
    red_nodes = {node for node, red in nodes.items() if red}
    
    while queue:
        node, red_count = queue.popleft()
        
        if red_count <= visited[node]:
            continue
        visited[node] = red_count
        
        for neighbor in graph.neighbors(node):
            if neighbor == t: 
                max_red_count = max(max_red_count, red_count)
            elif neighbor not in {s, t}:
                queue.append((neighbor, red_count + (1 if neighbor in red_nodes else 0)))

    if max_red_count == -1:
        return '-1'
    
    if s in red_nodes:
        max_red_count = max_red_count + 1

    if t in red_nodes:
        max_red_count = max_red_count + 1
    
    return str(max_red_count)



if __name__ == '__main__':
    print("hit here")
    path = "./data/increase-n500-3.txt"
    with open(path) as f:
        lines = f.readlines()

        n, m, r = [int(i) for i in lines[0].split()]
        start, terminal = lines[1].split()

        vertices = []
        edges = []
        for i in range(0, n):
            vertices.append(lines[i + 2].strip())
        for j in range(0, m):
            edges.append(lines[j + n + 2].strip())
	
    print(solve(n, m, r, start, terminal, vertices, edges))
