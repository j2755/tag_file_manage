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

    	



    def standardize_tag_names(self, tag_name):
        try:
            return tag_name.upper()
        except:
            pass

    def create_dataframe_for_daughters(self, directory):
        home_tag = directory.split('\\')[-1]
        exp = file_explore.Navigator(directory)
        directories = exp.daughters
        dm = data_management.Data_management(directories)
        dm.add_column(home_tag, 1)
        return dm

    def create_dataframe_for_files(self, directory):
        home_tag = directory.split('\\')[-1]
        exp = file_explore.Navigator(directory)
        directories = exp.files
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
    	



class Tag_manage:
	def __init__(self,directory):
		self.home=directory
		self.location=self.home+r'\data.csv'
		self.df=pd.read_csv(self.location,index_col='files')
		self.tags=list(self.df.columns)

	def merge_frames(self, data_frame_list):
		df = pd.concat(data_frame_list)
		return df



	def add_tag_column(self, tag_name,default_value=np.nan):
		copy=self.df.copy()
		copy[tag_name]=default_value
		self.update_csv(copy)
		

	def del_tag_column(self,tag_name):
		try:
			copy=self.df.copy()
			copy.drop([tag_name],axis=1,inplace=True)
			self.update_csv(copy)
			
		except:
			pass

	def add_value(self,data):
		row=pd.DataFrame([data],index=[index_name])
		copy=self.df.copy()
		self.df=pd.concat([row,self.df])


	def add_tag_to_file(self, index, column_name, value):
		copy=self.df.copy()
		copy.at[index, column_name] = value
		self.update_csv(copy)

	def give_list_of_tags(self):
		return self.df.columns

	def update_csv(self,dataframe):
		dataframe.to_csv(self.location)
		self.df=pd.read_csv(self.location,index_col='files')
		self.tags=list(dataframe.columns)


