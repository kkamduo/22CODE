from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import crop_tool_ui as bb
import cv2
import re
import numpy as np
import sys
import os
from datetime import datetime
from imutils import contours

pop_num_list = []

#크로핑(이하 GraphicsItem) 생성
class Testset(QGraphicsItemGroup):
    global pop_num_list

    #GraphicsItem 생성시 기본 Default값 지정
    def __init__(self,i,x,y,pix):
        super().__init__()
        self.cnt = i
        self.pix = pix
        self.bb = QGraphicsRectItem()
        self.pos_x = x
        self.pos_y = y
        self.bb.setRect(self.pos_x-(self.pix), self.pos_y-(self.pix), 2*self.pix, 2*self.pix)
        self.hover_flag = False

        #초기 좌표에 따라 박스 팬 색상설정
        if (self.pos_x-self.pix > 0 and self.pos_y-self.pix > 0 and self.pos_x+self.pix < 1200 and self.pos_y+self.pix < 900): 
            self.bb.setPen(Qt.green)
        else : self.bb.setPen(Qt.red)

        #좌측상단 박스 라벨 번호 추가
        self.lab = QGraphicsTextItem(str(i))
        self.lab.setPos(self.pos_x-50, self.pos_y-50)
        self.fontt = self.lab.font()
        self.fontt.setPointSize(20)
        self.lab.setFont(self.fontt)

        #GraphicsItem 그룹 지정 (라벨 + 박스)
        self.addToGroup(self.bb)
        self.addToGroup(self.lab)

        #GraphicsItem 선택,이동,HoverEvent 지정
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.box_pos = (self.pos_x, self.pos_y)

    #GraphicsItem 마우스 이벤트 지정
    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            ui.img_view_scene.removeItem(self)
            pop_num_list.append(self.cnt)
            pop_num_list.sort()
            ui.img_view_scene.boxes[self.cnt-1] = None

        if event.buttons() == Qt.LeftButton:
            self.hover_flag = True
            
    #GraphicsItem Hover 이벤트 지정 (박스이동)
    def hoverMoveEvent(self, event):
        if self.hover_flag :
            # print(self.pos_x,self.pos_y)
            # print(self.pos_x + self.pos().x(),self.pos_y + self.pos().y())
            self.box_pos = (self.pos_x + self.pos().x(),self.pos_y + self.pos().y())
            # if (event.scenePos().x()-self.pix > 0 and event.scenePos().y()-self.pix > 0 
            #     and event.scenePos().y()+self.pix < 900 and event.scenePos().x()+self.pix < 1200): 
            if (self.box_pos[0]-self.pix > 0 and self.box_pos[1]-self.pix > 0 
                and self.box_pos[1]+self.pix < 900 and self.box_pos[0]+self.pix < 1200): 
                self.bb.setPen(Qt.green)
            else : 
                self.bb.setPen(Qt.red)
                
            self.scene().clearSelection()

        self.hover_flag = False

#화면 중앙 라벨생성
class graphicsScene(QtWidgets.QGraphicsScene):
    #라벨 생성시 기본 Default값 지정
    def __init__ (self, i, pix, parent=None):
        super(graphicsScene, self).__init__ (parent)
        self.i = i
        self.x = 0
        self.y = 0
        self.boxes = []
        self.test_num = 0
        self.flag = False
        self.pix = pix

    #라벨 마우스 이벤트 지정
    def mousePressEvent(self, event) :
        #박스 생성
        if event.buttons() == Qt.LeftButton and self.flag:
            if pop_num_list == [] :
                self.x = event.scenePos().x()
                self.y = event.scenePos().y()

                self.test = Testset(self.i, self.x, self.y, self.pix)
                self.boxes.append(self.test)
                self.addItem(self.test)

                self.i += 1

        #박스 제거
            elif pop_num_list != []:
                self.x = event.scenePos().x()
                self.y = event.scenePos().y()
                self.test_num = pop_num_list.pop(0)

                self.test = Testset(self.test_num, self.x, self.y, self.pix)
                self.boxes[self.test_num-1] =  self.test
                self.addItem(self.test)

    #Ctrl 키에 대한 플래그 지정
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control :
            self.flag = True

    def keyReleaseEvent(self, event):
        self.flag = False

#메인 윈도우 생성
class Ui_MainWindow(QtWidgets.QMainWindow,bb.tt_MainWindow):
    #메인윈도우 초기 셋팅
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphicsPixmapItem = None
        self.folder = None
        self.pixel_size = None

    #하단 이미지 OPEN버튼 함수 구현
    def Img_Dialog(self):
        global main_img, main_img2

        if self.graphicsPixmapItem != None : self.img_view_scene.removeItem(self.graphicsPixmapItem)

        if self.pixel_size != None :
            self.img_view_scene = graphicsScene(1,self.pixel_size)
            self.img_Label.setScene(self.img_view_scene)

            checkerboard_row = []
            row =[]
            ta = []
            self.img_view_scene.i = 1
            self.img_view_scene.boxes = []
            self.img_view_scene.test_num = 0

            #파일 열기창 생성
            filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open Data File', '','')

            if filename[0] != '' :
                img = filename[0]

                #파일 불러오기
                main_img = cv2.imread(img)
                a = re.split(r"[/]",img)
                self.img_name_Label.setText(a[len(a)-1])

                #이미지 조정
                main_img2 = cv2.resize(main_img, dsize=(1200,900))
                main_img2 = cv2.cvtColor(main_img2, cv2.COLOR_BGR2RGB)
                img_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
                ret, img_thres = cv2.threshold(img_gray, 100, 255, 0)

                #이미지 변환 (라벨에 들어갈수 있도록 변환)
                [h, w, c] = main_img2.shape
                main_img2 = QtGui.QImage(main_img2.data, w, h, w*c, QtGui.QImage.Format_RGB888)
                main_img2 = QtGui.QPixmap.fromImage(main_img2)
                self.graphicsPixmapItem = QGraphicsPixmapItem(main_img2)
                self.graphicsPixmapItem.ItemIsSelectable = False
                self.img_view_scene.addItem(self.graphicsPixmapItem)
                self.img_Label.setScene(self.img_view_scene)

                #오토크로핑
                cnts, hierarchy = cv2.findContours(img_thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                (cnts, _) = contours.sort_contours(cnts, method="top-to-bottom")

                for cnt in cnts:
                    area = cv2.contourArea(cnt)
                    if area <10000 and area >2500:
                        ta.append(cnt)

                for (i,c) in enumerate(ta,1):
                    row.append(c)

                    if i % 11 == 0 :
                        (cnts,_) = contours.sort_contours(row,method="left-to-right")
                        checkerboard_row.append(cnts)
                        row = []

                for row in checkerboard_row:
                    for c in row:
                        m = cv2.moments(c)
                        cx = int(m["m10"] / m["m00"])
                        cy = int(m["m01"] / m["m00"])

                        self.img_view_scene.test = Testset(self.img_view_scene.i, cx/10, cy/10, self.pixel_size)
                        self.img_view_scene.test.x = cx/10
                        self.img_view_scene.test.y = cy/10
                        self.img_view_scene.boxes.append(self.img_view_scene.test)
                        self.img_view_scene.addItem(self.img_view_scene.test)
                        self.img_view_scene.i += 1
        else :
            QMessageBox.information(self,'Pixel Error', '우측 하단의 픽셀을 선택해주세요.')

    #하단 픽셀지정(리스트위젯)
    def Pixel_select(self):
        if self.Set_Pixel_1.isChecked() :
            self.pixel_size = 32
        elif self.Set_Pixel_2.isChecked():
            self.pixel_size = 48
        elif self.Set_Pixel_3.isChecked():
            self.pixel_size = 64
        elif self.Set_Pixel_4.isChecked():
            self.pixel_size = 96

    #우측 상단 폴더지정
    def Set_Folder(self):
        global file_list, folderPath

        folderPath = QFileDialog.getExistingDirectory()

        if folderPath != '':
            self.folder = folderPath
            self.folder_name_Label.setText(self.folder)
            file_list = os.listdir(self.folder)
            self.folder_list.addItems(file_list)

    #우측 상단 파일 저장
    def Save_croping(self):
        global crop_img, main_img_copy

        save_name = re.split(r"[.]",self.img_name_Label.text())

        if self.folder != None:
            for print_bb in self.img_view_scene.boxes :
                if print_bb != None:

                    crop_img = main_img[int((10*print_bb.box_pos[1])-(self.pixel_size*10)) : int((10*print_bb.box_pos[1])+(self.pixel_size*10)),
                                        int((10*print_bb.box_pos[0])-(self.pixel_size*10)): int(10*print_bb.box_pos[0])+(self.pixel_size*10)]
                    if crop_img.size > 0 and crop_img.size == (np.square(self.pixel_size*2*10) * 3) :
                        cv2.imwrite(self.folder + '/' + save_name[0] + '_' + str(print_bb.cnt) + '.jpg', crop_img)
                    else:
                        QMessageBox.information(self, 'Save Image Error', (str(print_bb.cnt) + '번 이미지를 확인해주세요.'))

                    self.folder_list.clear()
                    file_list = os.listdir(self.folder)
                    self.folder_list.addItems(file_list)
        else :
            QMessageBox.information(self,'Folder Error', '우측 상단의 저장 폴더를 지정해주세요.')

    #우측 폴더리스트 선택 및 라벨 사진 표현
    def Crop_file_select(self):
        if self.folder_list.currentItem() != None:
            crop = self.folder_list.currentItem().text()
            self.img_crop_name_Label.setText(crop)
            crop_img2 = cv2.imread(self.folder + '/' + crop)
            crop_img2 = cv2.resize(crop_img2, dsize = (200,200))

            [h, w, c] = crop_img2.shape
            crop_img2 = QtGui.QImage(crop_img2.data, w, h, w*c, QtGui.QImage.Format_RGB888)
            crop_img2 = QtGui.QPixmap.fromImage(crop_img2)
            self.img_crop_Label.setPixmap(crop_img2)

#메인문
if __name__ == "__main__":
    global ui
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())