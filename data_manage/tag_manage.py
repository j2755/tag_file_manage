from storage_and_modification import data_management, file_explore, storage
import graph_logic
import os
import pandas as pd


class Tag_manage:
    def __init__(self, directory):
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

    def merge_frames(self, data_frame_list):
        df = pd.concat(data_frame_list)
        return df

    def add_tag_column(self, tag_name):
        self.dm.add_column(tag_name, 0)

    def change_value_of_tag(self, index, column_name, value):
        self.dm.df.at[index, column_name] = value

    def give_list_of_tags(self):
        return self.df.columns
