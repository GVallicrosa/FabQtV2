#!/usr/bin/env python

import os
import platform
import sys
import vtk
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui.ui_fabqtDialog as ui_fabqtDialog
#import ui.ui_aboutDialog as ui_aboutDialog
#import ui.ui_toolDialog as ui_toolDialog

from core.python.about import *
from core.python.tools import *
from core.python.properties import *
from core.python.printer import *


class FabQtMain(QMainWindow, ui_fabqtDialog.Ui_MainWindow):
    def __init__(self, parent = None):
        print '\nInitialising application...'
        super(FabQtMain, self).__init__(parent)
        self.setupUi(self)

## Initial values
        self.configToolName = None
        self.configPrinterName = None
        self.toolList = loadTools()
        self.printerList = loadPrinters()
        self.actorDict = dict()

## Config tree and comboboxes
        self.loadConfigTree()
        self.populateToolComboBox()
        
## Render window
        self.camera = vtk.vtkCamera()
        self.camera.SetFocalPoint(100, 100, 0)
        self.camera.SetPosition(400, 100, 120)
        self.camera.SetViewUp(-1, 0, 0)
        self.ren = vtk.vtkRenderer()
        self.ren.SetActiveCamera(self.camera)
        #self.qvtkWidget.SetInteractorStyle(None) ################## Disables interaction with the 3D window
        self.qvtkWidget.GetRenderWindow().AddRenderer(self.ren)
        boundBox = vtk.vtkSTLReader()
        boundBox.SetFileName('config/boudCube.stl')
        boundBoxMapper = vtk.vtkPolyDataMapper()
        boundBoxMapper.SetInput(boundBox.GetOutput())
        boundBoxActor = vtk.vtkActor()
        boundBoxActor.SetMapper(boundBoxMapper)
        self.ren.AddActor(boundBoxActor)
        self.qvtkWidget.Initialize()
        self.qvtkWidget.GetRenderWindow().Render()
        self.qvtkWidget.Start()    
        
## Import model file dialog
        self.importDialog = QFileDialog(self, 'Import model', settings.value("Path/ModelDir", QVariant(QString('./'))).toString(), 
            "3D Models (*.STL *.stl);;All files (*)")
        self.connect(self.importDialog, SIGNAL('fileSelected(QString)'), self.importModel)
        
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
        self.connect(self.actionImport, SIGNAL("triggered()"), self.showImportDialog)
        self.connect(self.importModelButton, SIGNAL("clicked()"), self.showImportDialog)

## Context menus
        self.connect(self.modelTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showModelCustomContextMenu)
        self.connect(self.configTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showConfigCustomContextMenu)

## The config tool context menu
        self.toolMenu = QMenu()
        actionEditTool = self.toolMenu.addAction("Edit Tool")
        actionNewTool = self.toolMenu.addAction("New Tool")
        self.connect(actionEditTool, SIGNAL('triggered()'), self.editToolDialog)
        self.connect(actionNewTool, SIGNAL('triggered()'), self.newToolDialog)
        self.toolMenu.addAction(actionEditTool)
        self.toolMenu.addSeparator()
        self.toolMenu.addAction(actionNewTool)
        
## The config printer context menu
        self.printerMenu = QMenu()
        actionEditPrinter = self.printerMenu.addAction("Edit Printer")
        actionNewPrinter = self.printerMenu.addAction("New Printer")
        self.connect(actionEditPrinter, SIGNAL('triggered()'), self.editPrinterDialog)
        self.connect(actionNewPrinter, SIGNAL('triggered()'), self.newPrinterDialog)
        self.printerMenu.addAction(actionEditPrinter)
        self.printerMenu.addSeparator()
        self.printerMenu.addAction(actionNewPrinter)

## The model context menu
        self.modelMenu = QMenu()
        actionProperties = self.modelMenu.addAction("Properties/Transform")
        actionStandard = self.modelMenu.addAction("Standard Path Planning")
        actionAdvanced = self.modelMenu.addAction("Advanced Path Planning")
        actionOrigin = self.modelMenu.addAction("Move to Origin")
        actionDelete = self.modelMenu.addAction("Delete")
        self.connect(actionProperties, SIGNAL('triggered()'), self.showPropertiesDialog)
#        self.connect(actionStandard, SIGNAL('triggered()'), self.???)
#        self.connect(actionAdvanced, SIGNAL('triggered()'), self.???)
        self.connect(actionOrigin, SIGNAL('triggered()'), self.moveToOrigin)
        self.connect(actionDelete, SIGNAL('triggered()'), self.deleteModel)
        self.modelMenu.addAction(actionProperties)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionStandard)
        self.modelMenu.addAction(actionAdvanced)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionOrigin)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionDelete)

## Translations (en, ca, es_ES, pt_BR)
        self.connect(self.actionEnglish, SIGNAL("triggered()"), self.set_en)
        self.connect(self.actionSpanish_Spain, SIGNAL("triggered()"), self.set_es_ES)
        self.connect(self.actionCatalan, SIGNAL("triggered()"), self.set_ca)
        self.connect(self.actionPortuguese_Brazil, SIGNAL("triggered()"), self.set_pt_BR)
        print '\n* End Initialisation'

    def closeEvent(self, event): # Save some settings before closing
        print 'Entered main window close event'
        if self.okToContinue():
            print '* Saving Settings before closing'
            settings = QSettings()
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position",QVariant(self.pos()))
            settings.setValue("MainWindow/State",QVariant(self.saveState()))
#            settings.setValue("Printer/Printer", QVariant())
#            settings.setValue("Printer/Tool1", QVariant())
#            settings.setValue("Printer/Tool2", QVariant())
#            settings.setValue("Printer/PrinterPort", QVariant())
#            settings.setValue("Path/ModelDir", QVariant())
            print '* Closing...'
        else:
            event.ignore()
            
    def deleteModel(self):
        #delete from view, dictionary and reload model tree
        self.ren.RemoveActor(self.actorDict[str(self.model)])
        self.actorDict.pop(str(self.model))
        self.loadModelTree()        
    
    def editPrinterDialog(self):
        print 'Edit printer'
        self.showPrinterDialog(False)
        
    def editToolDialog(self):
        print 'Edit tool'
        self.showToolDialog(False)
        
    def importModel(self, fname):
        fname = str(fname)
        settings.setValue("Path/ModelDir", QVariant(fname[0:fname.find(fname.split('/')[-1])]))
        print '++ Importing model: ' + fname.split('/')[-1]
        extension = fname.split('.')[1]
        if extension == 'STL' or  extension == 'stl': 
            stl = vtk.vtkSTLReader()
            stl.SetFileName(str(fname))
            stlMapper = vtk.vtkPolyDataMapper()
            stlMapper.SelectColorArray(2)
            stlMapper.SetInput(stl.GetOutput())
            modActor = vtk.vtkActor()
            modActor.SetMapper(stlMapper)
            modActor.GetProperty().SetColor(random.random(), random.random(), random.random())
        elif extension == '3ds': ## Need to know what actor is added
            mod = vtk.vtk3DSImporter()
            mod.ComputeNormalsOn()
            mod.SetFileName(str(fname))
            mod.Read()
            #3ds.SetRenderWindow(renWin)
        if not str(fname.split('/')[-1]) in self.actorDict.keys():
            self.actorDict[str(fname.split('/')[-1])] = modActor
        else:
            print '++ Model name already used'
            exists = True
            name = str(fname.split('/')[-1])
            num = 2
            while exists:
                if not name + '(%s)' % str(num) in self.actorDict.keys():
                    print '++ New name: ' + name + '(%s)' % str(num)
                    self.actorDict[name + '(%s)' % str(num)] = modActor
                    exists = False
                else:
                    num += 1
        self.ren.AddActor(modActor)
        self.loadModelTree() 

    def loadConfigTree(self):
        print 'Delete config tree'
        self.configTreeWidget.clear()
        print 'Loading tools in config tree'
        self.loadToolTree()
        print 'Loading printers in config tree'
        self.loadPrinterTree()

    def loadModelTree(self):
        print 'Loading/Reloading model tree'
        self.modelTreeWidget.clear()
        for model in self.actorDict.keys():
            print 'Adding model: ' + model
            modelItem = QTreeWidgetItem(self.modelTreeWidget)
            modelItem.setText(0, model)
            
    def loadPrinterTree(self):
        self.printerTree = QTreeWidgetItem(self.configTreeWidget)
        self.printerTree.setText(0, "Printers")
        for printer in self.printerList:
            print 'Adding printer: ' + printer.name
            actualPrinter = QTreeWidgetItem(self.printerTree)
            actualPrinter.setText(0, printer.name)
    
    def loadToolTree(self):
        self.toolTree = QTreeWidgetItem(self.configTreeWidget)
        self.toolTree.setText(0, "Tools")
        for tool in self.toolList:
            if not tool.name == '## No Tool ##':
                print 'Adding tool: ' + tool.name
                self.actualTool = QTreeWidgetItem(self.toolTree)
                self.actualTool.setText(0, tool.name);
                next = QStringList('TIPDIAM')
                next.append(QString(tool.tipDiam))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('SYRDIAM')
                next.append(QString(tool.syrDiam))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('PATHWIDTH')
                next.append(QString(tool.pathWidth))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('PATHHEIGHT')
                next.append(QString(tool.pathHeight))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('JOGSPEED')
                next.append(QString(tool.jogSpeed))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('SUCKBACK')
                next.append(QString(tool.suckback))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('PUSHOUT')
                next.append(QString(tool.pushout))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('PATHSPEED')
                next.append(QString(tool.pathSpeed))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('PAUSEPATHS')
                next.append(QString(tool.pausePaths))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('CLEARANCE')
                next.append(QString(tool.clearance))
                self.actualTool.addChild(QTreeWidgetItem(next))
                next = QStringList('DEPRATE')
                next.append(QString(tool.depRate))
                self.actualTool.addChild(QTreeWidgetItem(next))

    def moveToOrigin(self):
        print 'Moved to Origin'
        self.actorDict[str(self.model)].SetPosition(0,0,0)
        
    def newPrinterDialog(self):
        print 'New printer'
        self.showPrinterDialog(True)
        
    def newToolDialog(self):
        print 'New tool'
        self.showToolDialog(True)

    def okToContinue(self): # To implement not saved changes closing
        return True

    def on_mainDock_closeEvent(self, event): # It never enters here, I don't know why (it could be a solution to the dock problem)
        print '***Entered mainDock close event!!' # For testing
        self.actionMain_tools.setChecked(False)
        event.accept()

    def populateToolComboBox(self):
        self.syringe1ComboBox.clear()
        self.syringe2ComboBox.clear()
        for tool in self.toolList:
            self.syringe1ComboBox.addItem(tool.name)
            self.syringe2ComboBox.addItem(tool.name)
            self.syringe1ComboBox.setCurrentIndex(-1) # The no tool
            self.syringe2ComboBox.setCurrentIndex(-1)

###### I don't like this solution for the translation
    def set_ca(self):
        self.updateTranslation('ca')
        print '* Changed language to Catalan'
    def set_en(self):
        self.updateTranslation('en')
        print '* Changed language to English'
    def set_es_ES(self):
        self.updateTranslation('es_ES')
        print '* Changed language to Spanish'
    def set_pt_BR(self):
        self.updateTranslation('pt_BR')
        print '* Changed language to Portuguese'
###### End translation

    def showAboutDialog(self):
        dialog = aboutDialog(self)
        dialog.exec_()

    def showConfigCustomContextMenu(self, pos):
        index = self.configTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return
        item = self.configTreeWidget.itemAt(pos)
        try:
            if item.parent().text(0) == 'Tools': # if it has parent, it is a slice, not a model
                self.configToolName = item.text(0)
                print 'Clicked on tool: ' + str(self.configToolName)
                self.toolMenu.exec_(QCursor.pos())
            elif item.parent().text(0) == 'Printers':
                self.configPrinterName = item.text(0)
                print 'Clicked on printer: ' + str(self.configPrinterName)
                self.printerMenu.exec_(QCursor.pos())
            else:
                return
        except AttributeError:
            return

        
    def showImportDialog(self):
        self.importDialog.exec_()

    def showModelCustomContextMenu(self, pos):
        index = self.modelTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return 
        item = self.modelTreeWidget.itemAt(pos) 
        if item.parent(): # if it has parent, it is a slice, not a model
            return
        self.model = item.text(0)
        self.modelMenu.exec_(QCursor.pos())
        
    def showPropertiesDialog(self):
        dialog = propertiesDialog(self, self.model, self.actorDict, self.toolList)
        dialog.exec_()
        
    def showPrinterDialog(self, new):
        print '** Showing printer edit dialog'
        if new:
            dialog = printerDialog(self)
        else:
            printer = loadPrinter(self.configPrinterName + '.printer')
            dialog = printerDialog(self, printer)
        dialog.exec_()
        self.printerList = loadPrinters()
        #self.populatePrinterCombobox()
        self.loadConfigTree()

    def showToolDialog(self, new):
        print '** Showing tool edit dialog'
        if new:
            print '*** New Tool'
            dialog = toolDialog(self)
        else:
            print '*** Edit Tool'
            tool = loadTool(self.configToolName + '.tool')
            dialog = toolDialog(self, tool)
        dialog.exec_() 
        self.toolList = loadTools()
        self.populateToolComboBox() # Reload data for comboboxes and tool tree
        self.loadConfigTree()

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

    def updateTranslation(self,lang):
        settings.setValue("Language",QVariant('languages/fabqt_' + lang))
        QMessageBox().about(self, self.tr("Translation Info"),self.tr("You need to restart the application to change the language"))
        print '* Language changed: you need to restart the application to apply changes'

## Execution of main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("FabQt") # Need to save settings
    app.setOrganizationName("FabQt") # Need to save settings

    settings = QSettings()

    translator = QTranslator()
    translator.load(settings.value("Language",QVariant(QString("languages/fabqt_en"))).toString())
    app.installTranslator(translator)
    lang = settings.value("Language",QVariant(QString("languages/fabqt_en"))).toString()

    form = FabQtMain()
    form.show()
    form.updateDialogs()
    if lang == "languages/fabqt_en":
        form.actionEnglish.setChecked(True)
    elif lang == "languages/fabqt_es_ES":
        form.actionSpanish.setChecked(True)
    elif lang == "languages/fabqt_ca":
        form.actionCatalan.setChecked(True)
    elif lang == "languages/fabqt_pt_BR":
        form.actionPortuguese_Brazil.setChecked(True)

    app.exec_()
