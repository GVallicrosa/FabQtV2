# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertiesDialog.ui'
#
# Created: Mon Aug 23 16:05:11 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_propertiesDialog(object):
    def setupUi(self, propertiesDialog):
        propertiesDialog.setObjectName("propertiesDialog")
        propertiesDialog.resize(338, 221)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(propertiesDialog.sizePolicy().hasHeightForWidth())
        propertiesDialog.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtGui.QVBoxLayout(propertiesDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.modelMaterialComboBox = QtGui.QComboBox(propertiesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelMaterialComboBox.sizePolicy().hasHeightForWidth())
        self.modelMaterialComboBox.setSizePolicy(sizePolicy)
        self.modelMaterialComboBox.setObjectName("modelMaterialComboBox")
        self.horizontalLayout.addWidget(self.modelMaterialComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(propertiesDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.x_translate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.x_translate.setMaximum(200.0)
        self.x_translate.setProperty("value", 0.0)
        self.x_translate.setObjectName("x_translate")
        self.gridLayout.addWidget(self.x_translate, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setText("Y")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.y_translate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.y_translate.setMaximum(200.0)
        self.y_translate.setObjectName("y_translate")
        self.gridLayout.addWidget(self.y_translate, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setText("Z")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.z_translate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.z_translate.setMaximum(200.0)
        self.z_translate.setObjectName("z_translate")
        self.gridLayout.addWidget(self.z_translate, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setText("X")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line_2 = QtGui.QFrame(propertiesDialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setText("X")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.x_rotate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.x_rotate.setMinimum(-360.0)
        self.x_rotate.setMaximum(360.0)
        self.x_rotate.setProperty("value", 0.0)
        self.x_rotate.setObjectName("x_rotate")
        self.gridLayout_2.addWidget(self.x_rotate, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setText("Y")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.y_rotate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.y_rotate.setMinimum(-360.0)
        self.y_rotate.setMaximum(360.0)
        self.y_rotate.setObjectName("y_rotate")
        self.gridLayout_2.addWidget(self.y_rotate, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setText("Z")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.z_rotate = QtGui.QDoubleSpinBox(propertiesDialog)
        self.z_rotate.setMinimum(-360.0)
        self.z_rotate.setMaximum(360.0)
        self.z_rotate.setObjectName("z_rotate")
        self.gridLayout_2.addWidget(self.z_rotate, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_3 = QtGui.QFrame(propertiesDialog)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setText("X")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.x_scale = QtGui.QDoubleSpinBox(propertiesDialog)
        self.x_scale.setDecimals(4)
        self.x_scale.setMaximum(9.9)
        self.x_scale.setProperty("value", 1.0)
        self.x_scale.setObjectName("x_scale")
        self.gridLayout_3.addWidget(self.x_scale, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setText("Y")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.y_scale = QtGui.QDoubleSpinBox(propertiesDialog)
        self.y_scale.setDecimals(4)
        self.y_scale.setMaximum(9.9)
        self.y_scale.setProperty("value", 1.0)
        self.y_scale.setObjectName("y_scale")
        self.gridLayout_3.addWidget(self.y_scale, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(propertiesDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setText("Z")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.z_scale = QtGui.QDoubleSpinBox(propertiesDialog)
        self.z_scale.setDecimals(4)
        self.z_scale.setMaximum(9.9)
        self.z_scale.setProperty("value", 1.0)
        self.z_scale.setObjectName("z_scale")
        self.gridLayout_3.addWidget(self.z_scale, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(propertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(propertiesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), propertiesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), propertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(propertiesDialog)

    def retranslateUi(self, propertiesDialog):
        propertiesDialog.setWindowTitle(QtGui.QApplication.translate("propertiesDialog", "Model Properties Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("propertiesDialog", "Model Material:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("propertiesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Enter new position [mm]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("propertiesDialog", "Translate to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("propertiesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Rotation in every axis [degrees]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("propertiesDialog", "Rotate:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("propertiesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">Scale in every axis (&lt;1 reduce; &gt;1 grow)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("propertiesDialog", "Scale:", None, QtGui.QApplication.UnicodeUTF8))
