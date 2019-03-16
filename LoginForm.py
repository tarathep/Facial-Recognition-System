# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from DetailForm import Detail_Dialog
from FacialRecognize import *
from PyQt5.QtCore import QTimer
from Database import Find
from RegForm import Reg_Dialog


class Login_Dialog(object):


    def setupUi(self, Dialog):
        self.I = 0

        self.opcamera = False
        self.active = 0
        self.loginDialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 603)
        Dialog.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(560, 450, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.pushButton_ok.setFlat(False)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 731, 331))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:white;")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 361, 281))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-160, -10, 671, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        # - - - -  CONNECT TO VIEW CAMERA

        self.face_detection_widget = FaceDetectionWidget('trainer\haarcascade_frontalface_default.xml')

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.addWidget(self.face_detection_widget)

        # set img status
        self.label_img = QtWidgets.QLabel(self.groupBox)
        self.label_img.setGeometry(QtCore.QRect(490, 90, 161, 161))
        self.label_img.setObjectName("label_img")

        # ---- update ui
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(2000)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.updateUI)
        # start timer
        self.qTimer.start()

        self.label_img.setPixmap(QtGui.QPixmap('data/authen_status/unknown.png'))



        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 430, 481, 161))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color:white;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_user = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_user.setGeometry(QtCore.QRect(180, 40, 281, 41))
        self.lineEdit_user.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(180, 100, 281, 41))
        self.lineEdit_pwd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Comic Sans MS\";")
        self.lineEdit_pwd.setText("")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_register = QtWidgets.QPushButton(Dialog)
        self.pushButton_register.setGeometry(QtCore.QRect(560, 530, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_register.setFont(font)
        self.pushButton_register.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.pushButton_register.setFlat(False)
        self.pushButton_register.setObjectName("pushButton_register")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 30, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "System Login"))
        self.pushButton_ok.setText(_translate("Dialog", "Login"))
        self.groupBox.setTitle(_translate("Dialog", "Authentication1"))
        self.label_img.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Dialog", "Authentication2"))
        self.lineEdit_user.setPlaceholderText(_translate("Dialog", "Admin"))
        self.lineEdit_pwd.setPlaceholderText(_translate("Dialog", " o o o o o o"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.pushButton_register.setText(_translate("Dialog", "Register"))
        self.label.setText(_translate("Dialog", "System Login"))

        self.pushButton_ok.clicked.connect(self.checkAuthII)
        self.pushButton_register.clicked.connect(self.openWindowRegister_Update)
        self.callVideoRec()


    def callVideoRec(self):
        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)
        self.record_video.start_recording()


    def Messagebox(self,title,text,button,icon):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(button)
        return msg.exec_()

    def openWindowRegister_Update(self):
        #QtCore.QCoreApplication.instance().quit()
        self.record_video.stop_recording()
        self.window = QtWidgets.QDialog()
        self.ui = Reg_Dialog()
        self.ui.setupUi(self.window,self.loginDialog)
        self.window.show()
        Dialog.hide()


    def updateUI(self):
        if(self.loginDialog.isActiveWindow()):
            self.I +=1
            percent = self.face_detection_widget.getStatus()
            if percent > 30:
                self.label_img.setPixmap(QtGui.QPixmap('data/authen_status/true.png'))
            elif percent == 0:
                self.label_img.setPixmap(QtGui.QPixmap('data/authen_status/unknown.png'))
            else:
                self.label_img.setPixmap(QtGui.QPixmap('data/authen_status/false.png'))
        else: self.I = 0
        if self.I ==1:
            print('OPEN')
            self.callVideoRec()

    def checkAuthII(self):
        self.callVideoRec()

        find = Find("localhost", 27017, 'Facial_RecogDB')
        user = self.lineEdit_user.text()
        pwd = self.lineEdit_pwd.text()

        id = find.admin(user,pwd)
        #print(id,self.face_detection_widget.id)
        if str(id) == str(self.face_detection_widget.id):
            self.Messagebox('Message', 'LOGIN SUCCESSFULLY!',
                            QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Information)
            print('LOGIN SUCCESSFULLY')

            self.record_video.stop_recording()

            self.window = QtWidgets.QDialog()
            self.ui = Detail_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
            Dialog.hide()

        else:
            print('Not Recognized Unauthorized!!')
            self.Messagebox('Message', 'Unauthorized!',
                            QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Warning)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Login_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




