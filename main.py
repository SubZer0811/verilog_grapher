from verilog_parser import parser
from grapher import grapher

if __name__ == "__main__":
	
	file_ = "c17.v"
	in_n, out_n, nodes, edges = parser(file_)
	grapher(in_n, out_n, nodes, edges)