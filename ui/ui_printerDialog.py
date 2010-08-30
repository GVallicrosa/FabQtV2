# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printerDialog.ui'
#
# Created: Fri Aug 27 09:32:58 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_printerDlg(object):
    def setupUi(self, printerDlg):
        printerDlg.setObjectName("printerDlg")
        printerDlg.resize(338, 441)
        self.verticalLayout_8 = QtGui.QVBoxLayout(printerDlg)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtGui.QTabWidget(printerDlg)
        self.tabWidget.setObjectName("tabWidget")
        self.general = QtGui.QWidget()
        self.general.setObjectName("general")
        self.verticalLayout = QtGui.QVBoxLayout(self.general)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtGui.QLabel(self.general)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.printerNameLineEdit = QtGui.QLineEdit(self.general)
        self.printerNameLineEdit.setObjectName("printerNameLineEdit")
        self.horizontalLayout.addWidget(self.printerNameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.general)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtGui.QLabel(self.general)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.updatePeriodLineEdit = QtGui.QLineEdit(self.general)
        self.updatePeriodLineEdit.setObjectName("updatePeriodLineEdit")
        self.gridLayout_3.addWidget(self.updatePeriodLineEdit, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.general)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.jogSpeedLineEdit = QtGui.QLineEdit(self.general)
        self.jogSpeedLineEdit.setObjectName("jogSpeedLineEdit")
        self.gridLayout_3.addWidget(self.jogSpeedLineEdit, 1, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.general)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.maxToolsLineEdit = QtGui.QLineEdit(self.general)
        self.maxToolsLineEdit.setObjectName("maxToolsLineEdit")
        self.gridLayout_3.addWidget(self.maxToolsLineEdit, 2, 1, 1, 3)
        self.label_4 = QtGui.QLabel(self.general)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 2)
        self.toolLimitLineEdit = QtGui.QLineEdit(self.general)
        self.toolLimitLineEdit.setObjectName("toolLimitLineEdit")
        self.gridLayout_3.addWidget(self.toolLimitLineEdit, 3, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.general)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.maxAccelLineEdit = QtGui.QLineEdit(self.general)
        self.maxAccelLineEdit.setObjectName("maxAccelLineEdit")
        self.gridLayout_3.addWidget(self.maxAccelLineEdit, 4, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.line_2 = QtGui.QFrame(self.general)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.general)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.general)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.yMaxLineEdit = QtGui.QLineEdit(self.general)
        self.yMaxLineEdit.setObjectName("yMaxLineEdit")
        self.gridLayout.addWidget(self.yMaxLineEdit, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.general)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.zMaxLineEdit = QtGui.QLineEdit(self.general)
        self.zMaxLineEdit.setObjectName("zMaxLineEdit")
        self.gridLayout.addWidget(self.zMaxLineEdit, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.general)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 3)
        self.xMaxLineEdit = QtGui.QLineEdit(self.general)
        self.xMaxLineEdit.setObjectName("xMaxLineEdit")
        self.gridLayout.addWidget(self.xMaxLineEdit, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.general, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 2)
        self.baseDirection = QtGui.QLineEdit(self.tab)
        self.baseDirection.setObjectName("baseDirection")
        self.gridLayout_4.addWidget(self.baseDirection, 0, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 2)
        self.baseMotor = QtGui.QLineEdit(self.tab)
        self.baseMotor.setObjectName("baseMotor")
        self.gridLayout_4.addWidget(self.baseMotor, 1, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 2)
        self.baseRange = QtGui.QLineEdit(self.tab)
        self.baseRange.setObjectName("baseRange")
        self.gridLayout_4.addWidget(self.baseRange, 2, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 2)
        self.baseLimit = QtGui.QLineEdit(self.tab)
        self.baseLimit.setObjectName("baseLimit")
        self.gridLayout_4.addWidget(self.baseLimit, 3, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 4, 0, 1, 2)
        self.baseIncrement = QtGui.QLineEdit(self.tab)
        self.baseIncrement.setObjectName("baseIncrement")
        self.gridLayout_4.addWidget(self.baseIncrement, 4, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 5, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 2)
        self.xDirection = QtGui.QLineEdit(self.tab_3)
        self.xDirection.setObjectName("xDirection")
        self.gridLayout_5.addWidget(self.xDirection, 0, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 2)
        self.xMotor = QtGui.QLineEdit(self.tab_3)
        self.xMotor.setObjectName("xMotor")
        self.gridLayout_5.addWidget(self.xMotor, 1, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 2)
        self.xRange = QtGui.QLineEdit(self.tab_3)
        self.xRange.setObjectName("xRange")
        self.gridLayout_5.addWidget(self.xRange, 2, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 3, 0, 1, 2)
        self.xLimit = QtGui.QLineEdit(self.tab_3)
        self.xLimit.setObjectName("xLimit")
        self.gridLayout_5.addWidget(self.xLimit, 3, 2, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 4, 0, 1, 2)
        self.xIncrement = QtGui.QLineEdit(self.tab_3)
        self.xIncrement.setObjectName("xIncrement")
        self.gridLayout_5.addWidget(self.xIncrement, 4, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 5, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_25 = QtGui.QLabel(self.tab_4)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 0, 0, 1, 2)
        self.yDirection = QtGui.QLineEdit(self.tab_4)
        self.yDirection.setObjectName("yDirection")
        self.gridLayout_6.addWidget(self.yDirection, 0, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_4)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 2)
        self.yMotor = QtGui.QLineEdit(self.tab_4)
        self.yMotor.setObjectName("yMotor")
        self.gridLayout_6.addWidget(self.yMotor, 1, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_4)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 2, 0, 1, 2)
        self.yRange = QtGui.QLineEdit(self.tab_4)
        self.yRange.setObjectName("yRange")
        self.gridLayout_6.addWidget(self.yRange, 2, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_4)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 3, 0, 1, 2)
        self.yLimit = QtGui.QLineEdit(self.tab_4)
        self.yLimit.setObjectName("yLimit")
        self.gridLayout_6.addWidget(self.yLimit, 3, 2, 1, 1)
        self.label_29 = QtGui.QLabel(self.tab_4)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 4, 0, 1, 2)
        self.yIncrement = QtGui.QLineEdit(self.tab_4)
        self.yIncrement.setObjectName("yIncrement")
        self.gridLayout_6.addWidget(self.yIncrement, 4, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 5, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_30 = QtGui.QLabel(self.tab_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 2)
        self.zDirection = QtGui.QLineEdit(self.tab_5)
        self.zDirection.setObjectName("zDirection")
        self.gridLayout_7.addWidget(self.zDirection, 0, 2, 1, 1)
        self.label_31 = QtGui.QLabel(self.tab_5)
        self.label_31.setObjectName("label_31")
        self.gridLayout_7.addWidget(self.label_31, 1, 0, 1, 2)
        self.zMotor = QtGui.QLineEdit(self.tab_5)
        self.zMotor.setObjectName("zMotor")
        self.gridLayout_7.addWidget(self.zMotor, 1, 2, 1, 1)
        self.label_32 = QtGui.QLabel(self.tab_5)
        self.label_32.setObjectName("label_32")
        self.gridLayout_7.addWidget(self.label_32, 2, 0, 1, 2)
        self.zRange = QtGui.QLineEdit(self.tab_5)
        self.zRange.setObjectName("zRange")
        self.gridLayout_7.addWidget(self.zRange, 2, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.tab_5)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 3, 0, 1, 2)
        self.zLimit = QtGui.QLineEdit(self.tab_5)
        self.zLimit.setObjectName("zLimit")
        self.gridLayout_7.addWidget(self.zLimit, 3, 2, 1, 1)
        self.label_34 = QtGui.QLabel(self.tab_5)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 4, 0, 1, 2)
        self.zIncrement = QtGui.QLineEdit(self.tab_5)
        self.zIncrement.setObjectName("zIncrement")
        self.gridLayout_7.addWidget(self.zIncrement, 4, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 5, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_7)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_35 = QtGui.QLabel(self.tab_6)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 0, 0, 1, 2)
        self.uDirection = QtGui.QLineEdit(self.tab_6)
        self.uDirection.setObjectName("uDirection")
        self.gridLayout_8.addWidget(self.uDirection, 0, 2, 1, 1)
        self.label_36 = QtGui.QLabel(self.tab_6)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 1, 0, 1, 2)
        self.uMotor = QtGui.QLineEdit(self.tab_6)
        self.uMotor.setObjectName("uMotor")
        self.gridLayout_8.addWidget(self.uMotor, 1, 2, 1, 1)
        self.label_37 = QtGui.QLabel(self.tab_6)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 2, 0, 1, 2)
        self.uRange = QtGui.QLineEdit(self.tab_6)
        self.uRange.setObjectName("uRange")
        self.gridLayout_8.addWidget(self.uRange, 2, 2, 1, 1)
        self.label_38 = QtGui.QLabel(self.tab_6)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 3, 0, 1, 2)
        self.uLimit = QtGui.QLineEdit(self.tab_6)
        self.uLimit.setObjectName("uLimit")
        self.gridLayout_8.addWidget(self.uLimit, 3, 2, 1, 1)
        self.label_39 = QtGui.QLabel(self.tab_6)
        self.label_39.setObjectName("label_39")
        self.gridLayout_8.addWidget(self.label_39, 4, 0, 1, 2)
        self.uIncrement = QtGui.QLineEdit(self.tab_6)
        self.uIncrement.setObjectName("uIncrement")
        self.gridLayout_8.addWidget(self.uIncrement, 4, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 5, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_8)
        self.tabWidget.addTab(self.tab_6, "")
        self.vAxisTab = QtGui.QWidget()
        self.vAxisTab.setObjectName("vAxisTab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.vAxisTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_40 = QtGui.QLabel(self.vAxisTab)
        self.label_40.setObjectName("label_40")
        self.gridLayout_9.addWidget(self.label_40, 0, 0, 1, 2)
        self.vDirection = QtGui.QLineEdit(self.vAxisTab)
        self.vDirection.setObjectName("vDirection")
        self.gridLayout_9.addWidget(self.vDirection, 0, 2, 1, 1)
        self.label_41 = QtGui.QLabel(self.vAxisTab)
        self.label_41.setObjectName("label_41")
        self.gridLayout_9.addWidget(self.label_41, 1, 0, 1, 2)
        self.vMotor = QtGui.QLineEdit(self.vAxisTab)
        self.vMotor.setObjectName("vMotor")
        self.gridLayout_9.addWidget(self.vMotor, 1, 2, 1, 1)
        self.label_42 = QtGui.QLabel(self.vAxisTab)
        self.label_42.setObjectName("label_42")
        self.gridLayout_9.addWidget(self.label_42, 2, 0, 1, 2)
        self.vRange = QtGui.QLineEdit(self.vAxisTab)
        self.vRange.setObjectName("vRange")
        self.gridLayout_9.addWidget(self.vRange, 2, 2, 1, 1)
        self.label_43 = QtGui.QLabel(self.vAxisTab)
        self.label_43.setObjectName("label_43")
        self.gridLayout_9.addWidget(self.label_43, 3, 0, 1, 2)
        self.vLimit = QtGui.QLineEdit(self.vAxisTab)
        self.vLimit.setObjectName("vLimit")
        self.gridLayout_9.addWidget(self.vLimit, 3, 2, 1, 1)
        self.label_44 = QtGui.QLabel(self.vAxisTab)
        self.label_44.setObjectName("label_44")
        self.gridLayout_9.addWidget(self.label_44, 4, 0, 1, 2)
        self.vIncrement = QtGui.QLineEdit(self.vAxisTab)
        self.vIncrement.setObjectName("vIncrement")
        self.gridLayout_9.addWidget(self.vIncrement, 4, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem8, 5, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.vAxisTab, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.printerButtonBox = QtGui.QDialogButtonBox(printerDlg)
        self.printerButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.printerButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.printerButtonBox.setObjectName("printerButtonBox")
        self.verticalLayout_8.addWidget(self.printerButtonBox)

        self.retranslateUi(printerDlg)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.printerButtonBox, QtCore.SIGNAL("accepted()"), printerDlg.accept)
        QtCore.QObject.connect(self.printerButtonBox, QtCore.SIGNAL("rejected()"), printerDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(printerDlg)
        printerDlg.setTabOrder(self.tabWidget, self.printerButtonBox)
        printerDlg.setTabOrder(self.printerButtonBox, self.printerNameLineEdit)
        printerDlg.setTabOrder(self.printerNameLineEdit, self.updatePeriodLineEdit)
        printerDlg.setTabOrder(self.updatePeriodLineEdit, self.jogSpeedLineEdit)
        printerDlg.setTabOrder(self.jogSpeedLineEdit, self.maxToolsLineEdit)
        printerDlg.setTabOrder(self.maxToolsLineEdit, self.toolLimitLineEdit)
        printerDlg.setTabOrder(self.toolLimitLineEdit, self.maxAccelLineEdit)
        printerDlg.setTabOrder(self.maxAccelLineEdit, self.xMaxLineEdit)
        printerDlg.setTabOrder(self.xMaxLineEdit, self.yMaxLineEdit)
        printerDlg.setTabOrder(self.yMaxLineEdit, self.zMaxLineEdit)
        printerDlg.setTabOrder(self.zMaxLineEdit, self.baseDirection)
        printerDlg.setTabOrder(self.baseDirection, self.baseMotor)
        printerDlg.setTabOrder(self.baseMotor, self.baseRange)
        printerDlg.setTabOrder(self.baseRange, self.baseLimit)
        printerDlg.setTabOrder(self.baseLimit, self.baseIncrement)
        printerDlg.setTabOrder(self.baseIncrement, self.xDirection)
        printerDlg.setTabOrder(self.xDirection, self.xMotor)
        printerDlg.setTabOrder(self.xMotor, self.xRange)
        printerDlg.setTabOrder(self.xRange, self.xLimit)
        printerDlg.setTabOrder(self.xLimit, self.xIncrement)
        printerDlg.setTabOrder(self.xIncrement, self.yDirection)
        printerDlg.setTabOrder(self.yDirection, self.yMotor)
        printerDlg.setTabOrder(self.yMotor, self.yRange)
        printerDlg.setTabOrder(self.yRange, self.yLimit)
        printerDlg.setTabOrder(self.yLimit, self.yIncrement)
        printerDlg.setTabOrder(self.yIncrement, self.zDirection)
        printerDlg.setTabOrder(self.zDirection, self.zMotor)
        printerDlg.setTabOrder(self.zMotor, self.zRange)
        printerDlg.setTabOrder(self.zRange, self.zLimit)
        printerDlg.setTabOrder(self.zLimit, self.zIncrement)
        printerDlg.setTabOrder(self.zIncrement, self.uDirection)
        printerDlg.setTabOrder(self.uDirection, self.uMotor)
        printerDlg.setTabOrder(self.uMotor, self.uRange)
        printerDlg.setTabOrder(self.uRange, self.uLimit)
        printerDlg.setTabOrder(self.uLimit, self.uIncrement)
        printerDlg.setTabOrder(self.uIncrement, self.vDirection)
        printerDlg.setTabOrder(self.vDirection, self.vMotor)
        printerDlg.setTabOrder(self.vMotor, self.vRange)
        printerDlg.setTabOrder(self.vRange, self.vLimit)
        printerDlg.setTabOrder(self.vLimit, self.vIncrement)

    def retranslateUi(self, printerDlg):
        printerDlg.setWindowTitle(QtGui.QApplication.translate("printerDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setToolTip(QtGui.QApplication.translate("printerDlg", "Name to identify the printer configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("printerDlg", "Printer name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Time that the micro-controller communicates with the software [ms]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("printerDlg", "Status update period:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Speed when no deposition [mm/s]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("printerDlg", "Jog speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("printerDlg", "Tools that can be mounted at the same time, usually 1 or 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("printerDlg", "Max tools:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("printerDlg", "Tool limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("printerDlg", "[mm/s²]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("printerDlg", "Max accel:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("printerDlg", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("printerDlg", "X axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("printerDlg", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("printerDlg", "Y axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(QtGui.QApplication.translate("printerDlg", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("printerDlg", "Z axis:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("printerDlg", "Maximum printing dimensions:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general), QtGui.QApplication.translate("printerDlg", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("printerDlg", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("printerDlg", "X axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("printerDlg", "Y axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("printerDlg", "Z axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("printerDlg", "U axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">D</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">irection vector for movement</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Z is 0 0 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">     for Y is 1 0 1 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("printerDlg", "Direction:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">Axis direction +-[mm] per (1/8) step</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("printerDlg", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("printerDlg", "Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">+</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">direction -direction (0 -&gt; limit switch not connected; 1 if it is)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("printerDlg", "Limit switch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setToolTip(QtGui.QApplication.translate("printerDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"internal-source-marker_0.4259963477961719\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">[</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:#000000;\">mm] default distance to move plunger in manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("printerDlg", "Increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vAxisTab), QtGui.QApplication.translate("printerDlg", "V axis", None, QtGui.QApplication.UnicodeUTF8))

