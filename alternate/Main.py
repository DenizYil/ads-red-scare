import Alternate as A
import Graph_Creation as GC
import networkx as nx


G, s, t = GC.create_network("G-ex.txt")
print(A.find_path_alternate(G, s, t))