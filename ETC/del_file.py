# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 17:38:57 2022

@author: JSH
"""

import pandas as pd
import os
import shutil

##
df_name = 'C:/Users/User/Desktop/del.xlsx'
df = pd.read_excel(df_name)

df_img = df["a"]
df_json = df["b"]

dir_list = []

##

file_dir = 'C:/Users/User/Desktop/a/1.Dataset/'
file_list = os.listdir(file_dir)

del_fol = []

for i in file_list:
    dir_list.append(file_dir+i+'/')

dir_list_list = []

for j in dir_list:
    dir_list_list.append(os.listdir(j))
    for t in dir_list_list:
        for y in t:
            del_fol.append(j+y)
    
del_fol_fin = list(set(del_fol))

##
del_img = list(df_img)
del_json = list(df_json)

for del_num_1 in range(len(del_img)):
    # for del_folder in del_fol_fin:
    print(del_fol_fin[0].index(del_img[del_num_1]))