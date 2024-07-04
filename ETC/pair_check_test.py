# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:11:42 2022

@author: JSH
    """

import cv2, numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('C:/Users/User/Desktop/test.png')
img1 = ~img1
# img2 = cv2.imread('C:/Users/User/Desktop/20220919/20220919_Xray_000122.jpg') 


sharpening_mask1 = np.array([[-2, -2, -2], [-2, 17, -2], [-2, -2, -2]])
sharpening_mask2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpening_mask3 = np.array([[-3, -3, -3], [-3, 28, -3], [-3, -3, -3]])

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
# hist2 = cv2.calcHist([img2], [0], None, [256], [0, 255])

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, gray_Test = cv2.threshold(gray1, 30, 255 ,cv2.THRESH_TRUNC)

gray1_s = cv2.filter2D(gray1, -1, sharpening_mask1)
equal = cv2.equalizeHist(gray1)


# plt.subplot(211), plt.plot(hist1)
# plt.subplot(212), plt.plot(equal)
# plt.show()

tt = cv2.resize(equal , dsize = (1200,800))

cv2.imshow('test', tt)
cv2.waitKey()

# ret = cv2.compareHist(hist1,hist2, cv2.HISTCMP_BHATTACHARYYA)