import networkx

def solve(n, m, r, start, terminal, vertices, edges):
	graph = networkx.DiGraph()

	if not networkx.is_directed(graph):
		raise Exception("This cannot be solved for directed graphs")
	else:
		flow = networkx.minimum_cut(graph)
		if flow == 2:
			return True
		else:
			return False
