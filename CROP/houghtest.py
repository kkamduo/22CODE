# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:48:19 2022

@author: JSH
"""

import cv2
import numpy as np

test = cv2.imread('C:/Users/User/Desktop/0602.jpg')
test1 = cv2.resize(test, dsize=(1280,960))
h,w = test1.shape[:2]

img_gray = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 80, 150)

lines = cv2.HoughLines(edges, 1, np.pi/180, 230)

for line in lines:
    rho, theta = line[0]
    
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a*rho
    y0 = b*rho
    
    x1,y1 = int(x0 + w * (-b)), int(y0 + h * a)
    x2,y2 = int(x0 - w * (-b)), int(y0 - h * a)
    
    cv2.line(test1, (x1,y1), (x2,y2), (125,125,125),5)
    
# test1 = cv2.resize(test, dsize=(1280,960))    
edges1 = cv2.resize(edges,dsize=(1280,960))

cv2.imshow("Test",test1)
cv2.waitKey(0)