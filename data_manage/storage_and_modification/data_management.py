import pandas as pd
import os
import sys
import numpy as np
#basic data structures for storing and modifying data

class Data_management:
	def __init__(self,index_list,data):
		self.df=pd.DataFrame(data,index=index_list)


	def add_empty_column(self,column_name):
		self.df[column_name]=np.nan

	def add_row(self,index_name,data):
		row=pd.DataFrame([data],index=[index_name])
		self.df=pd.concat([row,self.df])
	def change_value_of_entry(self,index,column_name,value):
		self.df.at[index,column_name]=value


x={'d':[2,2,2,2,2,2],'z':[1,1,11,1,1,1]}
index=['a','c','x','d','g','z']
x=Data_management(index,x)
x.add_empty_column('empty')



temp_name='aamama'
temp_data={'d':3323,'empty':22222}
x.add_row(temp_name,temp_data)
print(x.df)


new_index=['sdf']
new_data={'d':122,'k':311321}

new_df=pd.DataFrame(new_data,index=new_index)
frame=[x.df,new_df]
result=pd.concat(frame)
print(result)