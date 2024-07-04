# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:14:58 2023

@author: JSH
"""

import pandas as pd
import os
import re
import shutil
import time

json_root = 'C:/Users/User/Desktop/test'
des_dir = 'C:/Users/User/Desktop/output'

start = time.perf_counter()

output_list = []
output_list2 = []
json_list = []
max_size = 0

for (root, dirs, files) in os.walk(json_root):
    root = root.replace('\\', '/')
    crop_cls = re.split('/', root)
    
    if max_size < len(crop_cls) : 
        max_size = len(crop_cls)
        
    print(root,crop_cls,max_size)

    if len(files) > 0:
        # root_path = root.replace('\\', '/')
        # crop_cls = re.split('/', root_path)[-1]
        
        for file_name in files:
            if os.path.isdir(des_dir + '/' + crop_cls[max_size - 2]):
                pass
            else:
                os.makedirs(des_dir + '/' + crop_cls[max_size - 2])
                
            if os.path.splitext(file_name)[1] in '.json':
                json_path = root + '/' + file_name
                json_path = json_path.replace('\\', '/')
                
                test_cls = re.split('/', json_path)
                
                if json_list == []:
                    if os.path.isdir(des_dir + '/'  + test_cls[max_size - 2]  + '/' + test_cls[max_size - 1]):
                        df = pd.read_json(json_path)
                        img_file_name = df['images']['img_file_name'] + '.jpg'
                        bbox_info = df['annotations']['bbox']
                        output_info = [img_file_name,bbox_info]
                        output_list.append(output_info)
                    else:
                        os.makedirs(des_dir + '/' + test_cls[max_size - 2] + '/' + test_cls[max_size - 1])
                        df = pd.read_json(json_path)
                        img_file_name = df['images']['img_file_name'] + '.jpg'
                        bbox_info = df['annotations']['bbox']
                        output_info = [img_file_name,bbox_info]
                        output_list.append(output_info)
                else:
                    if re.split('/',json_list[-1])[-2] != test_cls[-2]:
                        if os.path.isdir(des_dir + '/'  + test_cls[max_size - 2]  + '/' + test_cls[max_size - 1]):
                            df = pd.read_json(json_path)
                            img_file_name = df['images']['img_file_name'] + '.jpg'
                            bbox_info = df['annotations']['bbox']
                            output_info = [img_file_name,bbox_info]
                            output_list2.append(output_info)
                        else:
                            os.makedirs(des_dir + '/' + test_cls[max_size - 2] + '/' + test_cls[max_size - 1])
                            df = pd.read_json(json_path)
                            img_file_name = df['images']['img_file_name'] + '.jpg'
                            bbox_info = df['annotations']['bbox']
                            output_info = [img_file_name,bbox_info]
                            output_list2.append(output_info)
                
            json_list.append(json_path)
# =============================================================================
#                 if re.split('/',json_list[-1])[-2] == test_cls[-2]:
#                     if os.path.isdir(des_dir + '/'  + test_cls[max_size - 2]  + '/' + test_cls[max_size - 1]):
#                         df = pd.read_json(json_path)
#                         img_file_name = df['images']['img_file_name'] + '.jpg'
#                         bbox_info = df['annotations']['bbox']
#                         output_info = [img_file_name,bbox_info]
#                         output_list.append(output_info)
#                     else:
#                         os.makedirs(des_dir + '/' + test_cls[max_size - 2] + '/' + test_cls[max_size - 1])
#                         df = pd.read_json(json_path)
#                         img_file_name = df['images']['img_file_name'] + '.jpg'
#                         bbox_info = df['annotations']['bbox']
#                         output_info = [img_file_name,bbox_info]
#                         output_list.append(output_info)
#                 else : 
#                     if re.split('/',json_list[-1])[-2] == test_cls[-2]:
#                         if os.path.isdir(des_dir + '/'  + test_cls[max_size - 2]  + '/' + test_cls[max_size - 1]):
#                             df = pd.read_json(json_path)
#                             img_file_name = df['images']['img_file_name'] + '.jpg'
#                             bbox_info = df['annotations']['bbox']
#                             output_info = [img_file_name,bbox_info]
#                             output_list2.append(output_info)
#                         else:
#                             os.makedirs(des_dir + '/' + test_cls[max_size - 2] + '/' + test_cls[max_size - 1])
#                             df = pd.read_json(json_path)
#                             img_file_name = df['images']['img_file_name'] + '.jpg'
#                             bbox_info = df['annotations']['bbox']
#                             output_info = [img_file_name,bbox_info]
#                             output_list2.append(output_info)
# =============================================================================

# =============================================================================
#                 if os.path.isdir(des_dir + '/' + crop_cls[0]):
#                     pass
#                 else:
#                     os.makedirs(des_dir + '/' + crop_cls[0])
#                     
#                 if os.path.isdir(des_dir + '/' + crop_cls[0] + '/' + crop_cls[1]):
#                     df = pd.read_json(json_path)
#                     img_file_name = df['images']['img_file_name'] + '.jpg'
#                     bbox_info = df['annotations']['bbox']
#                     output_info = [img_file_name,bbox_info]
#                     output_list.append(output_info)
# 
#                     output_df = pd.DataFrame(output_list,columns=['img_file_name','bbox'])
#                     output_df.to_excel(des_dir + '/' + crop_cls[0] + '/' + crop_cls[1] + '/outdata.xlsx')
#                     
#                 else:
#                     os.makedirs(des_dir + '/' + crop_cls[0] + '/' + crop_cls[1])
# 
#                     df = pd.read_json(json_path)
#                     img_file_name = df['images']['img_file_name'] + '.jpg'
#                     bbox_info = df['annotations']['bbox']
#                     output_info = [img_file_name,bbox_info]
#                     output_list.append(output_info)
# 
#                     output_df = pd.DataFrame(output_list,columns=['img_file_name','bbox'])
#                     output_df.to_excel(des_dir + '/' + crop_cls[0] + '/' + crop_cls[1] + '/outdata.xlsx')
# =============================================================================
                
end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} second(s)')