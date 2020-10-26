def sanitize(x):
	return x.strip(',;\n ()')

def parser(file_):
	v_file = open(file_, 'r')

	GATES = ['not', 'and', 'or', 'nand', 'nor', 'xor', 'xnor', 'buf']
	input_nodes = []		# all input ports are taken as nodes to visualize better
	output_nodes = []		# all output ports are taken as nodes to visualize better
	gates = []				# nodes
	wires = {}				# [edges][(tail, head)] here the first index is the name of the wire; 
							# tail and head are the nodes to which the edge is connected to

	line = v_file.readline()
	while (line):
		
		# find all the input ports
		if(line.find('input') == 0):
			line = line.split(sep=',')
			line = [x.strip('input,;\n ') for x in line]
			[input_nodes.append(x) for x in line]

		# find all the output ports
		elif(line.find('output') == 0):
			line = line.split(sep=',')
			line = [x.strip('output,;\n ') for x in line]
			[output_nodes.append(x) for x in line]

		# find all the connections and gates
		elif(any(g in line for g in GATES)):

			# remove gate type (gate instantiation) from line
			stri = ''
			line = (line.split(sep=' ', maxsplit=1)[1:])
			line = stri.join(line)

			# extract gate name from line, append to gates and remove from line
			line = line.split('(')
			gate = sanitize(line[0])
			gates.append(gate)
			line = line[1:]

			# extract input and output ports of gate and append wires
			stri = ''
			line = stri.join(line)
			line = [sanitize(x) for x in line.split(',')]
			_output = line[0]
			_input = line[1:]

			print(_output, _input)
			# checking if a wire exists in wires with name _output and adding its edge parameters
			if(_output in output_nodes):
				wires[_output] = (gate, _output)
			else:
				try:
					wires[_output][0] = gate
				except:
					wires[_output] = (gate, ' ')
					# print("test")
			
			for i in _input:
				# print(i, end='')
				if(i in input_nodes):
					wires[i] = (i, gate)
				else:
					try:
						wires[i] = (wires[i][0], gate)
						# print("exists")
					except KeyError:
						wires[i] = (' ', gate)
						# print("does not exist")

			# print()

		line = v_file.readline()

	print("\nINPUT:")
	print(input_nodes)

	print("\nOUTPUT:")
	print(output_nodes)

	print("\nGATES:")
	print(gates)

	print("\nWIRES: ")
	for i in wires:
		print(i, wires[i])

	return input_nodes, output_nodes, gates, wires