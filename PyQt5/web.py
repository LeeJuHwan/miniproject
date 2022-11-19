from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 500)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Entypo")
        self.widget.setFont(font)
        self.widget.setStyleSheet("QWidget#widget{\n"
" border:10px solid rgb(45,45,45);\n"
"border-radius:20px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 240))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 240))
        font = QtGui.QFont()
        font.setFamily("Entypo")
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
" background-color:rgb(20,20,20);\n"
" border-top-left-radius:40px;\n"
" border-top-right-raidus:40px;\n"
"}\n"
"QPushButton{\n"
" background-color:rgba(0,0,0,0);\n"
" color:rgb(144,144,144);\n"
" font:bold;\n"
" font-size:70px;\n"
" font-familyu:entypo;\n"
"}\n"
"QPushButton:hover{\n"
" color:rgb(142,176,27);\n"
"}\n"
"QPushButton:pressed{\n"
" padding-top:15px;\n"
" padding-left:15px;\n"
" color:rgb(91,88,53);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(21, 18, 21, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(45, 45))
        self.label_6.setMaximumSize(QtCore.QSize(45, 45))
        self.label_6.setStyleSheet("background-color:rgb(142,176,27);\n"
"border-radius:21px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(45, 45))
        self.label_5.setMaximumSize(QtCore.QSize(45, 45))
        self.label_5.setStyleSheet("background-color:rgb(45,45,45);\n"
"border-radius:21px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(45, 45))
        self.label_4.setMaximumSize(QtCore.QSize(45, 45))
        self.label_4.setStyleSheet("background-color:rgb(142,176,27);\n"
"border:10px solid rgb(45,45,45);\n"
"border-radius:40px")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(144,144,144);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_5.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lineEdit.setStyleSheet("background-color:rgb(31,31,31);\n"
"border-radius:10px;\n"
"color:rgb(144,144,144);\n"
"padding-left:15px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.widget_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color:rgb(45,45,45);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 60))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(45,45,45);\n"
"border-bottom-left-radius:40px;\n"
"border-bottom-right-radius:40px;\n"
"color:rgb(144,144,144);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "miniproject"))
        self.pushButton.setText(_translate("Form", "-"))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", "✕"))
        self.pushButton_5.setText(_translate("Form", ""))
        self.pushButton_4.setText(_translate("Form", ""))
        self.pushButton_6.setText(_translate("Form", "⟳"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Developed by juhwan"))

