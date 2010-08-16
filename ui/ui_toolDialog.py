# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolDialog.ui'
#
# Created: Mon Aug 16 11:52:59 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_toolDlg(object):
    def setupUi(self, toolDlg):
        toolDlg.setObjectName("toolDlg")
        toolDlg.resize(556, 245)
        self.verticalLayout = QtGui.QVBoxLayout(toolDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(toolDlg)
        self.label.setText("Tool Name:")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.toolNameLineEdit = QtGui.QLineEdit(toolDlg)
        self.toolNameLineEdit.setObjectName("toolNameLineEdit")
        self.gridLayout.addWidget(self.toolNameLineEdit, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(toolDlg)
        self.label_8.setText("SuckBack:")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.suckBackLineEdit = QtGui.QLineEdit(toolDlg)
        self.suckBackLineEdit.setObjectName("suckBackLineEdit")
        self.gridLayout.addWidget(self.suckBackLineEdit, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(toolDlg)
        self.label_2.setText("Tip Diameter:")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tipDiameterLineEdit = QtGui.QLineEdit(toolDlg)
        self.tipDiameterLineEdit.setObjectName("tipDiameterLineEdit")
        self.gridLayout.addWidget(self.tipDiameterLineEdit, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(toolDlg)
        self.label_7.setText("Pushout:")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.pushoutLineEdit = QtGui.QLineEdit(toolDlg)
        self.pushoutLineEdit.setObjectName("pushoutLineEdit")
        self.gridLayout.addWidget(self.pushoutLineEdit, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(toolDlg)
        self.label_3.setText("Syringe Diameter:")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.syringeDiameterLineEdit = QtGui.QLineEdit(toolDlg)
        self.syringeDiameterLineEdit.setObjectName("syringeDiameterLineEdit")
        self.gridLayout.addWidget(self.syringeDiameterLineEdit, 2, 1, 1, 1)
        self.pathSpeedLineEdit = QtGui.QLineEdit(toolDlg)
        self.pathSpeedLineEdit.setObjectName("pathSpeedLineEdit")
        self.gridLayout.addWidget(self.pathSpeedLineEdit, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(toolDlg)
        self.label_4.setText("Path Width:")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pathWidthLineEdit = QtGui.QLineEdit(toolDlg)
        self.pathWidthLineEdit.setObjectName("pathWidthLineEdit")
        self.gridLayout.addWidget(self.pathWidthLineEdit, 3, 1, 1, 1)
        self.pausePathsLineEdit = QtGui.QLineEdit(toolDlg)
        self.pausePathsLineEdit.setAcceptDrops(False)
        self.pausePathsLineEdit.setInputMask("")
        self.pausePathsLineEdit.setText("")
        self.pausePathsLineEdit.setObjectName("pausePathsLineEdit")
        self.gridLayout.addWidget(self.pausePathsLineEdit, 3, 3, 1, 1)
        self.label_5 = QtGui.QLabel(toolDlg)
        self.label_5.setText("Path Height:")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pathHeightLineEdit = QtGui.QLineEdit(toolDlg)
        self.pathHeightLineEdit.setObjectName("pathHeightLineEdit")
        self.gridLayout.addWidget(self.pathHeightLineEdit, 4, 1, 1, 1)
        self.clearanceLineEdit = QtGui.QLineEdit(toolDlg)
        self.clearanceLineEdit.setObjectName("clearanceLineEdit")
        self.gridLayout.addWidget(self.clearanceLineEdit, 4, 3, 1, 1)
        self.label_9 = QtGui.QLabel(toolDlg)
        self.label_9.setText("Jog Speed:")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.jogSpeedLineEdit = QtGui.QLineEdit(toolDlg)
        self.jogSpeedLineEdit.setObjectName("jogSpeedLineEdit")
        self.gridLayout.addWidget(self.jogSpeedLineEdit, 5, 1, 1, 1)
        self.depositionLineEdit = QtGui.QLineEdit(toolDlg)
        self.depositionLineEdit.setObjectName("depositionLineEdit")
        self.gridLayout.addWidget(self.depositionLineEdit, 5, 3, 1, 1)
        self.label_14 = QtGui.QLabel(toolDlg)
        self.label_14.setText("Path Speed:")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.label_13 = QtGui.QLabel(toolDlg)
        self.label_13.setText("Clearance:")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)
        self.label_15 = QtGui.QLabel(toolDlg)
        self.label_15.setText("Pause Paths:")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 2, 1, 1)
        self.label_12 = QtGui.QLabel(toolDlg)
        self.label_12.setText("Deposition Rate:")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.toolButtonBox = QtGui.QDialogButtonBox(toolDlg)
        self.toolButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.toolButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.toolButtonBox.setCenterButtons(True)
        self.toolButtonBox.setObjectName("toolButtonBox")
        self.verticalLayout.addWidget(self.toolButtonBox)

        self.retranslateUi(toolDlg)
        QtCore.QObject.connect(self.toolButtonBox, QtCore.SIGNAL("accepted()"), toolDlg.accept)
        QtCore.QObject.connect(self.toolButtonBox, QtCore.SIGNAL("rejected()"), toolDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(toolDlg)
        toolDlg.setTabOrder(self.toolNameLineEdit, self.tipDiameterLineEdit)
        toolDlg.setTabOrder(self.tipDiameterLineEdit, self.syringeDiameterLineEdit)
        toolDlg.setTabOrder(self.syringeDiameterLineEdit, self.pathWidthLineEdit)
        toolDlg.setTabOrder(self.pathWidthLineEdit, self.pathHeightLineEdit)
        toolDlg.setTabOrder(self.pathHeightLineEdit, self.jogSpeedLineEdit)
        toolDlg.setTabOrder(self.jogSpeedLineEdit, self.suckBackLineEdit)
        toolDlg.setTabOrder(self.suckBackLineEdit, self.pushoutLineEdit)
        toolDlg.setTabOrder(self.pushoutLineEdit, self.pathSpeedLineEdit)
        toolDlg.setTabOrder(self.pathSpeedLineEdit, self.pausePathsLineEdit)
        toolDlg.setTabOrder(self.pausePathsLineEdit, self.clearanceLineEdit)
        toolDlg.setTabOrder(self.clearanceLineEdit, self.depositionLineEdit)
        toolDlg.setTabOrder(self.depositionLineEdit, self.toolButtonBox)

    def retranslateUi(self, toolDlg):
        toolDlg.setWindowTitle(QtGui.QApplication.translate("toolDlg", "Tool Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("toolDlg", "Material name and color of the tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("toolDlg", "[seconds] early dispensing to start flow quickly", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("toolDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Internal tip diameter [mm]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">----------------------------------------</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Olive - 1.54 ||         Blue - 0.41</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amber - 1.36 ||    Orange - 0.33</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Grey - 1.19 ||          Red - 0.25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Green - 0.84 ||       Clear - 0.20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Pink - 0.61 || Lavender - 0.15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Purple - 0.51 ||     Yellow - 0.10</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("toolDlg", "[seconds] reverse plunger motion to stop flow quickly", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("toolDlg", "Internal syringe diameter [mm]\n"
"Diameter of the filament in extrusion [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("toolDlg", "Width of stream of material deposited [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("toolDlg", "Heigth of layers of material deposited [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(QtGui.QApplication.translate("toolDlg", "Stepper motor frequency [Hz]\n"
"(11400 for default motors)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setToolTip(QtGui.QApplication.translate("toolDlg", "[mm/s] speed along paths when depositing material", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setToolTip(QtGui.QApplication.translate("toolDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[mm] between the last layer and the tip when tranversing</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(usually two times path heigth)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setToolTip(QtGui.QApplication.translate("toolDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[mm] plunger motiom per [mm] path length</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(orientative value calculated from others)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

