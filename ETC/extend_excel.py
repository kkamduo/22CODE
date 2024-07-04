# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:56:07 2022

@author: JSH
"""

import os
import re
import pandas as pd

xlsx_root_dir = 'C:/Users/User/Desktop/fix_fin_data_ori'
# standard = pd.read_excel('C:/Users/User/Desktop/fix_fin_data_ori/1202data.xlsx').columns

excel_extension = ['.xlsx'] # 엑셀 확장자 지정
total_excel = []

# 엑셀 붙이기
for (root, dirs, files) in os.walk(xlsx_root_dir):
    if len(files) > 0:
        for file_name in files:
            if os.path.splitext(file_name)[1] in excel_extension:
                excel_path = root + '/' + file_name
                
                excel_path = excel_path.replace('\\', '/')
                df = pd.read_excel(excel_path)
                
                a = df.values.tolist()
                
                total_excel.extend(a)

# =============================================================================
# for (root, dirs, files) in os.walk(xlsx_root_dir):
#     if len(files) > 0:
#         for file_name in files:
#             if os.path.splitext(file_name)[1] in excel_extension:
#                 excel_path = root + '/' + file_name
#                 
#                 excel_path = excel_path.replace('\\', '/')
#                 df_comp = pd.read_excel(excel_path).columns
#                 
#                 if not (standard == df_comp).all():
#                     print(file_name)
# 
# =============================================================================
