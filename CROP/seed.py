import cv2
import numpy as np
import imutils

###############################변수지정###################################
ta = []
# tlist = []
pos_list = []

index = 0

i = 0
###############################이미지 불러오기############################
test = cv2.imread('C:/Users/User/Desktop/0602.jpg') #bgr이미지 불러오기
test2= cv2.cvtColor(test, cv2.COLOR_BGR2GRAY) #bgr2gray
h,w = test2.shape[:2]   #이미지 형태 불러오기
edges = cv2.Canny(test2, 50, 150)  #호퍼 변환을 위해 캐니

lines = cv2.HoughLines(edges, 1, np.pi/180, 1800) #호퍼변환

for line in lines:
    rho, theta = line[0]
    
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a*rho
    y0 = b*rho
    
    x1,y1 = int(x0 + w * (-b)), int(y0 + h * a)
    x2,y2 = int(x0 - w * (-b)), int(y0 - h * a)
    
    cv2.line(test2, (x1,y1), (x2,y2), (255,255,255), 50)
###############여까지 호퍼###################

###############쓰레스 홀드###################
ret, test3_2 = cv2.threshold(test2, 50, 255, 0)

# =============================================================================
# cnts, hierarchy = cv2.findContours(test3_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# tlist = list(cnts)
# =============================================================================

cnts, hierarchy = cv2.findContours(test3_2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
(cnts, _) = imutils.contours.sort_contours(cnts, method="top-to-bottom")

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area <5000 and area >200:
    # if area >60 and area < 700:
        ta.append(cnt)
        index += 1
    else:
        index += 1

##
checkerboard_row = []
row =[]
##

for (i,c) in enumerate(ta,1):
    # area = cv2.contourArea(c)
    row.append(c)
    
    if i % 10 == 0 :
        (cnts,_) = imutils.contours.sort_contours(row,method="left-to-right")
        checkerboard_row.append(cnts)
        row = []

# =============================================================================
# for cnt3 in ta:
#     m = cv2.moments(cnt3)
#     cx = int(m["m10"] / m["m00"])
#     cy = int(m["m01"] / m["m00"])
#     pos = [cx,cy]
#     pos_list.append(pos)
# 
# for i in range(int(len(pos_list))):
#     t1 = cv2.rectangle(test, (pos_list[i][0]-320,pos_list[i][1]-320), (pos_list[i][0]+320,pos_list[i][1]+320), (0,0,255), 15)
#     cv2.putText(test, str(i+1), (pos_list[i][0],pos_list[i][1]), cv2.FONT_HERSHEY_DUPLEX, 10, (255,0,0), 15)
#     test1 = cv2.resize(test, dsize=(1280,960))
#     test2 = cv2.resize(test2,dsize=(1280,960))
#     tt = cv2.resize(edges,dsize=(1280,960))
# =============================================================================

i = 0
for row in checkerboard_row:
    for c in row:
        m = cv2.moments(c)
        cx = int(m["m10"] / m["m00"])
        cy = int(m["m01"] / m["m00"])
        
        t1 = cv2.rectangle(test, (cx-320,cy-320), (cx+320,cy+320), (0,0,255), 15)
        cv2.putText(test, str(i+1), (cx,cy), cv2.FONT_HERSHEY_DUPLEX, 10, (255,0,0), 15)        
        i += 1

test1 = cv2.resize(test, dsize=(1280,960))
test2 = cv2.resize(test2,dsize=(1280,960))
tt = cv2.resize(edges,dsize=(1280,960))

cv2.imshow("sorted", test1)
cv2.waitKey(0)
##################################


# ============================================================================= ??? 추후 사용가능
# # ============================================================================= 
# #     area_list.append(r_a)
# #     ratio_list.append(ratio)
# # =============================================================================
#     
# # f1 = open("test/area_data.dat", "w")
# # f1.write("Area" + "\n")
# 
# # for i in range(len(area_list)):
# #     f1.write(str(area_list[i]) + "\n")
# # f1.close()
# 
# # t1 = cv2.resize(t1, dsize=(1280,960))
# # test1 = cv2.resize(test, dsize=(1280,960))
# 
# # =============================================================================
# # cv2.imwrite('test/test'+'.jpg', test)
# # cv2.imshow('t',test3_2)
# # cv2.waitKey(0)
# # =============================================================================
# 
# =============================================================================
