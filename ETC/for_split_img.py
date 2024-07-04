
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:29:01 2022

@author: JSH
"""

import os
import shutil
import random
import re
import pandas as pd

img_root_dir = 'D:/작종'
des_dir = 'D:/split/12월작물'

possible_img_extension = ['.jpg'] # 이미지 확장자들
img_path_list = []
total_user_list = []

info_file_name = 'C:/Users/User/Desktop/cr_name.txt'
info_file_cnt = 'C:/Users/User/Desktop/cr_cnt.txt'

user_name_df = pd.read_csv(info_file_name)
user_name_list = user_name_df['이름'].values.tolist()

user_cnt_df = pd.read_csv(info_file_cnt)
user_cnt_list = user_cnt_df['갯수'].values.tolist()
# user_cnt_list = list(map(int,user_cnt_list))

if not len(user_name_list) == len(user_cnt_list):
    print('Error')
else:
    for (root, dirs, files) in os.walk(img_root_dir):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path = root + '/' + file_name

                    # 경로에서 \를 모두 /로 바꿔줘야함
                    img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
                    img_path_list.append(img_path)

    for i in range(len(user_name_list)):
        print(user_name_list[i])
        split_user_img_list = [user_name_list[i],[random.sample(img_path_list, user_cnt_list[i])]]
        for j in split_user_img_list[1][0]:
            f_name = re.split('/',j)[-1]
            if not os.path.isdir(des_dir + '/' + user_name_list[i]):
                os.mkdir(des_dir + '/' + user_name_list[i])
                shutil.copy(j , des_dir + '/' + user_name_list[i] + '/' + f_name)
            else:
                shutil.copy(j , des_dir + '/' + user_name_list[i] + '/' + f_name)

        total_user_list.append(split_user_img_list)