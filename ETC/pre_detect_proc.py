import os
import pandas as pd
import cv2
import shutil
# =================================== 변수설명====================================================================================#
# ginseng_x = ginseg_x_start_point / ginseng_y = ginseg_y_start_point / ginseng_w = ginseg_x_length / ginseng_h = ginseg_y_length#
# bb_x = bb_x_start_point / bb_y = bb_y_start_point / bb_w = bb_x_length / bb_h = bb_y_length                                    #
# ===============================================================================================================================#

# 내공/내백이 홍삼 내에 속하는지 확인
def is_this_in(ginseng_x, ginseng_y, ginseng_w, ginseng_h, bb_x, bb_y, bb_w, bb_h): 
    if (ginseng_x <= round((bb_x * 1960) - (bb_w / 0.07141)/2) <= ginseng_x + ginseng_w and
        (ginseng_x <= round((bb_x * 1960) + (bb_w / 0.07141)/2) <= ginseng_x + ginseng_w) and 
        (ginseng_y - 30 <= round((bb_y * 1080) - (bb_h / 0.07141)/2) <= ginseng_y + ginseng_h + 30) and 
        (ginseng_y -30 <= round((bb_y * 1080) + (bb_h / 0.07141)/2) <= ginseng_y + ginseng_h + 30)
        ):
        return True
    else : 
        return False

# 내공/내백이 15mm~25mm 사이에 있는지 확인
def detection_error_part(ginseng_x, bb_x, bb_w): 
    if ginseng_x +210 <= round((bb_x * 1960) - (bb_w / 0.07141)/2) <= ginseng_x + 350 or \
    ginseng_x + 210 <= round((bb_x * 1960) + (bb_w / 0.07141)/2) <= ginseng_x + 350 or \
    round((bb_x * 1960) - (bb_w / 0.07141)/2) <= ginseng_x +210 <= round((bb_x * 1960) + (bb_w / 0.07141)/2) or \
    round((bb_x * 1960) - (bb_w / 0.07141)/2) <= ginseng_x +350 <= round((bb_x * 1960) + (bb_w / 0.07141)/2):
        return True
    else:
        return False

## 파일 불러오기
ginseng = open('C:/Users/User/Desktop/1007_lab_test/info.txt')
label_dir = 'C:/Users/User/Desktop/1007_lab_test/test_label/'
img_dir = 'C:/Users/User/Desktop/1007_lab_test/test_img/'
label_list = os.listdir(label_dir)

out_fin_data = 'C:/Users/User/Desktop/1007_lab_test/test_data.dat'

label_name = []
for label_name_ind in label_list:
    label_name.append(label_name_ind.split('.')[0])

# [20220707_003009.jpg] info
# ginseng_x = 562 
# ginseng_y = 599
# ginseng_w = 692 
# ginseng_h = 174

##메모장 읽어들이기 1
ginseng_ori = ginseng.readlines()

##데이터 집어넣을 빈 리스트
g_info_t = []
fin_data = []
img = []

for ginseng_info in ginseng_ori:
    # 홍삼 이미지 이름에 맞는 길이,폭 정보 가져오기
    g_info = ginseng_info.split('\n')[0]
    g_info = g_info.split(' ')
    g_info = list(filter(None, g_info))

# =============================================================================
#     test_img_file = cv2.imread(img_dir + g_info[0])
#     if os.path.isfile(img_dir + g_info[0]):
#         cv2.line(test_img_file, (int(g_info[3]) + 210,0), (int(g_info[3]) + 210, 1960), (0,0,255),10)
#         cv2.line(test_img_file, (int(g_info[3]) + 350,0), (int(g_info[3]) + 350, 1960), (0,0,255),10)
#         cv2.imwrite(img_dir + 'l_' + g_info[0] ,test_img_file)
# =============================================================================
    # g_info_t.append(g_info)

    # print(g_info[0], g_info[0].split('.')[0] in label_name)
    # 해당 홍삼이미지에 해당하는 내공/내백 검출이 있는지 확인후 필요값 변수에 저장하기

    if g_info[0].split('.')[0] in label_name :
        g_info_t.append(g_info)
        # ginseng_x , ginseng_y , ginseng_w, ginseng_h = g_info[3], g_info[4], g_info[5], g_info[6]
        gin = [float(g_info[3]), float(g_info[4]), float(g_info[5]), float(g_info[6])]
        
        file = open(label_dir + g_info[0].split('.')[0] + '.txt')
        string_ori = file.readlines()
        # file_info = []

        ## 최후미에 있는 '\n'을 제거 및 내공/내백 결과값 저장 및 검출범위에 속하는지 확인
        for string in string_ori:
            info = string.split('\n')[0]
            info = info.split(' ')
            info.insert(0, g_info[0])
            test_img = [info, is_this_in(gin[0],gin[1],gin[2],gin[3], float(info[2]), float(info[3]), float(info[4]), float(info[5])) ,
                             detection_error_part(gin[0], float(info[2]), float(info[4]))]
            ## 검출에 타당한 정보만 img 리스트에 넣기
            if test_img[1] and test_img[2] :
                img.append(test_img[:-2])

                if len(img) > 1:
                    max_area = max(float(l[0][6]) for l in img)
                    
                    for re_l in img:
                        if re_l[0][6] != max_area:
                            img.remove(re_l)
                # 최종 출력 데이터 형식 만들기
        fin_img = [img[0][0][0], img[0][0][1], str(int((float(img[0][0][2])*1960) - (float(img[0][0][4])/0.0714)/2)), 
                                               str(int((float(img[0][0][3])*1080) - (float(img[0][0][5])/0.0714)/2)), 
                                        str(int(float(img[0][0][4])/0.0714)), str(int(float(img[0][0][5])/0.0714))]
        fin_data.append(fin_img)

        file.close()

# 중복데이터 삭제
fin_data_sort = []

for x in fin_data:
    if x not in fin_data_sort:
        fin_data_sort.append(x)

# fin_data = set(fin_data)
with open(out_fin_data, 'w') as fin_file:
    for fin in fin_data_sort:
        fin_file.write(' '.join(fin) + '\n')

# =============================================================================
# oriimg_dir = 'Z:/IMG/하이드로봇테크앤리서치/redginseng/IMG/20220819'
# fin_dir = 'C:/Users/User/Desktop/test_data_1007/fin_img'
# 
# for copy_img in fin_data_sort:
#     print(copy_img[0])
#     shutil.copy(oriimg_dir + "/" + copy_img[0], fin_dir + "/" + copy_img[0])
# =============================================================================

# =============================================================================
# ## 메모장 읽어들이기 2
# string_ori = file.readlines()
# # file_info = []
# 
# img = []
# 
# # 내공/내백 검출 결과값 저장 리스트
# # bb_x, bb_y, bb_w, bb_h, in_flag, detect_flag = [], [], [], [], [], []
# 
# ## 최후미에 있는 '\n'을 제거 및 내공/내백 결과값 저장 및 검출범위에 속하는지 확인
# for string in string_ori:
#     info = string.split('\n')[0]
#     info = info.split(' ')
#     
#     # file_info.append(info)
#     # file_info = [info, is_this_in(ginseng_x, ginseng_y, ginseng_w, ginseng_h, float(info[1]), float(info[2]), float(info[3]), float(info[4])) 
#                    ,detection_error_part(ginseng_x, float(info[1]), float(info[3]))]
#     
#     # bb_x.append(info[1])
#     # bb_y.append(info[2])
#     # bb_w.append(info[3])
#     # bb_h.append(info[4])
#     # in_flag.append(is_this_in(ginseng_x, ginseng_y, ginseng_w, ginseng_h, float(info[1]), float(info[2]), float(info[3]), float(info[4])))
#     # detect_flag.append(detection_error_part(ginseng_x, float(info[1]), float(info[3])))
# 
#     test_img = ['20220707_Xray_003009.jpg' ,info, is_this_in(ginseng_x, ginseng_y, ginseng_w, ginseng_h, float(info[1]), 
#                   float(info[2]), float(info[3]), float(info[4])) ,detection_error_part(ginseng_x, float(info[1]), float(info[3]))]
#     img.append(test_img)
# 
# file.close()
# =============================================================================