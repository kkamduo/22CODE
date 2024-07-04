# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:21:17 2022

@author: JSH
"""

import pandas as pd
import cv2
import numpy as np
import os
import re
import shutil

file_dir = 'C:/Users/User/Desktop/Label_0808/22'
file_list = os.listdir(file_dir)
des_dir = 'C:/Users/User/Desktop/Label_0808/upload_2'

for i in range(len(file_list)): #len(file_list):
    prev_ori = file_list[i]
    prev_file = re.split(r"[.]",file_list[i])[0]

    if (i+1) != len(file_list):
        next_ori = file_list[i+1]
        next_file = re.split(r"[.]",file_list[i+1])[0]
        if prev_file == next_file :
            print("Find")
            print(prev_ori , next_ori)
            shutil.copy(file_dir + "/" + prev_ori, des_dir + "/" + prev_ori)
            shutil.copy(file_dir + "/" + next_ori, des_dir + "/" + next_ori)
    else:
        next_file = None
        print("Done")

# exel_dir = 'C:/Users/User/Desktop/홍삼_데이터시트_1%.xlsx'
# df_img_name = pd.read_excel(exel_dir,usecols=['img_file_name'])
# df_img_name = df_img_name.values.tolist()
# tt = np.array(df_img_name)