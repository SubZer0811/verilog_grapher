import networkx as nx
import matplotlib.pyplot as plt
import verilog_parser

''' 
in_n: input nodes; out_n: output nodes; 
nodes: gates; edges; connections
'''
in_n, out_n, nodes, edges = verilog_parser.parser("c17.v")     


G=nx.DiGraph()
G.add_nodes_from(in_n)
G.add_nodes_from(out_n)
G.add_nodes_from(nodes)

for i in edges:
    G.add_edge(*edges[i])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
nx.draw_networkx(G, with_labels=True)
plt.savefig("path_graph1.png")
plt.show()