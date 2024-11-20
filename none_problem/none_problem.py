from networkx import MultiDiGraph, shortest_path
import os

def solve(n, m, r, s, t, vertices: list[str], edges: list[str]) -> str:
    # print(n, m, r, s, t, vertices, edges)
    graph = MultiDiGraph()

    directed = False
    nodes = {}
    for vertex in vertices:
        if vertex.endswith('*'):
            red_vertex = vertex.removesuffix(' *')
            nodes[red_vertex] = True
        else:
            nodes[vertex] = False

    for vertex, red in nodes.items():
        graph.add_node(vertex, red=red)

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

    # Identify red vertices
    red_vertices = [vertex for vertex, data in graph.nodes(
        data=True) if data.get('red', True)]

    graph.remove_nodes_from(red_vertices)

    result = ''
    try:
        path = shortest_path(graph, source=s, target=t)
        # Subtract 1 from the number of nodes in the path to get the number of edges
        result = str(len(path) - 1)
    except Exception as e:
        result = '-1'

 #   print(result)
    return result


if __name__ == '__main__':
    path = "./data/wall-n-10000.txt"
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
    solve(n, m, r, start, terminal, vertices, edges)