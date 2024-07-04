# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:56:17 2023

@author: JSH
"""

import os
import shutil
import re

img_dir = 'C:/Users/User/Desktop/bb/검수'
img_extension = ['.jpg']
file_list = []

for (root, dirs, files) in os.walk(img_dir):
    if len(files) > 0:
        for file_name in files:
            if os.path.splitext(file_name)[1] in img_extension:
                excel_path = root + '/' + file_name
                excel_path = excel_path.replace('\\', '/')

                split_name = re.split('[_.]',file_name)[:-2]
                split_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] + '_' + split_name[3] + '_' + split_name[4] + '_' + split_name[5]
                file_name = split_name + '.jpg'
                file_list.append(file_name)
                
#%%
import os
import shutil
import re

def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

img_ori_dir = 'E:/원본/원본이미지'
des_dir = 'C:/Users/User/Desktop/aa/ori_img'
img_extension = ['.jpg']

for (root2, dirs2, files2) in os.walk(img_ori_dir):
    if len(files2) > 0:
        for file_name2 in files2:
            if os.path.splitext(file_name2)[1] in img_extension:
                img_ori_path = root2 + '/' + file_name2
                img_ori_path = img_ori_path.replace('\\', '/')
                
                if file_name2 in file_list:
                    shutil.copy(img_ori_path, des_dir + '/' + file_name2)

                # split_name = re.split('[_.]',file_name)[:-2]
                # split_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] + '_' + split_name[3] + '_' + split_name[4] + '_' + split_name[5]
                # file_name = split_name + '.jpg'
                # file_list.append(file_name)