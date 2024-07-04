# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:26:37 2022

@author: JSH
"""

import os
import pandas as pd

lab_dir = 'C:/Users/User/Desktop/내공20_lab/'
fin_dir = 'C:/Users/User/Desktop/20fin'
lab_list = os.listdir(lab_dir)

fin_data = []

for test in lab_list:
    sort_data = []
    test_data = open(lab_dir + test)
    test_txt = test_data.readlines()
    result_data = fin_dir + test
    
    for g_info in test_txt:
        g_info_f = g_info.split('\n')[0]
        g_info_f = g_info_f.split(' ')
        g_info_f = list(filter(None, g_info_f))
        
        sort_data.append(g_info_f)
        
        if g_info_f[0] == '2':
            sort_data.remove(g_info_f)
    
    fin_data.append(sort_data)
    
    test_data.close()
    
    with open(result_data, 'w') as fin_file:
        for fin in sort_data:
            fin_file.write(' '.join(fin) + '\n')