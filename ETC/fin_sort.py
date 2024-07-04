# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:48:00 2022

@author: JSH
"""

import os
import shutil
import re
import pandas as pd

# =============================================================================
# def del_file(folder):
#     fol_dict = {'내백' : white_list, '내공' : hole_list}
#     fol_select = fol_dict[folder]
#     return fol_select
# =============================================================================

root_file_dir = 'C:/Users/User/Desktop/fin/20221128/'
root_file_list = os.listdir(root_file_dir)
fin_excel_dir = 'C:/Users/User/Desktop/fin/fin/20221128dat_fin.xlsx'
re_img_list = []


for folder_dir_list in root_file_list:
    if '.xlsx' in folder_dir_list:
        if '~$' not in folder_dir_list:
            excel_dir = root_file_dir + folder_dir_list
            df_excel = pd.read_excel(excel_dir)
            
            # df_excel.loc[df_excel['inner_hole_class'] == df_excel['inside_hole_class'], ]

    elif '내백' in folder_dir_list:
        white_dir = root_file_dir + folder_dir_list + '/'
        white_list = os.listdir(white_dir)

        for white_i, each_white in enumerate(white_list):
            # white_list[white_i] = each_white.replace('_white','')
            (df_excel.loc[df_excel['img_file_name'] == each_white.replace('_white',''), ['inside_whites_length', 'inside_whites_width', 'inside_whites_class']]) = 0
# =============================================================================
#             (df_excel.loc[df_excel['img_file_name'] == each_white.replace('_white',''), ['classification']]) = \
#                 (df_excel.loc[df_excel['img_file_name'] == each_white.replace('_white',''), ['inner_hole_class']])
# =============================================================================

    elif '내공' in folder_dir_list:
        hole_dir = root_file_dir + folder_dir_list + '/'
        hole_list = os.listdir(hole_dir)

        for hole_i, each_hole in enumerate(hole_list):
            # hole_list[hole_i] = each_hole.replace('_holl','')
            (df_excel.loc[df_excel['img_file_name'] == each_hole.replace('_holl',''), ['inner_hole_length', 'inner_hole_width', 'inner_hole_class']]) = 0
# =============================================================================
#             (df_excel.loc[df_excel['img_file_name'] == each_white.replace('_holl',''), ['classification']]) = \
#                 (df_excel.loc[df_excel['img_file_name'] == each_white.replace('_holl',''), ['inner_white_class']])
# =============================================================================

    elif '재검수' in folder_dir_list:
        re_dir = root_file_dir + folder_dir_list + '/'
        re_list = os.listdir(re_dir)
        
        #코드짜는중()
        for each_re in re_list:
            if '_white' in each_re:
                each_re = each_re.replace('_white', '')
                re_img_list.append(each_re)
                
                df_excel.drop(df_excel.loc[df_excel['img_file_name']==each_re].index, inplace=True)

            elif '_holl' in each_re:
                each_re = each_re.replace('_holl', '')
                re_img_list.append(each_re)

                df_excel.drop(df_excel.loc[df_excel['img_file_name']==each_re].index, inplace=True)

df_excel.loc[df_excel['classification'] == df_excel['inside_whites_class'], ['inner_hole_length', 'inner_hole_width', 'inner_hole_class']] = 0
df_excel.loc[df_excel['classification'] == df_excel['inner_hole_class'], ['inside_whites_length', 'inside_whites_width', 'inside_whites_class']] = 0
df_excel.loc[df_excel['inner_hole_class'] > df_excel['inside_whites_class'], ['classification']] = df_excel['inner_hole_class']
df_excel.loc[df_excel['inner_hole_class'] < df_excel['inside_whites_class'], ['classification']] = df_excel['inside_whites_class']

c = df_excel['inner_hole_class'] == 0
d = df_excel['inside_whites_class'] == 0
df_excel.loc[(c&d), ['classification']] = 0
# =============================================================================
# a = df_excel['classification'] != df_excel['inside_whites_class']
# b =  df_excel['classification'] != df_excel['inner_hole_class']
# df_excel.loc[(a ), ['inside_whites_length','inside_whites_width', 'inside_whites_class']] = 0
# =============================================================================
    
# =============================================================================
# c = df_excel['inner_hole_class'] == 0
# d = df_excel['inside_whites_class'] == 0
# 
# df_excel.loc[(c & d) , ['classification']] = df_excel['inside_whites_class']
# =============================================================================

re_img_list = list(set(re_img_list))
df_excel.to_excel(fin_excel_dir,index=False) # 엑셀 파일 저장