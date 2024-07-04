# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:13:40 2022

@author: JSH
"""

import cv2 as cv
import numpy as np

img_color = cv.imread('C:/Users/User/Desktop/pair_test/20220812_Xray_000017.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 50, 255, 0)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue

# cv.imshow("result", img_color)

# cv.waitKey(0)

# for cnt in contours:

#     x, y, w, h = cv.boundingRect(cnt)
#     cv.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)


# cv.imshow("result", img_color)

# cv.waitKey(0)

for cnt in contours:

    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)

    cv.drawContours(img_color,[box],0,(0,0,255),2)

test = cv.resize(img_color, dsize = (1200,800))

cv.imshow("result", test)

cv.waitKey(0)