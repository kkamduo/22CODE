# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:33:28 2022

@author: JSH
"""
import cv2


img = 'C:/Users/User/Desktop/0616.jpg'
main_img = cv2.imread(img)

main_img2 = cv2.resize(main_img, dsize=(1200,900))
img_gray = cv2.cvtColor(main_img2, cv2.COLOR_BGR2GRAY)
ret, img_thres = cv2.threshold(img_gray, 50, 255, 0)

cv2.imshow('test',img_thres)
cv2.waitKey()
