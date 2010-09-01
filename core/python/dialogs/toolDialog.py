from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QDialogButtonBox, QDoubleValidator, QIntValidator, QMessageBox
from core.python.tool import Tool
import ui.ui_toolDialog as ui_toolDialog

class toolDialog(QDialog, ui_toolDialog.Ui_toolDlg):
    def __init__(self, parent = None, tool = None):
        super(toolDialog, self).__init__(parent)
        self.setupUi(self)
        saveAs = self.toolButtonBox.addButton('Save As', QDialogButtonBox.ActionRole)
        self.connect(saveAs, SIGNAL('clicked(bool)'), self.nameChangeable)
        if tool is not None: # if you edit you cannot change the tool name, and load the parameters
            self.toolNameLineEdit.setEnabled(False)
            self.toolNameLineEdit.setText(tool.name)
            self.tipDiameterLineEdit.setText(tool.tipDiam)
            self.syringeDiameterLineEdit.setText(tool.syrDiam)
            self.pathWidthLineEdit.setText(tool.pathWidth)
            self.pathHeightLineEdit.setText(tool.pathHeight)
            self.jogSpeedLineEdit.setText(tool.jogSpeed)
            self.suckBackLineEdit.setText(tool.suckback)
            self.pushoutLineEdit.setText(tool.pushout)
            self.pathSpeedLineEdit.setText(tool.pathSpeed)
            self.pausePathsLineEdit.setText(tool.pausePaths)
            self.clearanceLineEdit.setText(tool.clearance)
            self.depositionLineEdit.setText(tool.depRate)
            self.new = False
            saveAs.setEnabled(True)
        else:
            tool = Tool()
            self.new = True
            saveAs.setEnabled(False)
        self.tool = tool
        ## Enable only to write numbers on the parameters
        self.tipDiameterLineEdit.setValidator(QDoubleValidator(0.000, 10.000, 6, self.tipDiameterLineEdit))
        self.syringeDiameterLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.syringeDiameterLineEdit))
        self.pathWidthLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.pathWidthLineEdit))
        self.pathHeightLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.pathHeightLineEdit))
        self.jogSpeedLineEdit.setValidator(QIntValidator (1, 20000, self.jogSpeedLineEdit))
        self.suckBackLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.suckBackLineEdit))
        self.pushoutLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.pushoutLineEdit))
        self.pathSpeedLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.pathSpeedLineEdit))
        self.pausePathsLineEdit.setValidator(QIntValidator (1, 10000, self.pausePathsLineEdit))
        self.clearanceLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.clearanceLineEdit))
        self.depositionLineEdit.setValidator(QDoubleValidator(0, 10, 6, self.depositionLineEdit))

    def accept(self):
        if self.verify():
            self.tool = self.updateTool(self.tool)
            if self.tool.save(self.new):
                self.tool = None
                self.close()
            else:
                QMessageBox().about(self, self.tr("Error"), self.tr("Tool with same name already exists.\nChange the tool name."))
        else:
            QMessageBox().about(self, self.tr("Error"), self.tr("Not all paramaters are filled"))

    def nameChangeable(self):
        self.toolNameLineEdit.setEnabled(True)
        self.newTool = True

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
        if (self.toolNameLineEdit.text().isEmpty() or self.tipDiameterLineEdit.text().isEmpty() or
            self.syringeDiameterLineEdit.text().isEmpty() or self.pathWidthLineEdit.text().isEmpty() or
            self.pathHeightLineEdit.text().isEmpty() or self.jogSpeedLineEdit.text().isEmpty() or
            self.suckBackLineEdit.text().isEmpty() or self.pushoutLineEdit.text().isEmpty() or
            self.pathSpeedLineEdit.text().isEmpty() or self.pausePathsLineEdit.text().isEmpty() or
            self.clearanceLineEdit.text().isEmpty() or self.depositionLineEdit.text().isEmpty()):
            return False
        else:
            return True
