from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class tt_MainWindow(object):

    def setupUi(self, MainWindow):
        ##MainWindow##
        MainWindow.setFixedSize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)        
        MainWindow.setWindowTitle("Crop Tool Prototype")
        MainWindow.setWindowIcon(QIcon("./image/Icon.PNG"))
        MainWindow.setStyleSheet('background:#E3F2FD')

        self.GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox.setGeometry(QtCore.QRect(20, 10, 1460, 970))
        self.GroupBox.setStyleSheet('background:#F5F5F5;' 'border-color:#9E9E9E;' 'border-style:solid;' 'border-width:2px')

        ##GroupBox##
        self.img_Label = QtWidgets.QGraphicsView(self.GroupBox)
        self.img_Label.setGeometry(QtCore.QRect(20, 15, 1200, 900))
        self.img_Label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')
        self.img_Label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.img_Label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.img_Label.setRenderHint(QPainter.Antialiasing)

        self.Open_Btn = QtWidgets.QPushButton('Open', self.GroupBox)
        self.Open_Btn.setGeometry(QtCore.QRect(120, 925, 150, 30))
        self.Open_Btn.clicked.connect(self.Img_Dialog)
        
        self.Set_Pixel_Head_Label = QtWidgets.QLabel('Pixel 선택', self.GroupBox)
        self.Set_Pixel_Head_Label.setStyleSheet('border-style:None')
        self.Set_Pixel_Head_Label.setGeometry(870, 925, 100, 30)
        
        self.Set_Pixel_1 = QtWidgets.QRadioButton('640' ,self.GroupBox)
        self.Set_Pixel_1.setGeometry(935, 925, 50, 30)
        self.Set_Pixel_1.setStyleSheet('border-style:None')
        self.Set_Pixel_1.clicked.connect(self.Pixel_select)
        
        self.Set_Pixel_2 = QtWidgets.QRadioButton('960' ,self.GroupBox)
        self.Set_Pixel_2.setGeometry(985, 925, 50, 30)
        self.Set_Pixel_2.setStyleSheet('border-style:None')
        self.Set_Pixel_2.clicked.connect(self.Pixel_select)
        
        self.Set_Pixel_3 = QtWidgets.QRadioButton('1280' ,self.GroupBox)
        self.Set_Pixel_3.setGeometry(1035, 925, 50, 30)
        self.Set_Pixel_3.setStyleSheet('border-style:None')
        self.Set_Pixel_3.clicked.connect(self.Pixel_select)
        
        self.Set_Pixel_4 = QtWidgets.QRadioButton('1920' ,self.GroupBox)
        self.Set_Pixel_4.setGeometry(1085, 925, 50, 30)
        self.Set_Pixel_4.setStyleSheet('border-style:None')
        self.Set_Pixel_4.clicked.connect(self.Pixel_select)
# =============================================================================
#         self.listWidget = QtWidgets.QListWidget(self.GroupBox)
#         self.listWidget.setGeometry(QtCore.QRect(870, 925, 90, 30))
#         self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.listWidget.addItem("Pixel 선택")
#         self.listWidget.addItem("640")
#         self.listWidget.addItem("960")
#         self.listWidget.addItem("1280")
#         self.listWidget.addItem("1920")
#         self.listWidget.clicked.connect(self.Pixel_select)
#         
#         self.pixel_label = QtWidgets.QLabel('Pixel', self.GroupBox)
#         self.pixel_label.setGeometry(1000, 925, 90, 30)
#         self.pixel_label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')
#         self.pixel_label.setAlignment(Qt.AlignCenter)
# =============================================================================


        self.img_name_Label = QtWidgets.QLabel('Img File Name',self.GroupBox)
        self.img_name_Label.setGeometry(QtCore.QRect(320, 925, 500, 30))
        self.img_name_Label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')
        self.img_name_Label.setAlignment(Qt.AlignCenter)

        self.folder_name_Label = QtWidgets.QLabel('Save Folder Name',self.GroupBox)
        self.folder_name_Label.setGeometry(QtCore.QRect(1240, 20, 200, 30))
        self.folder_name_Label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')
        self.folder_name_Label.setAlignment(Qt.AlignCenter)

        self.Open_folder_Btn = QtWidgets.QPushButton('Open', self.GroupBox)
        self.Open_folder_Btn.setGeometry(QtCore.QRect(1240, 65, 200, 30))
        self.Open_folder_Btn.clicked.connect(self.Set_Folder)
        
        self.Save_Btn = QtWidgets.QPushButton('Save', self.GroupBox)
        self.Save_Btn.setGeometry(QtCore.QRect(1240, 110, 200, 30))
        self.Save_Btn.clicked.connect(self.Save_croping)

        self.folder_list = QtWidgets.QListWidget(self.GroupBox)
        self.folder_list.setGeometry(QtCore.QRect(1240, 165, 200, 500))
        # self.folder_list.clicked.connect(self.Crop_file_select)
        self.folder_list.currentItemChanged.connect(self.Crop_file_select)
        
        self.img_crop_Label = QtWidgets.QLabel(self.GroupBox)
        self.img_crop_Label.setGeometry(QtCore.QRect(1240, 700, 200, 200))
        self.img_crop_Label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')
        
        self.img_crop_name_Label = QtWidgets.QLabel(self.GroupBox)
        self.img_crop_name_Label.setGeometry(QtCore.QRect(1240, 925, 200, 30))
        self.img_crop_name_Label.setStyleSheet('background:#E3F2FD;' 'border-style:solid;' 'border-width:2px')