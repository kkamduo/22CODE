# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:30:46 2022

@author: JSH
"""

import os
import shutil

file_dir = 'C:/Users/User/Desktop/0819detect'
file_list = os.listdir(file_dir)

ori_dir = 'Z:/IMG/하이드로봇테크앤리서치/redginseng/IMG/20220819'
ori_list = os.listdir(ori_dir)

diff_list = list(set(ori_list).difference(set(file_list)))

for diff_name in diff_list:
    shutil.copy(ori_dir + "/" + diff_name, file_dir + "/" + diff_name)