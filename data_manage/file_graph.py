import networkx
import tag_manage
import pickle
import pandas as pd
def get_file_tag_edges_list(dataframe):
	index_list=list(dataframe.index)
	column_list=list(dataframe.columns.values)
	edges=[]
	for index in index_list:

		for column in column_list:
			
			if dataframe.at[index,column].any()==1:
				edges.append((index,column))
	return edges


class customGraph:
	def __init__(self,edge_list):
		self.edges=edge_list


def make_graph_from_edges(edge_list):
	graph=networkx.Graph()
	for edge in edge_list:
		x,y=edge

		if  (x.endswith('.jpg')or x.endswith('.png')) or (y.endswith('.jpg')or y.endswith('.png')):
			continue
		else:
			graph.add_edge(*edge)
	return graph

z=tag_manage.Multi_directory_tag_manager(r'D:\references\human creative\doujin\Andou Hiroyuki')
df=z.concat_all_dataframes()
edges=get_file_tag_edges_list(df)
print(edges)
g=make_graph_from_edges(edges)
print(g['BN_Training'])