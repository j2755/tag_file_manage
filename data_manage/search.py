import pandas as pd
import tag_manage



class Search_aid:
	def __init__(self,directory):
		self.tm=tag_manage.Tag_manage(directory)
		self.df=self.tm.df
		self.tags=list(self.tm.df.columns)
		self.index=list(self.tm.df.index)
		


	def give_list_of_tags_for_index(self,index):
		tag_list=[]
		for tag in self.tags:
			if self.df.loc[index][tag]==1:
				tag_list.append(tag)
		return tag_list


	
	def give_dict_of_tags_for_all_indeces(self):
		entry_dict={}
		for index in self.index:
			entry_dict.update({index:self.give_list_of_tags_for_index(index)})
		return entry_dict

	def format_dict_of_tags(self,dict_of_tags):
		df=pd.DataFrame.from_dict(dict_of_tags,orient='index')
		return df

	