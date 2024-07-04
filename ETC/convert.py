# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:25:13 2022

@author: JSH
"""

import re
import pandas as pd
import os

excel_file = 'C:/Users/User/Desktop/file_name2.xlsx'
excel_data = pd.read_excel(excel_file, 'Sheet1')

excel_list = excel_data.values.tolist()

b = []

for i in excel_list:
    a = re.split('[.,_]',i[0])
    i_2 = a[:-2]
    i_3 = d = i_2[0] + '_' + i_2[1] + '_' + i_2[2] + '.jpg'

    b.append(i_3)
    
file = pd.DataFrame()
file['img_file_name'] = b

file.to_excel('C:/Users/User/Desktop/file_name_end_2.xlsx',index=False)
