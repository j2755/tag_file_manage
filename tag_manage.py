
from storage_and_modification import data_management,file_explore,storage


import os
import pandas as pd
import numpy as np

class Tag__data_initialization:
    def __init__(self, directory):
    	self.directory=directory
    	self.dm = self.create_dataframe_for_entries(directory)
    	self.df = self.dm.df
    	self.save_dataframe()
    def create_dataframe_for_daughters(self, directory):
        home_tag = directory.split('\\')[-1]
        exp = file_explore.Navigator(directory)
        directories = exp.daughters
        dm = data_management.Data_management(directories)
        dm.add_column(home_tag, 1)
        return dm
    def get_entries(self):
    	home_tag = self.directory.split('\\')[-1]
    	exp = file_explore.Navigator(self.directory)
    	directories = exp.entries
    	return directories

    def create_dataframe_for_files(self):
        directories=get_entries()
        dm = data_management.Data_management(directories)
        dm.add_column(home_tag, 1)

        return dm

    def create_dataframe_for_entries(self, directory):
        home_tag = directory.split('\\')[-1]
        exp = file_explore.Navigator(directory)
        directories = exp.entries
        dm = data_management.Data_management(directories)
        dm.add_column(home_tag, 1)
        return dm
    def save_dataframe(self):
    	file_loc=self.directory+r'\data.csv'
    	if not os.path.exists(file_loc):
    		self.df.to_csv(self.directory+r'\data.csv',index_label='files')
    	



class Tag_manage(Tag__data_initialization):
	def __init__(self,directory):
		super().__init__(directory)
		self.home=directory
		self.location=self.home+r'\data.csv'
		self.df=pd.read_csv(self.location,index_col='files')
		self.tags=list(self.df.columns)
		self.index=list(self.df.index)
		self.update_files()

	def add_tag_column(self, tag_name,default_value=np.nan):
		z=self.df.copy()
		z[tag_name]=default_value
		self.update_csv(z)	

	def del_tag_column(self,tag_name):
		try:
			copy=self.df.copy()
			copy.drop([tag_name],axis=1,inplace=True)
			self.update_csv(copy)
			
		except:
			pass
	def get_row(self,index):
		return self.df.loc(index)
	def add_row(self,index_name,tag_data):
		row=pd.DataFrame(tag_data,index=[index_name])
		
		copy=self.df.copy()
		
		bon=pd.concat([copy,row])
		
		self.update_csv(bon)
		

	def update_files(self):
		entries=self.get_entries()
		files=list(self.df.index)
		entries.remove('data.csv')
		
		files_to_add=[x for x in entries if x not in files]
		if files_to_add==[]:
			pass
		for x in files_to_add:
			data=[0]*len(self.df.columns)
			data={self.df.columns[i]:data[i] for i in range(len(self.df.columns))}
			data.update({self.df.columns[0]:1})
			self.add_row(x,data)

	def add_tag_to_file(self, index, column_name, value):
		copy=self.df.copy()
		copy.at[index, column_name] = value
		self.update_csv(copy)

	def give_list_of_tags(self):
		return list(self.df.columns)

	def update_csv(self,dataframe):
		dataframe.to_csv(self.location,index_label='files')
		self.df=pd.read_csv(self.location,index_col='files')
		self.index=list(dataframe.index)
		self.tags=list(dataframe.columns)
	def add_tag_list_to_index_list(self,index_list,column_value_dict):

		for i in index_list:
			for tag,value in column_value_dict.items():
				normalized_tag=tag.lower()
				self.add_tag_to_file(i,normalized_tag,value)


class Multi_directory_tag_manager:

	#very slow to implement and gets slower as new columns are added, not practical in the long term to use as is
	#If i'm going to use it seriously it needs to be optimized
	def __init__(self,root_directory):
		self.root=root_directory
		self.manage=Tag_manage(root_directory)
		self.files=self.manage.index
		self.tags=self.manage.tags
		pass

	def nest_dataframes_in_daughters(self,root_directory):
		
		root=Tag_manage(root_directory)
		immediate_directories= next(os.walk(root_directory))[1]
		for directory in immediate_directories:
			
			try:
				new_df=Tag_manage(root_directory+'\\'+directory)
				for tag in root.tags:
				
					default=root.df.at[directory,tag]
					new_df.add_tag_column(tag,default)
				self.nest_dataframes_in_daughters(root_directory+'\\'+directory)
			except Exception as e:
				continue
			
	def clear_all_datacsv(self):
		files=[]
		for r,x,z in os.walk(self.root):
			for fil in z:
				if 'data.csv'==fil:
					files.append(os.path.join(r,fil))
		for x in files:
			os.remove(x)
	def add_entry(self,directory,index,column,value):
		tag_manage=Tag_manage(directory)
		normalized_tag=column.lower()
		tag_manage.add_tag_to_file(index,normalized_tag,value)
		self.nest_dataframes_in_daughters(directory)
	def add_multiple_tags_to_index(self,directory,index,column_value_dict):
		tag_manage=Tag_manage(directory)
		for tag,value in column_value_dict.items():
			normalized_tag=tag.lower()
			tag_manage.add_tag_to_file(index,tag,value)
		self.nest_dataframes_in_daughters(directory)
	def add_multiple_tags_to_index_list(self,directory,index_list,column_value_dict):
		tag_manage=Tag_manage(directory)
		tag_manage.add_tag_list_to_index_list(index_list,column_value_dict)
		self.nest_dataframes_in_daughters(directory)
	def add_entry_to_column(self,directory,column,value):
		tag_manage=Tag_manage(directory)
		for i in tag_manage.df.index:
			tag_manage.add_tag_column(directory,i,column,value)
		self.nest_dataframes_in_daughters(directory)

	def add_multiple_tag_columns(self,directory,column_value_dict):
		tag_manage=Tag_manage(directory)
		
		for tag,value in column_value_dict.items():
			normalized_tag=tag.lower()
			tag_manage.add_tag_column(tag,value)
		self.nest_dataframes_in_daughters(directory)
	def concat_all_dataframes(self):
		files=[]
		dataframes=[]
		for r,x,z in os.walk(self.root):
			for fil in z:
				if 'data.csv'==fil:
					files.append(os.path.join(r,fil))
		
		for x in files:
			try:
				df=pd.read_csv(x,index_col='files')
				dataframes.append(df)
			except Exception:
				continue
		super_dataframe=pd.concat(dataframes)
		return super_dataframe




class Search_aid:
	def __init__(self,directory):
		self.tm=Tag_manage(directory)
		self.df=self.tm.df
		self.tags=list(self.tm.df.columns)
		self.index=list(self.tm.df.index)
		self.tag_dict=self.give_dict_of_tags_for_all_indeces()


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


