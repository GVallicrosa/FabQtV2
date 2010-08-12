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
        self.connect(self.toolButtonBox, SIGNAL("accepted()"), self.verifyAndSave) # Apply to write tool if all things are entered and correct
        print '*** Tool dialog initialized'

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
        

    def verifyAndSave(self):
        print '*** Veryfy and save'

        if not self.toolNameLineEdit.text().isEmpty() and not self.tipDiameterLineEdit.text().isEmpty() and not self.syringeDiameterLineEdit.text        ().isEmpty() and not self.pathWidthLineEdit.text().isEmpty() and not self.pathHeightLineEdit.text().isEmpty() and not self.jogSpeedLineEdit.text().isEmpty() and not self.suckBackLineEdit.text().isEmpty() and not self.pushoutLineEdit.text().isEmpty() and not self.pathSpeedLineEdit.text().isEmpty() and not self.pausePathsLineEdit.text().isEmpty() and not self.clearanceLineEdit.text().isEmpty() and not self.depositionLineEdit.text().isEmpty():

            self.toolObject = self.updateTool(self.toolObject)
            saveTool(self.toolObject, self.newTool)
        else:
            print 'Cannot close'

