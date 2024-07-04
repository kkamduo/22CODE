# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:44:52 2022

@author: JSH
"""

import os
import pandas as pd

excel_file = 'C:/Users/User/Desktop/20221130/nas용/0914data.xlsx'

df = pd.read_excel(excel_file)

a  = df[df['classification'] == '하']['img_file_name']
b = a.to_list()