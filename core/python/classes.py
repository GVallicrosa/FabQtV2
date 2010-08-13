from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui.ui_aboutDialog as ui_aboutDialog
import ui.ui_toolDialog as ui_toolDialog
from core.python.functions import *

class aboutDialog(QDialog, ui_aboutDialog.Ui_AboutDlg):
    def __init__(self, parent = None):
        super(aboutDialog, self).__init__(parent)
        self.setupUi(self)

class Tool(object):
    def __init__(self, name = None, tipDiam = None, syrDiam = None, pathWidth = None, pathHeight = None, jogSpeed = None, suckback = None, pushout = None, pathSpeed = None, pausePaths = None, clearance = None, depRate = None):
        self.name = name
        self.tipDiam = tipDiam
        self.syrDiam = syrDiam
        self.pathWidth = pathWidth
        self.pathHeight = pathHeight
        self.jogSpeed = jogSpeed
        self.suckback = suckback
        self.pushout = pushout
        self.pathSpeed = pathSpeed
        self.pausePaths = pausePaths
        self.clearance = clearance
        self.depRate = depRate

class toolDialog(QDialog, ui_toolDialog.Ui_toolDlg):
    def __init__(self, parent = None, toolObject = None, newTool = True):
        super(toolDialog, self).__init__(parent)
        self.setupUi(self)
        if not newTool: # if you edit you cannot change the tool name, and load the parameters
            self.toolNameLineEdit.setEnabled(False)
            self.toolNameLineEdit.setText(toolObject.name)
            self.tipDiameterLineEdit.setText(toolObject.tipDiam)
            self.syringeDiameterLineEdit.setText(toolObject.syrDiam)
            self.pathWidthLineEdit.setText(toolObject.pathWidth)
            self.pathHeightLineEdit.setText(toolObject.pathHeight)
            self.jogSpeedLineEdit.setText(toolObject.jogSpeed)
            self.suckBackLineEdit.setText(toolObject.suckback)
            self.pushoutLineEdit.setText(toolObject.pushout)
            self.pathSpeedLineEdit.setText(toolObject.pathSpeed)
            self.pausePathsLineEdit.setText(toolObject.pausePaths)
            self.clearanceLineEdit.setText(toolObject.clearance)
            self.depositionLineEdit.setText(toolObject.depRate)
        else:
            toolObject = Tool()
        self.toolObject = toolObject
        self.newTool = newTool

## Enable only to write numbers on the parameters
        self.tipDiameterLineEdit.setValidator(QDoubleValidator(0.000,10.000, 6, self.tipDiameterLineEdit));
        self.syringeDiameterLineEdit.setValidator(QDoubleValidator(0,10, 6,self.syringeDiameterLineEdit));
        self.pathWidthLineEdit.setValidator(QDoubleValidator(0,10, 6,self.pathWidthLineEdit));
        self.pathHeightLineEdit.setValidator(QDoubleValidator(0,10, 6,self.pathHeightLineEdit));
        self.jogSpeedLineEdit.setValidator(QIntValidator (1, 20000, self.jogSpeedLineEdit));
        self.suckBackLineEdit.setValidator(QDoubleValidator(0,10, 6,self.suckBackLineEdit));
        self.pushoutLineEdit.setValidator(QDoubleValidator(0,10, 6,self.pushoutLineEdit));
        self.pathSpeedLineEdit.setValidator(QDoubleValidator(0,10, 6,self.pathSpeedLineEdit));
        self.pausePathsLineEdit.setValidator(QIntValidator (1, 10000, self.pausePathsLineEdit));
        self.clearanceLineEdit.setValidator(QDoubleValidator(0,10, 6, self.clearanceLineEdit));
        self.depositionLineEdit.setValidator(QDoubleValidator(0,10, 6,self.depositionLineEdit));

    def accept(self):
        if self.verify():
            self.toolObject = self.updateTool(self.toolObject)
            saveTool(self.toolObject, self.newTool)
            self.close()
        else:
            QMessageBox().about(self, self.tr("Error"),self.tr("Not all paramaters are filled"))

    def updateTool(self, tool):
            tool.name = self.toolNameLineEdit.text()
            tool.tipDiam = self.tipDiameterLineEdit.text()
            tool.syrDiam = self.syringeDiameterLineEdit.text()
            tool.pathWidth = self.pathWidthLineEdit.text()
            tool.pathHeight = self.pathHeightLineEdit.text()
            tool.jogSpeed = self.jogSpeedLineEdit.text()
            tool.suckback = self.suckBackLineEdit.text()
            tool.pushout = self.pushoutLineEdit.text()
            tool.pathSpeed = self.pathSpeedLineEdit.text()
            tool.pausePaths = self.pausePathsLineEdit.text()
            tool.clearance = self.clearanceLineEdit.text()
            tool.depRate = self.depositionLineEdit.text()
            return tool
        

    def verify(self):
        if self.toolNameLineEdit.text().isEmpty() or self.tipDiameterLineEdit.text().isEmpty() or self.syringeDiameterLineEdit.text().isEmpty() or self.pathWidthLineEdit.text().isEmpty() or self.pathHeightLineEdit.text().isEmpty() or self.jogSpeedLineEdit.text().isEmpty() or self.suckBackLineEdit.text().isEmpty() or self.pushoutLineEdit.text().isEmpty() or self.pathSpeedLineEdit.text().isEmpty() or self.pausePathsLineEdit.text().isEmpty() or self.clearanceLineEdit.text().isEmpty() or self.depositionLineEdit.text().isEmpty():
            return False
        else:
            return True
