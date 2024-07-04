# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:13:32 2022

@author: JSH
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

img_file = 'C:/Users/User/Desktop/inner_hole_data/20220826_Xray_000008.jpg'
img = cv2.imread(img_file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread(img_file)
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

contour_list = []
cir_list = []
test_img = np.array([[]])
test_img2 = np.array([[]])

# ============================================================================= 19일
for img_range in range(0,1960,1):
    new_img_line = np.array([])
    img_gray_line = img_gray[0:1080,img_range]

    img_gray_line_sort = np.array([each for each in img_gray_line if (50< each <230)])
    img_gray_mean = img_gray_line_sort.mean()

    if img_gray_mean > 0 :
        sort_min = min(img_gray_line_sort)
        sort_min_index = np.argmin(img_gray_line_sort)
        sort_max = max(img_gray_line_sort)
        sort_max_index = np.argmax(img_gray_line_sort)
        index_range = abs(sort_max_index - sort_min_index)

        test_a = (img_gray_mean - sort_min)
        test_b = (sort_max - img_gray_mean)
        test_c = int((test_a + test_b)/2)

# =============================================================================
#         if index_range > 0 :
#             val = (test_c/index_range) * 5
#         else:
#             val = 0
# =============================================================================

        for line in img_gray_line:
            if line > test_c or line < 50 or line > 230:
                line = 0
            else:
                line = 255
            new_img_line = np.append(new_img_line, line)
            new_img_line = np.array([new_img_line])

        if test_img.size == 0:
            test_img = new_img_line
        else:
            test_img = np.append(test_img, new_img_line, axis = 0)
    else :
        if test_img.size == 0:
            test_img = np.zeros((1,1080))
        else:
            test_img = np.append(test_img , np.zeros((1,1080)), axis = 0)

test_img = np.uint8(test_img.T)

# 20일 test
# =============================================================================
# for img_range in range(0,1960):
#     new_img_line = np.array([])
#     img_gray_line = img_gray[0:1080, img_range]
#     
#     img_gray_line_sort = np.array([each for each in img_gray_line if (50< each <230)])
#     img_gray_mean = img_gray_line_sort.mean()
#     index = np.where( np.logical_and(50< img_gray_line, img_gray_line < 230))[0]
# 
#     if img_gray_mean > 0:
# # =============================================================================
# #         for i in range(len(img_gray_line_sort)):
# #             if i < 5 :
# #                 avg = img_gray_line_sort[:5].mean()
# #                 diff = max(img_gray_line_sort[:5]) - min(img_gray_line_sort[:5])                
# #                 # print(avg)
# #             elif i > len(img_gray_line_sort)- 5:
# #                 avg = img_gray_line_sort[-5:].mean()
# #                 diff = max(img_gray_line_sort[-5:]) - min(img_gray_line_sort[-5:])
# #                 # print(avg)
# #             else :
# #                 avg = img_gray_line_sort[i-2:i+2].mean()
# #                 diff = max(img_gray_line_sort[i-5:i+5]) - min(img_gray_line_sort[i-5:i+5])
# #                 # print(avg)
# # =============================================================================
#         for i in index:
#             if i > 10:
#                 avg = img_gray_line[i-5:i+5].mean()
#                 diff = max(img_gray_line[i-5:i+5]) - min(img_gray_line[i-5:i+5])
#                 diff2 = max(img_gray_line[i-5:i+5]) - avg
#                 diff3 = avg - min(img_gray_line[i-5:i+5])
#                 
#         for line in img_gray_line:
#                 # if not(avg - int(diff*0.5) <= line <= avg + int(diff*0.5)) or line >230:
# # =============================================================================
# #                 if diff > 5:
# #                     if line > avg or line < 50 or line >230:
# #                         line = 0
# #                 else : 
# #                     if line < 50 or line > 230:
# #                         line = 0
# # =============================================================================
#                 if not(avg - diff/2 < line < avg + diff/2) or line < 50 or line > 230:
#                     line = 0
# 
#                 new_img_line= np.append(new_img_line, line)
#                 new_img_line = np.array([new_img_line])
#                 
#         if test_img.size == 0:
#             test_img = new_img_line
#         else:
#             test_img = np.append(test_img, new_img_line, axis = 0)
#     else :
#         if test_img.size == 0:
#             test_img = np.zeros((1,1080))
#         else:
#             test_img = np.append(test_img , np.zeros((1,1080)), axis = 0)
# =============================================================================

##21일 test
for img_range in range(0,1960):
    new_img_line2 = np.array([])
    img_gray_line2 = img_gray2[0:1080,img_range]

    img_gray_line_sort2 = np.array([each for each in img_gray_line2 if (50< each <230)])
    img_gray_mean2 = img_gray_line_sort2.mean()

    a = np.gradient(img_gray_line2)
    b = np.gradient(a)

    mean_gra = b.mean()
    max_gra = max(b)
    min_gra = min(b)
    
    ## 10.25 test
# =============================================================================
#     for i, line in enumerate(img_gray_line2):
#         if abs(b[i]) < 3:
#             line = 0
#         else:
#             line = 255
#         
#         new_img_line2 = np.append(new_img_line2,line)
#         new_img_line2 = np.array([new_img_line2])
#         
#     if test_img2.size == 0:
#             test_img2 = new_img_line2
#     else:
#         test_img2 = np.append(test_img2, new_img_line2, axis = 0)
# =============================================================================
    if img_gray_mean2 > 0:

        for i, line in enumerate(img_gray_line2):
            if line < 50 or line > 230 or abs(b[i]) > 3 :
                line = 0
            else:
                line = 255
            new_img_line2 = np.append(new_img_line2, line)
            new_img_line2 = np.array([new_img_line2])

        if test_img2.size == 0:
            test_img2 = new_img_line2
        else:
            test_img2 = np.append(test_img2, new_img_line2, axis = 0)
    else :
        if test_img2.size == 0:
            test_img2 = np.zeros((1,1080))
        else:
            test_img2 = np.append(test_img2 , np.zeros((1,1080)), axis = 0)
    ##

# =============================================================================
#     index_gra = np.where(np.logical_or( max_gra/2 < b , min_gra/ 2 > b))[0]
# 
#     for gra in index_gra:
#         img_gray_line2[gra - 1 : gra + 1] = 0
# 
#     if img_gray_mean2 > 0:
#         for line in img_gray_line2:
#             if line < 50 or line > 230:
#                 line = 0
#             else:
#                 line = 255
#             new_img_line2 = np.append(new_img_line2, line)
#             new_img_line2 = np.array([new_img_line2])
# 
#         if test_img2.size == 0:
#             test_img2 = new_img_line2
#         else:
#             test_img2 = np.append(test_img2, new_img_line2, axis = 0)
#     else :
#         if test_img2.size == 0:
#             test_img2 = np.zeros((1,1080))
#         else:
#             test_img2 = np.append(test_img2 , np.zeros((1,1080)), axis = 0)
# =============================================================================

test_img2 = np.uint8(test_img2.T)
test_img3 = ~(~test_img + ~test_img2)
# test_img = np.uint8(test_img)

# =============================================================================
# test_img_2 = np.array([[]])
# 
# for img_range in range(0,1080,1):
#     new_img_line = np.array([])
#     img_gray_line = img_gray[img_range,0:1960]
#     
#     img_gray_line_sort = [each for each in img_gray_line if each > 60]
#     img_gray_line_sort = np.array(img_gray_line_sort)
#     img_gray_mean = img_gray_line_sort.mean()
#     
#     #test
#     for line in img_gray_line:
#         if line > img_gray_mean -10 or line < 60 or line > 200 :
#             line = 0
#         new_img_line = np.append(new_img_line, line)
#         new_img_line = np.array([new_img_line])
# 
#     if test_img_2.size == 0:
#         test_img_2 = new_img_line
#     else:
#         test_img_2 = np.append(test_img_2, new_img_line, axis = 0)
# =============================================================================

# tt = cv2.resize(test_img ,dsize= (1200,800))
# cv2.imshow('test',tt)
# cv2.waitKey()