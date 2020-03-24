from storage_and_modification import data_management, file_explore, storage
import graph_logic
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


class Multi_directory_tag_manager:
	def __init__(self,root_directory):
		self.root=root_directory
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
		tag_manage.add_tag_to_file(index,column,value)
		self.nest_dataframes_in_daughters(directory)
	def add_entry_to_column(self,directory,column,value):
		tag_manage=Tag_manage(directory)
		for i in tag_manage.df.index:
			self.add_entry(directory,i,column,value)