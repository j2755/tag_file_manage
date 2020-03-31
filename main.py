
import storage_and_modification.data_management
import storage_and_modification.file_explore
import storage_and_modification.storage

import tag_manage

import tkinter as tk


def get_list_of_tags ():  
    directory = directory_entry.get()
    sa=tag_manage.Search_aid(directory)
    
    label1 = tk.Label(root, text= sa.tag_dict)
    canvas1.create_window(200, 230, window=label1)



root=tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()


directory_label=tk.Label(canvas1,text='Directory')
canvas1.create_window(100, 20, window=directory_label)

directory_entry = tk.Entry (root) 
canvas1.create_window(100, 40, window=directory_entry)

button1 = tk.Button(text='Get the Square Root', command=get_list_of_tags())
canvas1.create_window(200, 180, window=button1)

root.mainloop()