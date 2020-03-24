


def make_edge(node_1,node_2):
	return(node_1,node_2)

def make_edge_list(node_list_1,node_list_2):
	edge_list=[]
	for i in range(len(node_list_1)):
		edge_list.append((node_list_1[i],node_list_2[i]))
	return edge_list


def get_neighbors(edge_list,node):
	return [x for x in edge_list if node in x]

