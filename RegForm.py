# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtCore import QTimer
from FacialRecognize import RecordVideo,CreateDataSet,training
import Database as db
import numpy as np

class Reg_Dialog(object):

    def setupUi(self, Dialog,loginDialog):
        # - - - - - -init - - - - - -
        self.preDialog = loginDialog

        self.dialog = Dialog
        self.insert = db.Insert("localhost", 27017, 'Facial_RecogDB')
        self.find = db.Find("localhost", 27017, 'Facial_RecogDB')

        Dialog.setObjectName("Dialog")
        Dialog.resize(894, 704)
        Dialog.setMinimumSize(QtCore.QSize(822, 700))
        Dialog.setMaximumSize(QtCore.QSize(900, 800))
        Dialog.setStyleSheet("background-color: rgb(58, 58, 58);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(900, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:white;")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 440, 411, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color:white;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_admin = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_admin.setGeometry(QtCore.QRect(150, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_admin.setFont(font)
        self.lineEdit_admin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_admin.setText("")
        self.lineEdit_admin.setObjectName("lineEdit_admin")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(150, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_pwd.setFont(font)
        self.lineEdit_pwd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_pwd.setText("")
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 150, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_confirm = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_confirm.setGeometry(QtCore.QRect(150, 160, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_confirm.setFont(font)
        self.lineEdit_confirm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_confirm.setText("")
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 50, 411, 461))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color:white;")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_lname.setGeometry(QtCore.QRect(150, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_lname.setFont(font)
        self.lineEdit_lname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_lname.setText("")
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_fname.setGeometry(QtCore.QRect(150, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_fname.setFont(font)
        self.lineEdit_fname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_fname.setText("")
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(20, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(20, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(20, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(20, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_age = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_age.setGeometry(QtCore.QRect(150, 280, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_age.setFont(font)
        self.lineEdit_age.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_age.setText("")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.lineEdit_address = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_address.setGeometry(QtCore.QRect(150, 220, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_address.setText("")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.radioButton_m = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_m.setGeometry(QtCore.QRect(150, 349, 137, 29))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.radioButton_m.setFont(font)
        self.radioButton_m.setObjectName("radioButton_m")
        self.lineEdit_job = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_job.setGeometry(QtCore.QRect(150, 160, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_job.setFont(font)
        self.lineEdit_job.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_job.setText("")
        self.lineEdit_job.setObjectName("lineEdit_job")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_email.setGeometry(QtCore.QRect(150, 400, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(20, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.radioButton_f = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_f.setGeometry(QtCore.QRect(280, 350, 91, 29))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.radioButton_f.setFont(font)
        self.radioButton_f.setObjectName("radioButton_f")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(20, 400, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 50, 411, 391))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("color:white;")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 50, 361, 281))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-160, -10, 671, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")



        # - - - - - - - set reg video and detection cv2
        self.create_data_set_widget = CreateDataSet('trainer\haarcascade_frontalface_default.xml')



        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.formLayout.addWidget(self.create_data_set_widget)



        self.label_status = QtWidgets.QLabel(self.groupBox_5)
        self.label_status.setGeometry(QtCore.QRect(50, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_status.setObjectName("label_status")
        self.label_status_msg = QtWidgets.QLabel(self.groupBox_5)
        self.label_status_msg.setGeometry(QtCore.QRect(140, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_status_msg.setFont(font)
        self.label_status_msg.setAutoFillBackground(False)
        self.label_status_msg.setObjectName("label_status_msg")
        self.pushButton_submit = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_submit.setGeometry(QtCore.QRect(670, 570, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_submit.setFlat(False)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setGeometry(QtCore.QRect(500, 570, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_cancel.setFlat(False)
        self.pushButton_cancel.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def update(self, method, milisec):
        # ---- update ui
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(milisec)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(method)
        # start timer
        self.qTimer.start()


    def updateUI(self):
        self.create_data_set_widget.imsave = True
        self.label_status_msg.setText(str(self.create_data_set_widget.frame) + " frame")


    def trainer(self):
        #save img into dataset
        self.create_data_set_widget.saveIMG()


        # - - - - TRAINER - - - -#
        # Get the faces and IDs
        faces, ids = training.getImagesAndLabels('dataset')
        # Train the model using the faces and IDs
        training.recognizer.train(faces, np.array(ids))
        # Save the model into trainer.yml
        training.assure_path_exists('trainer/')
        training.recognizer.save('trainer/trainer.yml')
        print('success to registered.')
        self.Messagebox('Message', 'Success', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Information)

        self.record_video.stop_recording()

        self.preDialog.show()
        self.dialog.hide()
        #QtCore.QCoreApplication.instance().quit()
        


    def Messagebox(self,title,text,button,icon):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)

        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(button)
        return msg.exec_()

    def submitOnClicked(self):
        if self.Messagebox('Message','Do you want to save?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.Warning) == QtWidgets.QMessageBox.Yes:
            fname = self.lineEdit_fname.text()
            lname = self.lineEdit_lname.text()
            job = self.lineEdit_job.text()
            address = self.lineEdit_address.text()
            age = self.lineEdit_age.text()

            if self.radioButton_f.isChecked():
                gender = 'F'
            elif self.radioButton_m.isChecked():
                gender = 'M'
            else:
                gender = 'U'

            email = self.lineEdit_email.text()
            admin = self.lineEdit_admin.text()
            pwd = self.lineEdit_pwd.text()
            confirm = self.lineEdit_confirm.text()

            id = str((int(self.find.lastID()) + 1))

            if admin and pwd and confirm:
                if pwd == confirm:
                    print('insert admin')
                    self.insert.admin(id, admin, pwd)
                    self.insert.personal(id, fname, lname, job, address, age, gender, email, datetime.datetime.now(),
                                         '')
                    self.trainer()

                else:
                    self.Messagebox('Message', 'password confirm again!',
                                    QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Warning)

            else:
                self.insert.personal(id, fname, lname, job, address, age, gender, email, datetime.datetime.now(), '')
                self.trainer()

    def cancelOnClicked(self):
        self.record_video.stop_recording()

        self.preDialog.show()
        self.dialog.hide()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register"))
        self.groupBox.setTitle(_translate("Dialog", "Register"))
        self.groupBox_2.setTitle(_translate("Dialog", "Admin"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.lineEdit_admin.setPlaceholderText(_translate("Dialog", "admin"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.lineEdit_pwd.setPlaceholderText(_translate("Dialog", "o o o o o o o o"))
        self.label_12.setText(_translate("Dialog", "Confirm"))
        self.lineEdit_confirm.setPlaceholderText(_translate("Dialog", "o o o o o o o o"))
        self.groupBox_4.setTitle(_translate("Dialog", "Personal"))
        self.lineEdit_lname.setPlaceholderText(_translate("Dialog", "Last Name"))
        self.lineEdit_fname.setPlaceholderText(_translate("Dialog", "First Name"))
        self.label_13.setText(_translate("Dialog", "Gender"))
        self.label_14.setText(_translate("Dialog", "First Name"))
        self.label_15.setText(_translate("Dialog", "Address"))
        self.label_16.setText(_translate("Dialog", "Job"))
        self.lineEdit_age.setPlaceholderText(_translate("Dialog", "1-99"))
        self.label_17.setText(_translate("Dialog", "Last Name"))
        self.lineEdit_address.setPlaceholderText(_translate("Dialog", "123/456 BKK Thailand"))
        self.radioButton_m.setText(_translate("Dialog", "Male"))
        self.lineEdit_job.setPlaceholderText(_translate("Dialog", "Programmer"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog", "mail@domain.com"))
        self.label_18.setText(_translate("Dialog", "Age"))
        self.radioButton_f.setText(_translate("Dialog", "Female"))
        self.label_11.setText(_translate("Dialog", "E-Mail"))
        self.groupBox_5.setTitle(_translate("Dialog", "Camera (1)"))
        self.label_status.setText(_translate("Dialog", "Status : "))
        self.label_status_msg.setStyleSheet(_translate("Dialog", "0"))
        self.label_status_msg.setText(_translate("Dialog", "? frame"))
        self.pushButton_submit.setText(_translate("Dialog", "Submit"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))

        self.pushButton_submit.clicked.connect(self.submitOnClicked)
        self.pushButton_cancel.clicked.connect(self.cancelOnClicked)
        self.update(self.updateUI, 1000)


        # TODO: set faceID to data get last form mongodb
        self.create_data_set_widget.setFaceId(str(int(self.find.lastID()) + 1))

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.create_data_set_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)
        self.record_video.start_recording()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Reg_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




