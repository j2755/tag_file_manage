import pandas as pd
import os
import sys
import numpy as np
#basic data structures for storing and modifying data

class Data_management:
	def __init__(self,index_list,data=[]):
		self.df=pd.DataFrame(data,index=index_list)


	def add_column(self,column_name,default_value=np.nan):
		self.df[column_name]=default_value

	def add_row(self,index_name,data):
		row=pd.DataFrame([data],index=[index_name])
		self.df=pd.concat([row,self.df])

