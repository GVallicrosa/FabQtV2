#!/usr/bin/env python

import os
import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui.ui_fabqtDialog as ui_fabqtDialog
import ui.ui_aboutDialog as ui_aboutDialog
import ui.ui_toolDialog as ui_toolDialog
#import ui.resources_rc as ui.resources_rc

from core.python.classes import *

class FabQtMain(QMainWindow, ui_fabqtDialog.Ui_MainWindow):
    def __init__(self, parent = None):
        super(FabQtMain, self).__init__(parent)
        self.setupUi(self)

## Initial values
        self.configToolName = None

## Load preferences (called at the main loop)
        self.resize(settings.value("MainWindow/Size",QVariant(QSize(600, 500))).toSize())
        self.move(settings.value("MainWindow/Position",QVariant(QPoint(0, 0))).toPoint())
        self.restoreState(settings.value("MainWindow/State").toByteArray());

## Show/hide dialogs from the menu
        self.connect(self.actionMain_tools, SIGNAL("toggled(bool)"), self.mainDock.setVisible)
        self.connect(self.actionStatus_Info, SIGNAL("toggled(bool)"), self.infoDock.setVisible)
        self.connect(self.actionToolbar, SIGNAL("toggled(bool)"), self.toolBar.setVisible)

## If you close a dialog, update in the menu
        self.connect(self.mainDock, SIGNAL("visibilityChanged(bool)"), self.actionMain_tools.setChecked) # PROBLEM: when minimized, it loses the docks
        self.connect(self.infoDock, SIGNAL("visibilityChanged(bool)"), self.actionStatus_Info.setChecked)

## Update movements
        self.connect(self.x_IncrementLineEdit, SIGNAL("textEdited(QString)"), self.updateMovement)
        self.connect(self.y_IncrementLineEdit, SIGNAL("textEdited(QString)"), self.updateMovement)
        self.connect(self.z_IncrementLineEdit, SIGNAL("textEdited(QString)"), self.updateMovement)
        self.connect(self.u_IncrementLineEdit, SIGNAL("textEdited(QString)"), self.updateMovement)
        self.connect(self.v_IncrementLineEdit, SIGNAL("textEdited(QString)"), self.updateMovement)

## General actions
        self.connect(self.actionQuit, SIGNAL("triggered()"), self.close)
        self.connect(self.actionAbout, SIGNAL("triggered()"), self.showAboutDialog)
        self.connect(self.actionImport, SIGNAL("triggered()"), self.startPrinting)
        self.connect(self.importModelButton, SIGNAL("triggered()"), self.startPrinting)

## Context menus
        self.connect(self.modelTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showModelCustomContextMenu)
        self.connect(self.configTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showConfigCustomContextMenu)

## The config context menu
        self.toolMenu = QMenu()
        actionEditTool = self.toolMenu.addAction("Edit Tool")
        actionNewTool = self.toolMenu.addAction("New Tool")
        self.connect(actionEditTool, SIGNAL('triggered()'), self.showToolDialog)
        self.connect(actionNewTool, SIGNAL('triggered()'), self.showToolDialog)
        self.toolMenu.addAction(actionEditTool)
        self.toolMenu.addSeparator()
        self.toolMenu.addAction(actionNewTool)

## The model context menu
        self.modelMenu = QMenu()
        actionProperties = self.modelMenu.addAction("Properties")
        actionStandard = self.modelMenu.addAction("Standard Path Planning")
        actionAdvanced = self.modelMenu.addAction("Advanced Path Planning")
        actionTranslate = self.modelMenu.addAction("Translate")
        actionRotate = self.modelMenu.addAction("Rotate")
        actionScale = self.modelMenu.addAction("Scale")
        actionOrigin = self.modelMenu.addAction("Move to Origin")
#        self.connect(actionProperties, SIGNAL('triggered()'), self.???) # How to have the item clicked??
#        self.connect(actionStandard, SIGNAL('triggered()'), self.???)
#        self.connect(actionAdvanced, SIGNAL('triggered()'), self.???)
#        self.connect(actionTranslate, SIGNAL('triggered()'), self.???)
#        self.connect(actionRotate, SIGNAL('triggered()'), self.???)
#        self.connect(actionScale, SIGNAL('triggered()'), self.???)
#        self.connect(actionOrigin, SIGNAL('triggered()'), self.???)
        self.modelMenu.addAction(actionProperties)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionStandard)
        self.modelMenu.addAction(actionAdvanced)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionTranslate)
        self.modelMenu.addAction(actionRotate)
        self.modelMenu.addAction(actionScale)
        self.modelMenu.addAction(actionOrigin)

## Translations (en, ca, es_ES, pt_BR)
        self.connect(self.actionEnglish, SIGNAL("triggered()"), self.set_en)
        self.connect(self.actionSpanish_Spain, SIGNAL("triggered()"), self.set_es_ES)
        self.connect(self.actionCatalan, SIGNAL("triggered()"), self.set_ca)
        self.connect(self.actionPortuguese_Brazil, SIGNAL("triggered()"), self.set_pt_BR)

    ## I don't like this solution for the translation
    def set_en(self):
        self.updateTranslation('en')
    def set_es_ES(self):
        self.updateTranslation('es_ES')
    def set_ca(self):
        self.updateTranslation('ca')
    def set_pt_BR(self):
        self.updateTranslation('pt_BR')

    def updateTranslation(self,lang):
        settings.setValue("Language",QVariant('languages/fabqt_' + lang))
        QMessageBox().about(self, self.tr("Translation Info"),self.tr("You need to restart the application to change the language"))

    def closeEvent(self, event): # Save some settings before closing
        if self.okToContinue():
            settings = QSettings()
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position",QVariant(self.pos()))
            settings.setValue("MainWindow/State",QVariant(self.saveState()))
        else:
            event.ignore()

    def okToContinue(self): # To implement not saved changes closing
        return True

    @pyqtSignature("QCloseEvent")
    def on_mainDock_closeEvent(self, event): # It never enters here, I don't know why (it could be a solution to the dock problem)
        print '***Entered close event!!' # For testing
        self.actionMain_tools.setChecked(False)
        event.accept()

    def showAboutDialog(self):
        dialog = aboutDialog(self)
        dialog.exec_()

    def showConfigCustomContextMenu(self, pos):
        index = self.configTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return 
        item = self.configTreeWidget.itemAt(pos) 
        #if not item.parent() == 'Tools': # if it has parent, it is a slice, not a model
         #   return
        #self.configToolName = item.text(0)
        self.toolMenu.exec_(QCursor.pos())

    def showModelCustomContextMenu(self, pos):
        index = self.modelTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return 
        item = self.modelTreeWidget.itemAt(pos) 
        if item.parent(): # if it has parent, it is a slice, not a model
            return
        name = item.text(0)
        self.modelMenu.exec_(QCursor.pos())

    def showToolDialog(self):
        print '*** Showing tool edit dialog'
        if self.configToolName is not None: # Editing a tool
            print '*** Edit Tool'
            pass
        else: # New tool
            print '*** New Tool'
            dialog = toolDialog(self)
            dialog.exec_()

    def startPrinting(self): # need to be implemented
        pass

    def updateDialogs(self): # Needed at the startup
        self.actionMain_tools.setChecked(self.mainDock.isVisible())
        self.actionStatus_Info.setChecked(self.infoDock.isVisible())
        self.actionToolbar.setChecked(self.toolBar.isVisible())

    def updateMovement(self):
        self.x_Commanded.setSingleStep(self.x_IncrementLineEdit.text().toDouble()[0]) # 0 because returns two elements
        self.y_Commanded.setSingleStep(self.y_IncrementLineEdit.text().toDouble()[0])
        self.z_Commanded.setSingleStep(self.z_IncrementLineEdit.text().toDouble()[0])
        self.u_Commanded.setSingleStep(self.u_IncrementLineEdit.text().toDouble()[0])
        self.v_Commanded.setSingleStep(self.v_IncrementLineEdit.text().toDouble()[0])

## Execution of main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("FabQt") # Need to save settings
    app.setOrganizationName("FabQt") # Need to save settings

    settings = QSettings()

    translator = QTranslator()
    translator.load(settings.value("Language",QVariant(QString("languages/fabqt_en"))).toString())
    app.installTranslator(translator)

    form = FabQtMain()
    form.show()
    form.updateDialogs()
    app.exec_()
