import networkx as nx
import matplotlib.pyplot as plt
import verilog_parser

''' 
in_n: input nodes; out_n: output nodes; 
nodes: gates; edges; connections
'''

def grapher(in_n, out_n, nodes, edges):

	# in_n, out_n, nodes, edges = verilog_parser.parser(file_)     

	G=nx.DiGraph()
	G.add_nodes_from(in_n, node_color="r")
	G.add_nodes_from(out_n)
	G.add_nodes_from(nodes)

	colour_map = []
	size = []
	line_size = []
	for node in G:
		if node in in_n:
			colour_map.append('red')
		elif node in out_n:
			colour_map.append('green')
		else:
			colour_map.append('blue')
		size.append(100*len(node))

	for i in edges:
		for j in i[2]:
			G.add_edge(i[1], j, weight=6)
			# line_size.append(3)

	nx.draw(G, with_labels=True, node_color=colour_map, node_size=size, arrowsize=20, pos=nx.spring_layout(G, k=7))
	# plt.savefig("path_graph1.png")
	plt.show()