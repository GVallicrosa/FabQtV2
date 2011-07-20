# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advancedDialog.ui'
#
# Created: Tue Jul 19 12:41:04 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_advancedDialog(object):
    def setupUi(self, advancedDialog):
        advancedDialog.setObjectName(_fromUtf8("advancedDialog"))
        advancedDialog.resize(368, 326)
        self.verticalLayout = QtGui.QVBoxLayout(advancedDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.activateRaft = QtGui.QGroupBox(advancedDialog)
        self.activateRaft.setAutoFillBackground(False)
        self.activateRaft.setCheckable(True)
        self.activateRaft.setObjectName(_fromUtf8("activateRaft"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.activateRaft)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addRaft = QtGui.QCheckBox(self.activateRaft)
        self.addRaft.setChecked(True)
        self.addRaft.setObjectName(_fromUtf8("addRaft"))
        self.verticalLayout_2.addWidget(self.addRaft)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.activateRaft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.baseDensity = QtGui.QDoubleSpinBox(self.activateRaft)
        self.baseDensity.setSingleStep(0.1)
        self.baseDensity.setProperty(_fromUtf8("value"), 0.5)
        self.baseDensity.setObjectName(_fromUtf8("baseDensity"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.baseDensity)
        self.label_3 = QtGui.QLabel(self.activateRaft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.baseOver = QtGui.QDoubleSpinBox(self.activateRaft)
        self.baseOver.setSingleStep(0.1)
        self.baseOver.setProperty(_fromUtf8("value"), 2.0)
        self.baseOver.setObjectName(_fromUtf8("baseOver"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.baseOver)
        self.label_4 = QtGui.QLabel(self.activateRaft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.baseLayers = QtGui.QSpinBox(self.activateRaft)
        self.baseLayers.setProperty(_fromUtf8("value"), 1)
        self.baseLayers.setObjectName(_fromUtf8("baseLayers"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.baseLayers)
        self.label_5 = QtGui.QLabel(self.activateRaft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.interfaceDensity = QtGui.QDoubleSpinBox(self.activateRaft)
        self.interfaceDensity.setSingleStep(0.1)
        self.interfaceDensity.setProperty(_fromUtf8("value"), 0.5)
        self.interfaceDensity.setObjectName(_fromUtf8("interfaceDensity"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.interfaceDensity)
        self.label_6 = QtGui.QLabel(self.activateRaft)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.interfaceOver = QtGui.QDoubleSpinBox(self.activateRaft)
        self.interfaceOver.setSingleStep(0.1)
        self.interfaceOver.setProperty(_fromUtf8("value"), 1.0)
        self.interfaceOver.setObjectName(_fromUtf8("interfaceOver"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.interfaceOver)
        self.label_7 = QtGui.QLabel(self.activateRaft)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.interfaceLayers = QtGui.QSpinBox(self.activateRaft)
        self.interfaceLayers.setProperty(_fromUtf8("value"), 2)
        self.interfaceLayers.setObjectName(_fromUtf8("interfaceLayers"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.interfaceLayers)
        self.label_8 = QtGui.QLabel(self.activateRaft)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_8)
        self.raftMargin = QtGui.QDoubleSpinBox(self.activateRaft)
        self.raftMargin.setProperty(_fromUtf8("value"), 3.0)
        self.raftMargin.setObjectName(_fromUtf8("raftMargin"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.raftMargin)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.activateRaft)
        self.buttonBox = QtGui.QDialogButtonBox(advancedDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(advancedDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), advancedDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), advancedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(advancedDialog)

    def retranslateUi(self, advancedDialog):
        advancedDialog.setWindowTitle(QtGui.QApplication.translate("advancedDialog", "Advanced Path Planning", None, QtGui.QApplication.UnicodeUTF8))
        self.activateRaft.setTitle(QtGui.QApplication.translate("advancedDialog", "Activate Raft", None, QtGui.QApplication.UnicodeUTF8))
        self.addRaft.setText(QtGui.QApplication.translate("advancedDialog", "Add Raft, Elevate Nozzle, Orbit and Set Altitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("advancedDialog", "Base Infill Density (ratio):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("advancedDialog", "Base Layer Thickness over Layer Thickness:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("advancedDialog", "Base Layers (integer):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("advancedDialog", "Interface Infill Density (ratio):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("advancedDialog", "Interface Layer Thickness over Layer Thickness:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("advancedDialog", "Interface Layers (integer):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("advancedDialog", "Raft Margin (mm):", None, QtGui.QApplication.UnicodeUTF8))

