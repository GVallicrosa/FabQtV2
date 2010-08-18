from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *

import os
import codecs

import ui.ui_toolDialog as ui_toolDialog

CODEC = "UTF-8"

def loadTool(fname):
    tool = Tool()
    tool.name = fname.split('.')[0]
    fh = QFile('tools/' + fname)
    fh.open(QIODevice.ReadOnly)
    dom = QDomDocument()
    dom.setContent(fh)
    fh.close()
    root = dom.documentElement()
    if root.tagName() != "TOOL":
        raise ValueError, "not a Tool XML file"
    tool.tipDiam = str(root.attribute("TIPDIAM"))
    tool.syrDiam = str(root.attribute("SYRDIAM"))
    tool.pathWidth = str(root.attribute("PATHWIDTH"))
    tool.pathHeight = str(root.attribute("PATHHEIGHT"))
    tool.jogSpeed = str(root.attribute("JOGSPEED"))
    tool.suckback = str(root.attribute("SUCKBACK"))
    tool.pushout = str(root.attribute("PUSHOUT"))
    tool.pathSpeed = str(root.attribute("PATHSPEED"))
    tool.pausePaths = str(root.attribute("PAUSEPATHS"))
    tool.clearance = str(root.attribute("CLEARANCE"))
    tool.depRate = str(root.attribute("DEPOSITIONRATE")) 
    return tool

def loadTools(): # look /tools and call loadTool to parse it, the put all in a list
    print '** Loading tools'
    dirList=os.listdir('tools/')
    toolList = list()
#    toolList.insert(-1, Tool('## No Tool ##'))
    for fname in dirList:
        if fname[-5:] == '.tool':
            toolList.insert(-1, loadTool(fname))
            print '*** Loading tool: ' + fname.split('.')[0]
    print '** Finished loading tools\n'
    return toolList

def saveTool(tool, newTool):
    fh = QFile('tools/' + tool.name + '.tool')
    if newTool and fh.exists():
        return False
    if fh.open(QIODevice.WriteOnly):
        stream = QTextStream(fh)
        stream.setCodec(CODEC)
        stream << ("<?xml version='1.0' encoding='%s'?>\n<!DOCTYPE TOOL>\n<TOOL\n" % CODEC)
        stream << ("TIPDIAM='%s'\nSYRDIAM='%s'\nPATHWIDTH='%s'\nPATHHEIGHT='%s'\nJOGSPEED='%s'\nSUCKBACK='%s'\nPUSHOUT='%s'\nPATHSPEED='%s'\nPAUSEPATHS='%s'\nCLEARANCE='%s'\nDEPOSITIONRATE='%s'\n>" % (tool.tipDiam, tool.syrDiam, tool.pathWidth, tool.pathHeight, tool.jogSpeed, tool.suckback, tool.pushout, tool.pathSpeed, tool.pausePaths, tool.clearance, tool.depRate))
        stream << ("\n</TOOL>")
        fh.close()
    return True

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
    def __init__(self, parent = None, toolObject = None):
        super(toolDialog, self).__init__(parent)
        self.setupUi(self)
        saveAs = self.toolButtonBox.addButton('Save As',QDialogButtonBox.ActionRole)
        self.connect(saveAs, SIGNAL('clicked(bool)'), self.nameChangeable)
        if toolObject is not None: # if you edit you cannot change the tool name, and load the parameters
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
            self.newTool = False
            saveAs.setEnabled(True)
        else:
            toolObject = Tool()
            self.newTool = True
            saveAs.setEnabled(False)
        self.toolObject = toolObject
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
            if saveTool(self.toolObject, self.newTool):
                self.toolObject = None
                self.close()
            else:
                QMessageBox().about(self, self.tr("Error"),self.tr("Tool with same name already exists.\nChange the tool name."))
        else:
            QMessageBox().about(self, self.tr("Error"),self.tr("Not all paramaters are filled"))

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
        if self.toolNameLineEdit.text().isEmpty() or self.tipDiameterLineEdit.text().isEmpty() or self.syringeDiameterLineEdit.text().isEmpty() or self.pathWidthLineEdit.text().isEmpty() or self.pathHeightLineEdit.text().isEmpty() or self.jogSpeedLineEdit.text().isEmpty() or self.suckBackLineEdit.text().isEmpty() or self.pushoutLineEdit.text().isEmpty() or self.pathSpeedLineEdit.text().isEmpty() or self.pausePathsLineEdit.text().isEmpty() or self.clearanceLineEdit.text().isEmpty() or self.depositionLineEdit.text().isEmpty():
            return False
        else:
            return True
