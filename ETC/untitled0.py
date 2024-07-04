# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:24:10 2023

@author: JSH
"""

import pandas as pd
import os
import re
import shutil
import time

def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

# =============================================================================
# def copy_img(img_root_dir,possible_img_extension,excel_file_list,des_dir,check_name_list):
#     for (root, dirs, files) in os.walk(img_root_dir):
#         if len(files) > 0:
#             files.sort()
#             for file_name in files:
#                 if os.path.splitext(file_name)[1] in possible_img_extension:
#                     if len(file_name) == 29:
#                         img_path = root + '/' + file_name
#         
#                         # 경로에서 \를 모두 /로 바꿔줘야함
#                         img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
#                         img_path_list.append(file_name)
#         
#                         split_name = re.split('[._]',file_name)
#                         check_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] +'.jpg'
#                         if check_name not in check_name_list:
#                             check_name_list.append(check_name)
#                         check_date = split_name[0]
#         
# # =============================================================================
# #                         if check_name in excel_file_list:
# #                             if os.path.isdir(des_dir + '/' + check_date):
# #                                 shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
# #                             else:
# #                                 os.makedirs(des_dir + '/' + check_date)
# #                                 shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
# #                         else:
# #                             pass
# # =============================================================================    
#                     
#     # return files, img_path_list, img_path, split_name, check_name, check_date
# =============================================================================

shutil.copyfileobj = _copyfileobj_patched

start = time.perf_counter()

img_root_dir = 'H:/project_ana'
xlsx_root_dir = 'C:/Users/User/Desktop/2.라벨링데이터'
des_dir = 'C:/Users/User/Desktop/ana_img'

img_path_list = []
check_name_list = []
img_list = []
error_img_list = []
excel_file_list = []
possible_img_extension = ['.jpg'] # 이미지 확장자들
excel_extension = ['.json'] # 엑셀 확장자 지정

for (root, dirs, files) in os.walk(xlsx_root_dir):
    if len(files) > 0:
        for file_name in files:
            if os.path.splitext(file_name)[1] in excel_extension:
                excel_path = root + '/' + file_name
                excel_path = excel_path.replace('\\', '/')

                split_name = re.split('[.]',file_name)[0]
                file_name = split_name + '.jpg'
                img_list.append(file_name)

for (root2, dirs2, files2) in os.walk(img_root_dir):
        print(root2)
        if len(files2) > 0:
            files2.sort()
            for file_name2 in files2:
                if os.path.splitext(file_name2)[1] in possible_img_extension:
                    if len(file_name2) >= 29:
                        img_path = root2 + '/' + file_name2

                        # 경로에서 \를 모두 /로 바꿔줘야함
                        img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
                        img_path_list.append(file_name2)

                        split_name = re.split('[._]',file_name2)
                        check_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] +'.jpg'
                        if check_name not in check_name_list:
                            check_name_list.append(check_name)
                        check_date = split_name[0]

                        try:
                            if check_name in img_list:
                                if os.path.isdir(des_dir + '/' + check_date):
                                    shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name2)
                                else:
                                    os.makedirs(des_dir + '/' + check_date)
                                    shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name2)
                            else:
                                pass
                        except:
                            error_img_list.append(check_name)

end = time.perf_counter()

no_img = list(set(img_list) - set(check_name_list))
no_img.sort()

print(f'Finished in {round(end-start, 2)} second(s)')