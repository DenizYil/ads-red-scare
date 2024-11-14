import heapq as hq

IS_RED = "is_red"
EDGES = "edges"


def solve(n, m, r, s, t, vertices: list[str], edges: list[str]) -> str:
    if n <= 0 or m <= 0 or s == t:
        return '-1'

    graph = construct_graph(vertices, edges)

    distances = dict.fromkeys(graph, n + 1)
    distances[s] = graph[s][IS_RED]
    distances = dijkstra(graph, distances, s)
    return distances[t] if distances[t] <= n else '-1'


def construct_graph(vertices, edges):
    graph = {}
    for vertex_line in vertices:
        vertex = vertex_line.split()
        graph[vertex[0]] = {
            IS_RED: int(len(vertex) > 1),
            EDGES: []
        }

    is_directed = True
    first_edge = edges[0].split()
    if first_edge[1] == "--":
        is_directed = False

    for edge in edges:
        current_edge = edge.split()
        create_directed_edge(graph, current_edge[0], current_edge[2])
        if not is_directed:
            create_directed_edge(graph, current_edge[2], current_edge[0])
    return graph


def create_directed_edge(graph, vertex_start, vertex_end):
    graph[vertex_start][EDGES].append(
        (vertex_start, vertex_end, graph[vertex_end][IS_RED]))


def dijkstra(graph, distances, start):
    pq = []
    hq.heappush(pq, (distances[start], start))
    visited = set([])
    while len(pq) > 0:
        current_vertex = hq.heappop(pq)[1]
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for edge in graph[current_vertex][EDGES]:
            new_distance = distances[current_vertex] + edge[2]
            if new_distance < distances[edge[1]]:
                distances[edge[1]] = new_distance
                hq.heappush(pq, (new_distance, edge[1]))
    return distances
