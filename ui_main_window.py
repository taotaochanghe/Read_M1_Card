# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_sum = QtWidgets.QLabel(self.frame_2)
        self.label_sum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sum.setObjectName("label_sum")
        self.horizontalLayout.addWidget(self.label_sum)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter_4 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.label_3.setObjectName("label_3")
        self.lineEdit_payment = QtWidgets.QLineEdit(self.splitter_4)
        self.lineEdit_payment.setEnabled(True)
        self.lineEdit_payment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_payment.setObjectName("lineEdit_payment")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_pay = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_pay.setObjectName("pushButton_pay")
        self.pushButton_invalid = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_invalid.setObjectName("pushButton_invalid")
        self.pushButton_read = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_read.setObjectName("pushButton_read")
        self.pushButton_hand = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_hand.setObjectName("pushButton_hand")
        self.pushButton_unlock = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_unlock.setObjectName("pushButton_unlock")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.verticalLayout.addWidget(self.textBrowser_output)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "充值卡修改器"))
        self.label.setText(_translate("MainWindow", "卡内余额"))
        self.label_sum.setText(_translate("MainWindow", "0.00"))
        self.label_3.setText(_translate("MainWindow", "充值金额"))
        self.lineEdit_payment.setText(_translate("MainWindow", "100"))
        self.pushButton_pay.setText(_translate("MainWindow", "充值"))
        self.pushButton_invalid.setText(_translate("MainWindow", "失效"))
        self.pushButton_read.setText(_translate("MainWindow", "读卡"))
        self.pushButton_hand.setText(_translate("MainWindow", "发卡"))
        self.pushButton_unlock.setText(_translate("MainWindow", "解锁"))
