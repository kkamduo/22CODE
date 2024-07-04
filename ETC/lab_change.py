# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:19:31 2022

@author: JSH
"""

import pandas as pd
import cv2
import numpy as np
import os
import re
import shutil

file_dir = 'C:/Users/User/Desktop/비둘기/'

file_list = os.listdir(file_dir)

file_list_py = [file for file in file_list if file.endswith('.txt')]

for i in file_list_py :
    if i != 'classes.txt':
        data = pd.read_table(file_dir + i,sep=' ')
        if data.columns[0] != '1' : 
            data.rename(columns = {'0':'1'},inplace=True)
            data.to_csv(file_dir + i ,sep=' ')