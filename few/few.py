import heapq as hq

IS_RED = "is_red"
EDGES = "edges"


def main():
    n, m, r = [int(i) for i in input().split()]
    start, terminal = input().split()

    if n <= 0 or m <= 0 or start == terminal:
        print(-1)
        return

    graph = construct_graph(n, m)

    distances = dict.fromkeys(graph, n + 1)
    distances[start] = graph[start][IS_RED]
    distances = dijkstra(graph, distances, start)
    print(distances[terminal] if distances[terminal] <= n else -1)


def construct_graph(n, m):
    graph = {}
    for i in range(0, n):
        vertex = input().split()
        graph[vertex[0]] = {
            IS_RED: int(len(vertex) > 1),
            EDGES: []
        }

    is_directed = True
    edge = input().split()
    create_directed_edge(graph, edge[0], edge[2])
    if edge[1] == "--":
        is_directed = False
        create_directed_edge(graph, edge[2], edge[0])

    for i in range(0, m - 1):
        edge = input().split()
        create_directed_edge(graph, edge[0], edge[2])
        if not is_directed:
            create_directed_edge(graph, edge[2], edge[0])
    return graph


def create_directed_edge(graph, vertex_start, vertex_end):
    graph[vertex_start][EDGES].append((vertex_start, vertex_end, graph[vertex_end][IS_RED]))


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


if __name__ == "__main__":
    main()