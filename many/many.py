from networkx import MultiDiGraph, all_simple_paths, is_directed_acyclic_graph


def solve(n, m, r, s, t, vertices: list[str], edges: list[str]) -> str:
    graph = MultiDiGraph()

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
        return '-1'

    try:
        paths = list(all_simple_paths(graph, source=s, target=t))
    except Exception:
        return '-1'

    max_red_count = -1

    for path in paths:
        red_count = sum(
            1 for node in path[1:-1] if graph.nodes[node].get('red', False)
        )
        max_red_count = max(max_red_count, red_count)

    return str(max_red_count)
