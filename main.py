import argparse
from verilog_parser import parser
from grapher import grapher

if __name__ == "__main__":
	
	cli = argparse.ArgumentParser(description="Convert Gate level verilog to a visualizable graph")
	cli.add_argument('verilog_file', type=str, help="Path to the verilog file")
	cli.add_argument('--verbose', type=bool, default=0, help="Display information about nodes and edges of graph")

	args = cli.parse_args()

	in_n, out_n, nodes, edges = parser(args.verilog_file, verbose=args.verbose)
	grapher(in_n, out_n, nodes, edges, verbose=args.verbose)