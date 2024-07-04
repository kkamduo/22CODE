# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 09:54:54 2022

@author: JSH
"""

import pandas as pd
import cv2
import numpy as np
import os
import re
import time

def is_this_in(ginseng_x, ginseng_y, ginseng_w, ginseng_h, bb_x, bb_y, bb_w, bb_h): # 내공/내백 측정범위 확인 및 분류
    if (ginseng_x <= round((bb_x * 1960) - (bb_w / 0.07201)/2) <= ginseng_x + ginseng_w and
        (ginseng_x <= round((bb_x * 1960) + (bb_w / 0.07201)/2) <= ginseng_x + ginseng_w) and 
        (ginseng_y - 30 <= round((bb_y * 1080) - (bb_h / 0.07201)/2) <= ginseng_y + ginseng_h + 30) and 
        (ginseng_y -30 <= round((bb_y * 1080) + (bb_h / 0.07201)/2) <= ginseng_y + ginseng_h + 30)
        ):
        return True
    else : return False

def detection_error_part(ginseng_x, bb_x, bb_w):
    if ginseng_x +210 <= round((bb_x * 1960) - (bb_w / 0.07201)/2) <= ginseng_x + 350 or \
    ginseng_x + 210 <= round((bb_x * 1960) + (bb_w / 0.07201)/2) <= ginseng_x + 350 or \
    round((bb_x * 1960) - (bb_w / 0.07201)/2) <= ginseng_x +210 <= round((bb_x * 1960) + (bb_w / 0.07201)/2) or \
    round((bb_x * 1960) - (bb_w / 0.07201)/2) <= ginseng_x +350 <= round((bb_x * 1960) + (bb_w / 0.07201)/2):
        return True
    else:
        return False

def classification(e_length,e_width):
    if e_width <= 0.5 and e_length <= 10:
        df_exel.loc[index,'classification'] = "상"
    elif 0.5 < e_width <= 2 and 10 < e_length <= float(df_exel.iloc[2]['Red_ginseng_length(mm)']) / 4 :
        df_exel.loc[index,'classification'] = "중"
    elif e_width <= float(df_exel.iloc[2]['Red_ginseng_width(mm)']) / 3 and e_length <= float(df_exel.iloc[2]['Red_ginseng_length(mm)']) / 2 :
        df_exel.loc[index,'classification'] = "하"
    else:
        df_exel.loc[index,'classification'] = "최하"

start = time.time()

# 라벨경로 지정 및 불러들이기
file_dir = 'C:/Users/User/Desktop/excel2/0726/0726fin/'
file_list = os.listdir(file_dir)

'''
첫번째 작업일때 형식
file_dir = 'C:/Users/User/Desktop/excel2/date/datefin/'

두번째 작업일때 형식
file_dir = 'C:/Users/User/Desktop/excel2/date/re/datefin/'
'''

# 엑셀파일 지정 및 불러들이기
exel_dir = 'C:/Users/User/Desktop/excel2/0726/0726test.xlsx'
df_exel = pd.read_excel(exel_dir)

'''
첫번째 작업일때 형식
file_dir = 'C:/Users/User/Desktop/excel2/date/datetest.xlsx/'

두번째 작업일때 형식
file_dir = 'C:/Users/User/Desktop/excel2/date/re/date/datere.xlsx'
'''

df_img_name = pd.read_excel(exel_dir,usecols=['img_file_name'])
df_img_name = df_img_name.values

df_img_bbox = pd.read_excel(exel_dir, usecols=['bounding_box_ori_x','bounding_box_ori_y'])
df_img_bbox = df_img_bbox.values

# 내공 내백 검출 범위 테스팅
for file_data in file_list:
    file_data_type = re.split(r"[.]",file_data)[-1] #엑셀파일 내에 해당 라벨이 존재하는지 여부 확인을 위한 변수

    if file_data_type != "jpg":
        pass
    
    else:
        file_img_name = file_data
        index = np.where(df_img_name==file_img_name)[0][0]
        test_img = cv2.imread(file_dir + file_data)
        cv2.line(test_img, ( df_exel.iloc[index]['bounding_box_ori_x'] + 210,0), ( df_exel.iloc[index]['bounding_box_ori_x'] + 210, 1960), (0,0,255),10)
        cv2.line(test_img, ( df_exel.iloc[index]['bounding_box_ori_x'] + 350,0), ( df_exel.iloc[index]['bounding_box_ori_x'] + 350, 1960), (0,0,255),10)
        cv2.imwrite(file_dir + file_data,test_img)
        # show_img = cv2.resize(test_img, dsize = (1200,800))
        # cv2.imshow('t',show_img)
        # cv2.waitKey(0)

for file_data in file_list:
    file_data_type = re.split(r"[.]",file_data)[-1] #엑셀파일 내에 해당 라벨이 존재하는지 여부 확인을 위한 변수
    file_data_name = re.split(r"[.]",file_data)[0] + ".jpg"

    if file_data_type != "txt":
        pass

    else :
        if file_data_name in df_img_name:
            label_data = pd.read_table(file_dir+'/'+file_data,sep=' ',header=None)
            index = np.where(df_img_name==file_data_name)[0][0] # 엑셀 파일내 해당 라벨의 인덱싱 찾기
            print(file_data_name,'index is', index)
            info = len(label_data)

            if info == 1: # 라벨정보가 한개일 경우
                CS = label_data[0][0]
                
                if CS == 0: # 라벨 CLS가 0 (내공)일 경우
                    hole_x = label_data[1][0]
                    hole_y = label_data[2][0]
                    hole_h = label_data[4][0]
                    hole_w = label_data[3][0]
                    
                    if is_this_in(
                            df_exel.iloc[index]['bounding_box_ori_x'], df_exel.iloc[index]['bounding_box_ori_y'],
                            df_exel.iloc[index]['bounding_box_width'], df_exel.iloc[index]['bounding_box_height'],
                            hole_x, hole_y, hole_w, hole_h) and \
                        detection_error_part(df_exel.iloc[index]['bounding_box_ori_x'], hole_x, hole_w):
                            df_exel.loc[index,'Inner_hole_width(mm)'] = float(hole_h)
                            df_exel.loc[index,'Inner_hole_length(mm)'] = float(hole_w)
                            classification(hole_w,hole_h)

                elif CS == 1 or CS == 2: # 라벨 CLS가 1 (내백)일 경우
                    white_x = label_data[1][0]
                    white_y = label_data[2][0]
                    white_h = label_data[4][0]
                    white_w = label_data[3][0]
                    
                    if is_this_in(
                            df_exel.iloc[index]['bounding_box_ori_x'], df_exel.iloc[index]['bounding_box_ori_y'],
                            df_exel.iloc[index]['bounding_box_width'], df_exel.iloc[index]['bounding_box_height'],
                            white_x, white_y, white_w, white_h) and \
                        detection_error_part(df_exel.iloc[index]['bounding_box_ori_x'], white_x, white_w):
                            df_exel.loc[index,'Inside_whites_width(mm)'] = float(white_h)
                            df_exel.loc[index,'Inside_whites_length(mm)'] = float(white_w)
                            classification(white_w,white_h)

            elif info >= 2: # 라벨정보가 다수일 경우
                check_data = pd.DataFrame([])
                for i in range(info):
                    if (is_this_in(
                            df_exel.iloc[index]['bounding_box_ori_x'], df_exel.iloc[index]['bounding_box_ori_y'],
                            df_exel.iloc[index]['bounding_box_width'], df_exel.iloc[index]['bounding_box_height'],
                            label_data.iloc[i-1][1], label_data.iloc[i-1][2], label_data.iloc[i-1][3], label_data.iloc[i-1][4]) and
                        detection_error_part(
                        df_exel.iloc[index]['bounding_box_ori_x'], label_data.iloc[i-1][1], label_data.iloc[i-1][3])):
                                
                                check_data = pd.concat([check_data,label_data.iloc[[i-1]]])
                                print(df_exel.iloc[index]['img_file_name'],is_this_in(
                                    df_exel.iloc[index]['bounding_box_ori_x'], df_exel.iloc[index]['bounding_box_ori_y'],
                                    df_exel.iloc[index]['bounding_box_width'], df_exel.iloc[index]['bounding_box_height'],
                                    label_data.iloc[i-1][1], label_data.iloc[i-1][2],
                                    label_data.iloc[i-1][3], label_data.iloc[i-1][4]))
                    i += 1
                    
                if len(check_data)> 0 :
                    tt = max(check_data[:][5])
                    max_index = label_data.loc[label_data[5] == tt].index[0]
                    CS = label_data[0][max_index]
                    
                    if CS == 0: # 라벨 CLS가 0 (내공)일 경우
                        hole_x = label_data[1][max_index]
                        hole_y = label_data[2][max_index]
                        hole_h = label_data[4][max_index]
                        hole_w = label_data[3][max_index]
                        
                        df_exel.loc[index,'Inner_hole_width(mm)'] = float(hole_h)
                        df_exel.loc[index,'Inner_hole_length(mm)'] = float(hole_w)
        
                        classification(hole_w,hole_h)
    
                    elif CS == 1 or CS == 2: # 라벨 CLS가 1 (내백)일 경우
                        white_x = label_data[1][max_index]
                        white_y = label_data[2][max_index]
                        white_h = label_data[4][max_index]
                        white_w = label_data[3][max_index]
                        
                        df_exel.loc[index,'Inside_whites_width(mm)'] = float(white_h)
                        df_exel.loc[index,'Inside_whites_length(mm)'] = float(white_w)
        
                        classification(white_w,white_h)
                
        df_exel.to_excel(exel_dir,index=False) # 엑셀 파일 저장

print("run time :", time.time() - start)