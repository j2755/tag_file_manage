


def make_edge(node_1,node_2):
	return(node_1,node_2)

def make_edge_list(node_list_1,node_list_2):
	edge_list=[]
	for i in range(len(node_list_1)):
		edge_list.append((node_list_1[i],node_list_2[i]))
	return edge_list




x=[1,2,3,4,5]
y=[4,4,4,4,4]
z=['a','a','a','b','a']
print(make_edge_list(x,y))