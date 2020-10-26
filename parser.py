v_file = open("c17.v", 'r')

input_nodes = []
output_nodes = []

line = v_file.readline()
while (line):
	# print(line, end='')
	if(line.find('input') == 0):
		line = line.split(sep=',')
		line = [x.strip('input,;\n ') for x in line]
		[input_nodes.append(x) for x in line]

	elif(line.find('output') == 0):
		line = line.split(sep=',')
		line = [x.strip('output,;\n ') for x in line]
		[output_nodes.append(x) for x in line]

	
	line = ''
	line = v_file.readline()

print(input_nodes)
print(output_nodes)