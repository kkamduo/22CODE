# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:24:39 2022

@author: JSH
"""

import pandas as pd
import os
import re

file_dir = 'E:/승훈_재확인/'
file_list = os.listdir(file_dir)

file = pd.DataFrame()
file['img_file_name'] = file_list

file.to_excel('C:/Users/User/Desktop/file_name2.xlsx',index=False)

