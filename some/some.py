import copy
import networkx

def solve(n: int, m: int, r: int, start: str, terminal: str, vertices: list[str], edges: list[str]):
	"""
	Solves the Some problem of red scare; i.e. is there a simple path from start to terminal that contains a red node

	n = Number of nodes\n
	m = Number of edges\n
	r = Number of red nodes\n
	start = Start node\n
	terminal = End node\n
	vertices = List of vertices\n
	edges = List of edges\n
	"""
	graph = networkx.DiGraph()

	nodes = {}
	red_nodes = [] # We will need a list of all (ingoing)red nodes for our actual algorithm

	for vertex in vertices:
		if vertex.endswith("*"):
			red_nodes.append(vertex.removesuffix(" *"))
			ingoing_red_vertex = vertex.removesuffix(" *")
			nodes[ingoing_red_vertex] = True
		else:
			ingoing_node = vertex
			nodes[ingoing_node] = False

	for vertex, is_red in nodes.items():
		graph.add_node(vertex, red=is_red)
		graph.add_edge(vertex, vertex+"'", directed=True, capacity=1)

	for edge in edges:
		if ' -- ' in edge:
			u, v = edge.strip().split(' -- ')
			graph.add_edge(u+"'", v, directed=True, capacity=1)
			graph.add_edge(v+"'", u, directed=True, capacity=1)
		elif ' -> ' in edge:
			return "?!"

	start_ = start+"_"			# The new Start and Sink, added for network flow
	terminal_ = terminal+"_"	# ^

	graph.add_edge(start+"'", terminal_, directed=True, capacity=1)
	graph.add_edge(terminal+"'", terminal_, directed=True, capacity=1)

	for red_node in red_nodes:
		new_graph = copy.deepcopy(graph)
		new_graph.add_edge(start_, red_node, directed=True, capacity=2)
		new_graph.get_edge_data(red_node, red_node+"'")["capacity"] = 2
		flow = networkx.minimum_cut(new_graph, start_, terminal_)
		if flow[0] == 2:
			return "True"
	return "False"

if __name__ == '__main__':
	path = "./data/wall-z-10000.txt"
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