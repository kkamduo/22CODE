# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:03:24 2022

@author: JSH
"""

import cv2
import numpy as np
class rect:
    def __init__(self,img,x,y,i):  #bb 좌표 입력받기
        self.click_flag = True #선택 상태인지 아닌지
        self.w = 30 #bb의 넓이 및 높이 (320)
        self.h = 30
        self.x_pos = x 
        self.y_pos = y #bb 좌표
        self.num = i
        self.image = img

    def move_bb(self,way):

        if self.click_flag :

            if way == 'l' :
                self.x_pos = self.x_pos - 2
                # cv2.rectangle(self.image, (self.x_pos-self.w,self.y_pos-self.h), (self.x_pos+self.w,self.y_pos+self.h), (0,0,255), 15)
                print('x_pos = ',self.x_pos)
                cv2.imshow('t',tt)

            elif way == 'r' :
                self.x_pos = self.x_pos + 2
                # cv2.rectangle(self.image, (self.x_pos-self.w,self.y_pos-self.h), (self.x_pos+self.w,self.y_pos+self.h), (0,0,255), 15)
                print('x_pos = ',self.x_pos)
                cv2.imshow('t',tt)

            elif way == 'u':
                self.y_pos = self.y_pos - 2
                # cv2.rectangle(self.image, (self.x_pos-self.w,self.y_pos-self.h), (self.x_pos+self.w,self.y_pos+self.h), (0,0,255), 15)
                print('y_pos = ',self.y_pos)
                cv2.imshow('t',tt)
            
            elif way == 'd':
                self.y_pos = self.y_pos + 2
                # cv2.rectangle(self.image, (self.x_pos-self.w,self.y_pos-self.h), (self.x_pos+self.w,self.y_pos+self.h), (0,0,255), 15)
                print('y_pos = ',self.y_pos)
                cv2.imshow('t',tt)

    def draw_bb(self):
        cv2.rectangle(self.image, (self.x_pos-self.w,self.y_pos-self.h), (self.x_pos+self.w,self.y_pos+self.h), (0,0,255), 15)
        cv2.putText(self.image, str(self.num+1), (self.x_pos,self.y_pos), cv2.FONT_HERSHEY_DUPLEX, 10, (255,0,0), 15)

test = cv2.imread('C:/Users/User/Desktop/0602.jpg') #bgr이미지 불러오기
test2= cv2.cvtColor(test, cv2.COLOR_BGR2GRAY) #bgr2gray
h,w = test2.shape[:2]   #이미지 형태 불러오기
tt = cv2.resize(test, dsize=(900,1200))


rect1 = rect(tt,500,500,1)
rect1.draw_bb()


cv2.imshow('t',tt)

while True:
    if cv2.waitKey() == 27:
        break
    elif cv2.waitKeyEx() == 0x250000:
        rect1.move_bb('l')
    elif cv2.waitKeyEx() == 0x270000:
        rect1.move_bb('r')
    elif cv2.waitKeyEx() == 0x260000:
        rect1.move_bb('u')
    elif cv2.waitKeyEx() == 0x280000:
        rect1.move_bb('d')
    elif cv2.EVENT_LBUTTONDOWN():
        rect1.remove()
        
cv2.destroyAllWindows()