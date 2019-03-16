# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import csv
import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableWidgetItem

from Database import Update, Insert, Delete
from FacialRecognize import *
from RegForm import Reg_Dialog


class Detail_Dialog(object):

    def setupUi(self, Dialog):

        self.detailDialog  = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(1122, 750)
        Dialog.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1121, 751))
        self.groupBox.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:white;")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 30, 411, 711))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color:white;")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_fname.setGeometry(QtCore.QRect(150, 140, 231, 41))
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
        self.label_13.setGeometry(QtCore.QRect(20, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(20, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(20, 320, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(20, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.radioButton_m = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_m.setGeometry(QtCore.QRect(150, 449, 137, 29))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.radioButton_m.setFont(font)
        self.radioButton_m.setObjectName("radioButton_m")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(20, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.radioButton_f = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_f.setGeometry(QtCore.QRect(280, 450, 91, 29))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.radioButton_f.setFont(font)
        self.radioButton_f.setObjectName("radioButton_f")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(20, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(20, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.label_id = QtWidgets.QLabel(self.groupBox_4)
        self.label_id.setGeometry(QtCore.QRect(140, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_id.setObjectName("label_id")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_lname.setGeometry(QtCore.QRect(150, 200, 231, 41))
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
        self.lineEdit_job = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_job.setGeometry(QtCore.QRect(150, 260, 231, 41))
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
        self.lineEdit_address = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_address.setGeometry(QtCore.QRect(150, 320, 231, 41))
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
        self.lineEdit_fname_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_fname_5.setGeometry(QtCore.QRect(150, 380, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_fname_5.setFont(font)
        self.lineEdit_fname_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_fname_5.setText("")
        self.lineEdit_fname_5.setObjectName("lineEdit_fname_5")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_email.setGeometry(QtCore.QRect(150, 500, 231, 41))
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
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_delete.setGeometry(QtCore.QRect(150, 610, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_delete.setFlat(False)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_update.setGeometry(QtCore.QRect(30, 610, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_update.setFont(font)
        self.pushButton_update.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_update.setFlat(False)
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_export = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_export.setGeometry(QtCore.QRect(280, 610, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_export.setFont(font)
        self.pushButton_export.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_export.setFlat(False)
        self.pushButton_export.setObjectName("pushButton_export")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 331, 351))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("color:white;")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 311, 301))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-180, 0, 671, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        # - - - -  CONNECT TO VIEW CAMERA
        self.face_detection_widget = FaceDetectionWidget('trainer\haarcascade_frontalface_default.xml')

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)
        self.record_video.start_recording()

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.addWidget(self.face_detection_widget)



        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(770, 550, 341, 191))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("color:white;")
        self.groupBox_6.setObjectName("groupBox_6")
        self.listView = QtWidgets.QListView(self.groupBox_6)
        self.listView.setGeometry(QtCore.QRect(10, 40, 321, 131))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.listView.setFont(font)
        self.listView.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listView.setObjectName("listView")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 390, 331, 351))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("color:white;")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_img1 = QtWidgets.QLabel(self.groupBox_7)
        self.label_img1.setGeometry(QtCore.QRect(20, 40, 131, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_img1.setFont(font)
        self.label_img1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_img1.setObjectName("label_img1")
        self.label_img2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_img2.setGeometry(QtCore.QRect(180, 40, 131, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_img2.setFont(font)
        self.label_img2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_img2.setObjectName("label_img2")
        self.label_img3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_img3.setGeometry(QtCore.QRect(180, 190, 131, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_img3.setFont(font)
        self.label_img3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_img3.setObjectName("label_img3")
        self.label_img4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_img4.setGeometry(QtCore.QRect(20, 190, 131, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_img4.setFont(font)
        self.label_img4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_img4.setObjectName("label_img4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(770, 30, 341, 511))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("color:white;")
        self.groupBox_8.setObjectName("groupBox_8")



        #-------------- set table init to show

        self.tableView = QtWidgets.QTableWidget(self.groupBox_8)
        self.tableView.setGeometry(QtCore.QRect(10, 30, 321, 361))
        self.tableView.setObjectName("tableView")



        listHeader = ['id','fname','lname','job','address','age','gender','email','registime']
        self.tableView.setColumnCount(len(listHeader))


        for i in range(9):
            item = QtWidgets.QTableWidgetItem(listHeader[i])
            item.setForeground(QtGui.QColor(0, 0, 0))
            self.tableView.setHorizontalHeaderItem(i, item)



        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 400, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("color:white;")
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_ID.setGeometry(QtCore.QRect(20, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_ID.setText("")
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.pushButton_Register = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_Register.setGeometry(QtCore.QRect(180, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton_Register.setFont(font)
        self.pushButton_Register.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Register.setFlat(False)
        self.pushButton_Register.setObjectName("pushButton_Select")
        self.groupBox_7.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.groupBox_8.raise_()


        self.I = 0

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        # ----------------------------------------------------------------------------------------------------------

    def Messagebox(self, title, text, button, icon):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(button)
        return msg.exec_()

    def CSVWriter(self, path, list):
        try:
            with open(path, 'w', newline='', encoding="UTF-8") as f:
                fw = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
                # header
                for i in list:
                    fw.writerow(i)
        except Exception as e:
            print(e)

    def updateOnClicked(self):
        print('updated')
        id = str(self.label_id.text())
        fname = self.lineEdit_fname.text()
        lname = self.lineEdit_lname.text()
        job = self.lineEdit_job.text()
        add = self.lineEdit_address.text()
        age = self.lineEdit_fname_5.text()

        if self.radioButton_m.isChecked():
            self.radioButton_m.setChecked(True)
        elif self.radioButton_m.isChecked():
            self.radioButton_f.setChecked(True)

        if self.radioButton_f.isChecked():
            gender = 'F'
        elif self.radioButton_m.isChecked():
            gender = 'M'
        else:
            gender = 'U'
        email = self.lineEdit_email.text()

        up = Update("localhost", 27017, 'Facial_RecogDB')
        up.personal(id, fname, lname, job, add, age, gender, email)

    def deleteOnClicked(self):
        try:

            delete = Delete("localhost", 27017, 'Facial_RecogDB')

            delete.delAllById(int(self.label_id.text()))

            # - - - - TRAINER - - - -#
            # Get the faces and IDs
            faces, ids = training.getImagesAndLabels('dataset')
            # Train the model using the faces and IDs
            training.recognizer.train(faces, np.array(ids))
            # Save the model into trainer.yml
            training.assure_path_exists('trainer/')
            training.recognizer.save('trainer/trainer.yml')

            self.label_id.setText("?")
            self.lineEdit_fname.setText("")
            self.lineEdit_lname.setText('')
            self.lineEdit_job.setText('')
            self.lineEdit_address.setText('')
            self.lineEdit_fname_5.setText('')

            self.radioButton_m.setChecked(False)
            self.radioButton_f.setChecked(False)

            self.lineEdit_email.setText("")

            self.label_img1.setText("?")
            self.label_img2.setText("?")
            self.label_img3.setText("?")
            self.label_img4.setText("?")

            print('deleted!')
            self.Messagebox('Message', 'Deleted!',
                            QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Warning)
        except:
            print("err not have data")




    def exportOnClicked(self):
        try:
            print('exported')
            raw = []
            id = str(self.face_detection_widget.id)
            find = Find("localhost", 27017, 'Facial_RecogDB')

            p = find.personal(id)
            for i in find.timestamp(str(id)):
                raw.append([id, p[1], p[2], p[3], p[4], p[5], p[6], p[7], i])
            self.CSVWriter("export/" + p[1] + "_export.csv", raw)

            self.Messagebox('Message', 'Exported .CSV', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Information)
        except:
            print('err no data')


    def updateUI(self):
        # UPDATE TABLE
        find = Find("localhost", 27017, 'Facial_RecogDB')
        self.personals = find.personals()

        self.tableView.setRowCount(len(self.personals))

        for i in range(9):
            for j, k in enumerate(self.personals):
                self.tableView.setItem(j, i, QTableWidgetItem(str(k[i])))

        self.tableView.update()



        if (self.detailDialog.isActiveWindow()):
            self.I += 1
        else:
            self.I = 0

        if self.I == 1:
            self.lineEdit_ID.setFocus()
            self.callVideoRec()

        if self.lineEdit_ID.text():
            id = str(self.lineEdit_ID.text())
        else:
            id = str(self.face_detection_widget.id)



        find = Find("localhost", 27017, 'Facial_RecogDB')
        insert = Insert("localhost", 27017, 'Facial_RecogDB')

        try:
            int(id)
        except :
            id = 0


        p = find.personal(int(id))


        if p != None:

            if (self.lineEdit_fname.hasFocus() or self.lineEdit_lname.hasFocus() or\
                    self.lineEdit_job.hasFocus() or self.lineEdit_address.hasFocus() or\
                    self.lineEdit_fname_5.hasFocus() or self.radioButton_m.hasFocus() or\
                    self.radioButton_f.hasFocus() or self.lineEdit_email.hasFocus()):
                print('not action')
            else:
                self.label_id.setText(id)
                self.lineEdit_fname.setText(p[1])
                self.lineEdit_lname.setText(p[2])
                self.lineEdit_job.setText(p[3])
                self.lineEdit_address.setText(p[4])
                self.lineEdit_fname_5.setText(p[5])

                # - - - - - find Gender aet
                if p[6] == 'M':
                    self.radioButton_m.setChecked(True)
                elif p[6] == 'F':
                    self.radioButton_f.setChecked(True)
                else:
                    self.radioButton_m.setChecked(False)
                    self.radioButton_f.setChecked(False)

                self.lineEdit_email.setText(p[7])

                self.label_img1.setPixmap(QtGui.QPixmap('dataset/User.' + id + '.1.jpg'))
                self.label_img2.setPixmap(QtGui.QPixmap('dataset/User.' + id + '.2.jpg'))
                self.label_img3.setPixmap(QtGui.QPixmap('dataset/User.' + id + '.3.jpg'))
                self.label_img4.setPixmap(QtGui.QPixmap('dataset/User.' + id + '.4.jpg'))

                count = find.lastIDTime(int(id))

                insert.timestamp(id, int(count) + 1, datetime.datetime.now())
                fi = find.timestamp(int(id))

                if fi != None:
                    model = QStandardItemModel()
                    for f in fi:
                        model.appendRow(QStandardItem(f))

                    self.listView.setModel(model)

        else:
            self.label_id.setText("?")
            self.lineEdit_fname.setText("")
            self.lineEdit_lname.setText('')
            self.lineEdit_job.setText('')
            self.lineEdit_address.setText('')
            self.lineEdit_fname_5.setText('')

            self.radioButton_m.setChecked(False)
            self.radioButton_f.setChecked(False)

            self.lineEdit_email.setText("")

            self.label_img1.setPixmap(QtGui.QPixmap('data/qperson.png'))
            self.label_img2.setPixmap(QtGui.QPixmap('data/qperson.png'))
            self.label_img3.setPixmap(QtGui.QPixmap('data/qperson.png'))
            self.label_img4.setPixmap(QtGui.QPixmap('data/qperson.png'))


            model = QStandardItemModel()
            model.appendRow(QStandardItem(None))
            self.listView.setModel(model)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Facial Recognition Detail"))
        self.groupBox_4.setTitle(_translate("Dialog", "Personal"))
        self.lineEdit_fname.setPlaceholderText(_translate("Dialog", "Bokie"))
        self.label_13.setText(_translate("Dialog", "Gender"))
        self.label_14.setText(_translate("Dialog", "First Name"))
        self.label_15.setText(_translate("Dialog", "Address"))
        self.label_16.setText(_translate("Dialog", "Job"))
        self.label_17.setText(_translate("Dialog", "Last Name"))
        self.radioButton_m.setText(_translate("Dialog", "Male"))
        self.label_18.setText(_translate("Dialog", "Age"))
        self.radioButton_f.setText(_translate("Dialog", "Female"))
        self.label_11.setText(_translate("Dialog", "E-Mail"))
        self.label_19.setText(_translate("Dialog", "ID"))
        self.label_id.setText(_translate("Dialog", "ID"))
        self.lineEdit_lname.setPlaceholderText(_translate("Dialog", "Tarathep"))
        self.lineEdit_job.setPlaceholderText(_translate("Dialog", "Programmer"))
        self.lineEdit_address.setPlaceholderText(_translate("Dialog", "123/456 BKK"))
        self.lineEdit_fname_5.setPlaceholderText(_translate("Dialog", "1-99"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog", "name@domain.com"))
        self.pushButton_delete.setText(_translate("Dialog", "Delete"))
        self.pushButton_update.setText(_translate("Dialog", "Update"))
        self.pushButton_export.setText(_translate("Dialog", "Export"))
        self.groupBox_5.setTitle(_translate("Dialog", "Camera (1)"))
        self.groupBox_6.setTitle(_translate("Dialog", "Login Time"))
        self.groupBox_7.setTitle(_translate("Dialog", "Pototype"))
        self.label_img1.setText(_translate("Dialog", "?"))
        self.label_img2.setText(_translate("Dialog", "?"))
        self.label_img3.setText(_translate("Dialog", "?"))
        self.label_img4.setText(_translate("Dialog", "?"))
        self.groupBox_8.setTitle(_translate("Dialog", "Registered List"))
        self.groupBox_9.setTitle(_translate("Dialog", "SelectID"))
        self.lineEdit_ID.setPlaceholderText(_translate("Dialog", "Search ID"))
        self.pushButton_Register.setText(_translate("Dialog", "Register"))

        self.pushButton_update.clicked.connect(self.updateOnClicked)
        self.pushButton_delete.clicked.connect(self.deleteOnClicked)
        self.pushButton_export.clicked.connect(self.exportOnClicked)
        self.pushButton_Register.clicked.connect(self.openWindowRegister)

        # ---- update ui
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(2000)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.updateUI)
        # start timer
        self.qTimer.start()

    def callVideoRec(self):
        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)
        self.record_video.start_recording()

    def openWindowRegister(self):
        # QtCore.QCoreApplication.instance().quit()
        self.record_video.stop_recording()
        self.window = QtWidgets.QDialog()
        self.ui = Reg_Dialog()
        self.ui.setupUi(self.window, self.detailDialog)
        self.window.show()
        self.detailDialog.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Detail_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
