# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:18:32 2022

@author: JSH
"""

import os
import shutil
import time
from datetime import timedelta
import re
import pandas as pd
import threading

def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

def copy_img(img_root_dir,possible_img_extension,excel_file_list,des_dir,check_name_list):
    for (root, dirs, files) in os.walk(img_root_dir):
        if len(files) > 0:
            files.sort()
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path = root + '/' + file_name
    
                    # 경로에서 \를 모두 /로 바꿔줘야함
                    img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
                    img_path_list.append(file_name)
    
                    split_name = re.split('[._]',file_name)
                    check_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] +'.jpg'
                    if check_name not in check_name_list:
                        check_name_list.append(check_name)
                    check_date = split_name[0]
    
                    if check_name in excel_file_list:
                        if os.path.isdir(des_dir + '/' + check_date):
                            shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
                        else:
                            os.makedirs(des_dir + '/' + check_date)
                            shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
                    else:
                        pass
                    
    # return files, img_path_list, img_path, split_name, check_name, check_date

shutil.copyfileobj = _copyfileobj_patched

if __name__ == '__main__':
    start = time.perf_counter()

    img_root_dir = 'Z:/IMG/하이드로봇테크앤리서치/검수이미지/20220808'
    xlsx_root_dir = 'C:/Users/User/Desktop/홍삼납품/test'
    des_dir = 'C:/Users/User/Desktop/move_file_test/1'

    img_path_list = []
    check_name_list = []
    excel_list = []
    excel_file_list = []
    possible_img_extension = ['.jpg'] # 이미지 확장자들
    excel_extension = ['.json'] # 엑셀 확장자 지정

    ## 단일지정 (엑셀파일)
    # =============================================================================
    # excel_file = 'C:/Users/User/Desktop/홍삼납품/홍삼_추가물량_준비.xlsx'
    # df = pd.read_excel(excel_file)
    # 
    # a = df['img_file_name'].to_list() # 엑셀파일에서 file이름을 리스트로 저장
    # =============================================================================

    ## 최상위폴더지정 (엑셀파일)
    for (root, dirs, files) in os.walk(xlsx_root_dir):
        if len(files) > 0:
            for file_name in enumerate(files):
                if os.path.splitext(file_name[1])[1] in excel_extension:
                    excel_path = root + '/' + file_name[1]

                    excel_path = excel_path.replace('\\', '/')
                    df = pd.read_excel(excel_path)
                    excel_list.append(file_name)

                    a = df['img_file_name'].to_list() # 엑셀파일에서 file이름을 리스트로 저장

                    if file_name[0] == 0 :
                        excel_file_list = a
                    if file_name[0] > 0:
                        excel_file_list.extend(a)

    ## 등급 지정파트
    # =============================================================================
    # a  = df[df['classification'] == '하']['img_file_name']
    # b = a.to_list()
    # =============================================================================
    ##
    
    ## 개별폴더 지정 (이미지)
    # =============================================================================
    # # =============================================================================
    # # img_path1 = 'Z:/IMG/하이드로봇테크앤리서치/검수이미지/20221007'
    # # img_path2 = 'Z:/IMG/하이드로봇테크앤리서치/검수이미지/20221015'
    # # img_path3 = 'Z:/IMG/하이드로봇테크앤리서치/검수이미지/20221018'
    # # img_path4 = 'Z:/IMG/하이드로봇테크앤리서치/검수이미지/20221024'
    # # =============================================================================
    # 
    # img_list = os.listdir(img_root_dir)
    # # =============================================================================
    # # img_list.extend(os.listdir(img_path2))
    # # img_list.extend(os.listdir(img_path3))
    # # img_list.extend(os.listdir(img_path4))
    # # =============================================================================
    # 
    # for img_name in img_list:
    #     split_name = re.split('[._]',img_name)
    #     check_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] +'.jpg'
    #     check_date = split_name[0]
    # 
    #     if check_name in excel_file_list:
    #         shutil.copy(str('Z:/IMG/하이드로봇테크앤리서치/검수이미지/' + check_date + '/' + img_name) , des_dir + '/' + img_name)
    #     else:
    #         pass
    # 
    #     img_path_list.sort()
    # =============================================================================
    
    ## 최상위 폴더 지정 (이미지)
    
    # 스레드
    threads = []
    # =============================================================================
    # for _ in range(10):
    #     t = threading.Thread(target=copy_img(img_root_dir, possible_img_extension, excel_file_list, des_dir))
    #     t.start()
    #     threads.append(t)
    # =============================================================================

    copy_img(img_root_dir, possible_img_extension, excel_file_list, des_dir,check_name_list)
    end = time.perf_counter()

    no_img = list(set(excel_file_list) - set(check_name_list))
    no_img.sort()

    print(f'Finished in {round(end-start, 2)} second(s)')

    # =============================================================================
    # for (root, dirs, files) in os.walk(img_root_dir):
    #     if len(files) > 0:
    #         for file_name in files:
    #             if os.path.splitext(file_name)[1] in possible_img_extension:
    #                 img_path = root + '/' + file_name
    # 
    #                 # 경로에서 \를 모두 /로 바꿔줘야함
    #                 img_path = img_path.replace('\\', '/') # \는 \\로 나타내야함
    #                 img_path_list.append(file_name)
    # 
    #                 split_name = re.split('[._]',file_name)
    #                 check_name = split_name[0] + '_' + split_name[1] + '_' + split_name[2] +'.jpg'
    #                 check_date = split_name[0]
    # 
    #                 if check_name in excel_file_list:
    #                     if os.path.isdir(des_dir + '/' + check_date):
    #                         shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
    #                     else:
    #                         os.makedirs(des_dir + '/' + check_date)
    #                         shutil.copy(img_path, des_dir + '/' + check_date + '/' +  file_name)
    #                 else:
    #                     pass
    # 
    # img_path_list.sort()
    # =============================================================================