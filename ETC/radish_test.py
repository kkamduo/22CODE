# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:02:42 2023

@author: JSH
"""

import os
import shutil
from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

img_dir = 'C:/Users/User/Desktop/radish_Test/20221024_SEED2_GD_02_A_0001.jpg'
test_img = cv2.imread(img_dir)
copy_img = test_img.copy()
# mask_img = np.zeros((test_img[0],test_img[1], dtype = np.int32))
mask_img = np.zeros((4000,3000),dtype = np.uint8)

check_area = []
len_info = []
make_len = []
num_list = []
check_list = []
pop_list = []
fin_list = []
new_cont = []

# 그레이 스케일 및 바이너리 스케일 변환 ---①
gray = cv2.cvtColor(copy_img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for i in contours : 
    if 150000 <cv2.contourArea(i) < 1500000 :
        check_area.append(i)
        cv2.drawContours(copy_img, i, -1, (0,0,255), 2)
        new_cont.append(i)
        
        for j in range(len(i)):
            len_info.append(tuple(i[j,:,:][0]))
            
cv2.fillPoly(mask_img, new_cont, 255)
            
for num, k in enumerate(len_info):
    num_list.append(num)
    check_list.append(k[1])
    make_len.append((k[1],k[0]))

for n , l in enumerate(check_list):
    if check_list.count(l) < 2:
        pop_list.append(make_len[n])

for m in make_len:
    if m not in pop_list:
        fin_list.append(m)

fin_list.sort()
t_start = []
t_start_check = []
fin_start = []
t_end = []
t_end_check = []
fin_end = []
t_pix = []

for cal_num, cal_ele in enumerate(fin_list):
    if cal_num < len(fin_list)-1:
        if cal_ele[0] == fin_list[cal_num+1][0]:
            
            for pix_num in range(cal_ele[1],fin_list[cal_num+1][1]):
                pix_len = 0
                # start_point = []
                # end_point = []
                # pix_len = []
                if mask_img[cal_ele[0],pix_num+1] == 255 and mask_img[cal_ele[0],pix_num-1] == 0:
                    t_start.append([cal_ele[0],pix_num])
                    t_start_check.append(cal_ele[0])
                elif mask_img[cal_ele[0],pix_num+1] == 0 and mask_img[cal_ele[0],pix_num-1] == 255:
                    t_end.append([cal_ele[0],pix_num])
                    t_end_check.append(cal_ele[0])

for fix_start in t_start:
    if fix_start[0] in t_end_check:
        fin_start.append(fix_start)
        
for fix_end in t_end:
    if fix_end[0] in t_start_check:
        fin_end.append(fix_end)
                # t_start.append(start_point)
                # t_end.append(end_point)
                    # cv2.line(copy_img, (cal_ele[1],cal_ele[0]) , (fin_list[cal_num][1],cal_ele[0]), (0,0,255),10)
                    # cv2.line(copy_img, (cal_ele[1],cal_ele[0]) , (cal_ele[1],cal_ele[0]+1), (0,0,255),10)
                    # print(cal_ele[1],pix_num)
                    # if
                    # cv2.circle(copy_img, (pix_num,cal_ele[0]), 10, (0,0,255))

# cv2.line(copy_img, (fin_list[3755][1],fin_list[3755][0]) , (fin_list[3756][1],fin_list[3756][0]), (0,0,255),10)

copy_img = cv2.cvtColor(copy_img, cv2.COLOR_BGR2RGB)
plt.imshow(copy_img)
# plt.imshow(mask_img)
# cv2.imshow('t',copy_img)
# cv2.waitKey(0)