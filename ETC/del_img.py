# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:33:24 2022

@author: JSH
"""

import os
import shutil
import time
import re
import pandas as pd

root_dir = 'C:/Users/User/Desktop/fix_fin_data_ori'  #엑셀파일이 있는 경로

excel_list = []
excel_extension = ['.xlsx'] # 엑셀 확장자 지정

total_cnt = 0
cls_0_cnt = 0
cls_1_cnt = 0
cls_2_cnt = 0
cls_3_cnt = 0

del_list_file = 'C:/Users/User/Desktop/del_list.txt' # 삭제파일 이름저장 파일 경로

df_del = pd.read_csv(del_list_file)
df_del_list = df_del['img_name'].to_list() # 삭제파일 이름 리스트로 저장

for (root, dirs, files) in os.walk(root_dir):
    if len(files) > 0:
        for file_name in files:
            if os.path.splitext(file_name)[1] in excel_extension:
                excel_path = root + '/' + file_name
                
                excel_path = excel_path.replace('\\', '/')
                df = pd.read_excel(excel_path)
                excel_list.append(file_name)
                
                a = df['img_file_name'].to_list() # 엑셀파일에서 file이름을 리스트로 저장
                b = list(set(a) & set(df_del_list)) # 삭제파일 리스트와 엑셀파일file이름의 교집합을 리스트로 저장
                
                old_df = df
                
                for i in b:
                    df = df.append({'img_file_name' : i}, ignore_index = True)
                
                df = df.drop_duplicates(['img_file_name'], keep = False)
                
                total_cnt += len(df)
                cls_0_cnt += len(df.loc[df['classification']=='상'])
                cls_1_cnt += len(df.loc[df['classification']=='중'])
                cls_2_cnt += len(df.loc[df['classification']=='하'])
                cls_3_cnt += len(df.loc[df['classification']=='최하'])
                df.to_excel(excel_path,index=False) # 엑셀 파일 저장

excel_list.sort()