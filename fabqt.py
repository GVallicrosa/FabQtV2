#!/usr/bin/env python
from __future__ import division
import sys
import os
import vtk
from time import localtime, asctime
# Import Qt
from PyQt4.QtCore import QString, QUrl, QVariant, QSettings, QTranslator, QStringList, QSize, QPoint, SIGNAL, QStringList
from PyQt4.QtGui import QTreeWidgetItem, QApplication, QMenu, QMainWindow, QFileDialog, QCursor, QMessageBox
# Dialogs
import ui.ui_fabqtDialog as ui_fabqtDialog
from core.python.dialogs.printerDialog import printerDialog
from core.python.dialogs.propertiesDialog import propertiesDialog
from core.python.dialogs.toolDialog import toolDialog
from core.python.dialogs.aboutDialog import aboutDialog
from core.python.dialogs.advancedDialog import advancedDialog
# All other modules needed
from core.python.advancedOptions import Options
from core.python.tool import loadTools
from core.python.printer import loadPrinters
from core.python.render import generateAxes, moveToOrigin, validateMove
from core.python.model import Model
from core.python import printerports
from core.python.taskexecutor import ThreadPool
import core.python.skeinmod as skeinmod
from core.python.fablog import Fablog

if os.path.exists('log.txt'):
    if os.path.getsize('log.txt') >= 1024*1024: # 1MB
        os.remove('log.txt')

logger = Fablog()
logger.log('\n\n' + str(asctime(localtime())) + '\n')

class FabQtMain(QMainWindow, ui_fabqtDialog.Ui_MainWindow):
    def __init__(self, parent = None):
        ## Init parent and make connections
        super(FabQtMain, self).__init__(parent)
        self.setupUi(self)
        self.connect(logger, SIGNAL('Fablogging'), self.logText)
        logger.log('--> Initialising application')
        ## Initial values
        self.configToolName = None
        self.configPrinterName = None
        self.model = None
        self.toolDict = loadTools() # toolname: Tool()
        self.printerDict = loadPrinters() # printername: Printer()
        self.modelDict = dict() # modelname: Model()
        self.options = Options() # advanced path options
        ## Config tree and comboboxes, load initial values
        self.loadConfigTree()
        self.populateToolComboBox()
        self.populatePrinterComboBox()
        self.populatePrinterPort()
        self.currentPrinter = self.printerDict[str(self.printerComboBox.currentText())]
        ## Render window using VTK lib
        self.camera = vtk.vtkCamera()
        self.camera.SetFocalPoint(0, 0, 0)
        self.camera.SetPosition(300, 0, 100)
        self.camera.SetViewUp(-1, 0, 0)
        #self.camera.SetParallelProjection(1)#######
        self.ren = vtk.vtkRenderer()
        self.ren.SetActiveCamera(self.camera)
        self.qvtkWidget.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.qvtkWidget.GetRenderWindow().AddRenderer(self.ren)
        ## Building table representation
        base = vtk.vtkCubeSource()
        xmax, ymax, zmax = self.currentPrinter.getPrintingDimensions()
        base.SetBounds(-xmax/2, xmax/2, -ymax/2, ymax/2, -5, 0)
        baseMapper = vtk.vtkPolyDataMapper()
        baseMapper.SetInput(base.GetOutput())
        baseActor = vtk.vtkActor()
        baseActor.SetMapper(baseMapper)
        baseActor.PickableOff()
        ## Origin Axes
        axesActor, XActor, YActor, ZActor = generateAxes(self.currentPrinter)
        XActor.SetCamera(self.camera)
        YActor.SetCamera(self.camera)
        ZActor.SetCamera(self.camera)
        ## Add all initial actors
        self.ren.AddActor(baseActor)
        self.ren.AddActor(axesActor)
        self.ren.AddActor(XActor)
        self.ren.AddActor(YActor)
        self.ren.AddActor(ZActor)
        ## Start rendering
        self.qvtkWidget.Initialize()
        self.qvtkWidget.GetRenderWindow().Render()
        self.qvtkWidget.Start()    
## CONNECTIONS AND MENUS
        ## Import model file dialog
        self.importDialog = QFileDialog(self, 'Import model', settings.value("Path/ModelDir", QVariant(QString('./'))).toString(), 
            "3D Models (*.STL *.stl);;All files (*)")
        self.connect(self.importDialog, SIGNAL('fileSelected(QString)'), self.importModel)
        ## Load preferences (called at the main loop)
        self.resize(settings.value("MainWindow/Size", QVariant(QSize(600, 500))).toSize())
        self.move(settings.value("MainWindow/Position", QVariant(QPoint(0, 0))).toPoint())
        self.restoreState(settings.value("MainWindow/State").toByteArray())
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
        ## Comboboxes
        self.connect(self.printerComboBox, SIGNAL("currentIndexChanged(QString"), self.updateCurrentPrinter)
        ## Double clicks   
        self.connect(self.modelTreeWidget, SIGNAL("doubleClicked(QModelIndex)"), self.modelDoubleClicked)   
        ## General actions
        self.connect(self.actionQuit, SIGNAL("triggered()"), self.close)
        self.connect(self.actionAbout, SIGNAL("triggered()"), self.showAboutDialog)
        self.connect(self.actionImport, SIGNAL("triggered()"), self.showImportDialog)
        self.connect(self.importModelButton, SIGNAL("clicked()"), self.showImportDialog)
        self.connect(self.resetViewButton, SIGNAL("clicked()"), self.resetView)
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
        actionDeletePath = self.modelMenu.addAction("Erase Path")
        actionOrigin = self.modelMenu.addAction("Move to Origin")
        actionDelete = self.modelMenu.addAction("Delete")
        self.connect(actionProperties, SIGNAL('triggered()'), self.showPropertiesDialog)
        self.connect(actionStandard, SIGNAL('triggered()'), self.pathPlanning) # testing save STL
        self.connect(actionAdvanced, SIGNAL('triggered()'), self.pathAdvanced)
        self.connect(actionDeletePath, SIGNAL('triggered()'), self.pathDelete)
        self.connect(actionOrigin, SIGNAL('triggered()'), self.moveToOrigin)
        self.connect(actionDelete, SIGNAL('triggered()'), self.deleteModel)
        self.modelMenu.addAction(actionProperties)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionStandard)
        self.modelMenu.addAction(actionAdvanced)
        self.modelMenu.addAction(actionDeletePath)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionOrigin)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionDelete)
        ## Translations (en, ca, es_ES, pt_BR)
        self.connect(self.actionEnglish, SIGNAL("triggered()"), self.set_en)
        self.connect(self.actionSpanish_Spain, SIGNAL("triggered()"), self.set_es_ES)
        self.connect(self.actionCatalan, SIGNAL("triggered()"), self.set_ca)
        self.connect(self.actionPortuguese_Brazil, SIGNAL("triggered()"), self.set_pt_BR)
        logger.log('--> End Initialisation')
        
    def closeEvent(self, event): # Save some settings before closing
        logger.log('Main window close event')
        if self.okToContinue():
            logger.log('Saving Settings before closing')
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position", QVariant(self.pos()))
            settings.setValue("MainWindow/State", QVariant(self.saveState()))
            settings.setValue("Printer/Printer", QVariant(self.printerComboBox.currentText()))
            settings.setValue("Printer/Tool1", QVariant(self.syringe1ComboBox.currentText()))
            settings.setValue("Printer/Tool2", QVariant(self.syringe2ComboBox.currentText()))
            settings.setValue("Printer/Port", QVariant(self.portComboBox.currentText()))
            logger.log('Closing...')
        else:
            event.ignore()
            
    def deleteModel(self):
        ''' Deletes the model from view and dictionary and reloads the model tree.'''
        self.ren.RemoveActor(self.model.readActor())
        self.ren.RemoveActor(self.model.getPathActor())
        self.ren.RemoveActor(self.model.getSupportPathActor())
        self.ren.RemoveActor(self.model.getBasePathActor())
        self.modelDict.pop(str(self.model.name))
        self.loadModelTree()        
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Deleted model: ' + self.model.name)
    
    def editPrinterDialog(self):
        '''Edits printer configuration, general options and axes options.'''
        logger.log('Edit printer Dialog')
        self.showPrinterDialog(False)
        
    def editToolDialog(self):
        logger.log('Edit tool Dialog')
        self.showToolDialog(False)
             
    def importModel(self, fname):
        fname = str(fname)
        settings.setValue("Path/ModelDir", QVariant(fname[0:fname.find(fname.split('/')[-1])]))
        model = Model()
        pool = ThreadPool(2) 
        pool.add_task(model.load(fname))
        if str(model.name) in self.modelDict.keys():
            logger.log('++ Model name already used')
            exists = True
            name = str(model.name)
            num = 2
            while exists:
                if not name + '(%s)' % str(num) in self.modelDict.keys():
                    logger.log('++ New name: ' + name + '(%s)' % str(num))
                    model.name = name + '(%s)' % str(num)
                    exists = False
                else:
                    num += 1
        self.modelDict[str(model.name)] = model
        printer = str(self.printerComboBox.currentText())
        printer = self.printerDict[printer]
        self.ren.AddActor(model.readActor())
        validateMove(model.readActor(), printer)
        self.qvtkWidget.GetRenderWindow().Render()
        self.loadModelTree()

    def loadConfigTree(self):
        logger.log('Delete config tree')
        self.configTreeWidget.clear()
        logger.log('Loading tools in config tree')
        self.loadToolTree()
        logger.log('Loading printers in config tree')
        self.loadPrinterTree()

    def loadModelTree(self):
        logger.log('Loading model tree')
        self.modelTreeWidget.clear()
        for model in self.modelDict.keys():
            logger.log('Adding model: ' + model)
            modelItem = QTreeWidgetItem(self.modelTreeWidget)
            modelItem.setText(0, model)
            modelItem.addChild(QTreeWidgetItem(QStringList('Model')))
            if self.modelDict[model].hasModelPath():
                modelItem.addChild(QTreeWidgetItem(QStringList('model_path')))
            if self.modelDict[model].hasSupportPath():
                modelItem.addChild(QTreeWidgetItem(QStringList('support_path')))
            if self.modelDict[model].hasBasePath():
                modelItem.addChild(QTreeWidgetItem(QStringList('base_path')))
        self.modelTreeWidget.expandAll()
            
    def loadPrinterTree(self):
        printerTree = QTreeWidgetItem(self.configTreeWidget)
        printerTree.setText(0, "Printers")
        for printer in self.printerDict.values():
            if not printer.name == '## No Printer ##':
                logger.log('Adding printer: ' + printer.name)
                actualPrinter = QTreeWidgetItem(printerTree)
                actualPrinter.setText(0, printer.name)
    
    def loadToolTree(self):
        toolTree = QTreeWidgetItem(self.configTreeWidget)
        toolTree.setText(0, "Tools")
        for tool in self.toolDict.values():
            if not tool.name == '## No Tool ##':
                logger.log('Adding tool: ' + tool.name)
                actualTool = QTreeWidgetItem(toolTree)
                actualTool.setText(0, tool.name)
                nextattirb = QStringList('TIPDIAM')
                nextattirb.append(QString(tool.tipDiam))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('SYRDIAM')
                nextattirb.append(QString(tool.syrDiam))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('PATHWIDTH')
                nextattirb.append(QString(tool.pathWidth))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('PATHHEIGHT')
                nextattirb.append(QString(tool.pathHeight))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('JOGSPEED')
                nextattirb.append(QString(tool.jogSpeed))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('SUCKBACK')
                nextattirb.append(QString(tool.suckback))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('PUSHOUT')
                nextattirb.append(QString(tool.pushout))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('PATHSPEED')
                nextattirb.append(QString(tool.pathSpeed))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('PAUSEPATHS')
                nextattirb.append(QString(tool.pausePaths))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('CLEARANCE')
                nextattirb.append(QString(tool.clearance))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                nextattirb = QStringList('DEPRATE')
                nextattirb.append(QString(tool.depRate))
                actualTool.addChild(QTreeWidgetItem(nextattirb))
                
    def logText(self, text):
        self.logTextBrowser.append(QString(text))

    def modelDoubleClicked(self, index):
        item = self.modelTreeWidget.itemFromIndex(index)
        if not item.parent(): # its a model
            modelName = item.text(0)
            logger.log('Double clicked on model: ' + modelName)
            model = self.modelDict[str(modelName)]
            actor = model.readActor()
            center = actor.GetCenter()
            self.camera.SetFocalPoint(center)
        else: # is 'Model' or 'Toolpath'
            parent = item.parent()
            modelName = parent.text(0)
            model = self.modelDict[str(modelName)]
            text = str(item.text(0))
            if text == 'Model':
                actor = model.readActor()
                num = actor.GetProperty().GetOpacity()
                if num == 0:
                    actor.GetProperty().SetOpacity(0.5)
                else:
                    actor.GetProperty().SetOpacity(0)
            elif text == 'model_path':
                actor = model.getPathActor()
                num = actor.GetProperty().GetOpacity()
                if num == 0:
                    actor.GetProperty().SetOpacity(1)
                else:
                    actor.GetProperty().SetOpacity(0)
            elif text == 'support_path':
                actor = model.getSupportPathActor()
                num = actor.GetProperty().GetOpacity()
                if num == 0:
                    actor.GetProperty().SetOpacity(1)
                else:
                    actor.GetProperty().SetOpacity(0)
            elif text == 'base_path':
                actor = model.getBasePathActor()
                num = actor.GetProperty().GetOpacity()
                if num == 0:
                    actor.GetProperty().SetOpacity(1)
                else:
                    actor.GetProperty().SetOpacity(0)
        self.qvtkWidget.GetRenderWindow().Render()

    def moveToOrigin(self):
        moveToOrigin(self.model.readActor())
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Moved to Origin, model: ' + self.model.name)

    def newPrinterDialog(self):
        logger.log('New printer Dialog')
        self.showPrinterDialog(True)
        
    def newToolDialog(self):
        logger.log('New tool Dialog')
        self.showToolDialog(True)

    def okToContinue(self): # To implement not saved changes closing
        logger.log("It's ok to continue")
        return True
        
    def on_mainDock_closeEvent(self, event): # It never enters here, I don't know why (it could be a solution to the dock problem)
        print 'Entered mainDock close event' # For testing
        self.actionMain_tools.setChecked(False)
        event.accept()
        
    def pathAdvanced(self):
        if self.model.readModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        else:
            logger.log('Starting advanced path planning')
            Dialog = advancedDialog(self, self.options)
            Dialog.exec_()
            skeinmod.applyConfig(self.model, self.toolDict, True, self.options)
            self.pathDelete()
            pool = ThreadPool(2) 
            pool.add_task(self.model.Slice())
            pathActor = self.model.getPathActor()
            self.ren.AddActor(self.model._slice_actor)
            self.ren.AddActor(self.model._support_actor)
            self.ren.AddActor(self.model._base_actor)
            logger.log('Added path actor to the scene')
            modelActor = self.model.readActor()
            modelActor.GetProperty().SetOpacity(0)
            self.qvtkWidget.GetRenderWindow().Render()
            self.loadModelTree()
        
    def pathDelete(self):
        self.ren.RemoveActor(self.model.getPathActor())
        self.ren.RemoveActor(self.model.getSupportPathActor())
        self.ren.RemoveActor(self.model.getBasePathActor())
        self.model.deletePath()
        modelActor = self.model.readActor()
        modelActor.GetProperty().SetOpacity(0.5)
        self.loadModelTree()        
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Deleted path of model: ' + self.model.name)
        
    def pathPlanning(self):
        if self.model.readModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        else:
            logger.log('Starting path planning')
            skeinmod.applyConfig(self.model, self.toolDict)
            self.pathDelete()
            pool = ThreadPool(2) 
            pool.add_task(self.model.Slice())
            pathActor = self.model.getPathActor()
            self.ren.AddActor(self.model._slice_actor)
            self.ren.AddActor(self.model._support_actor)
            self.ren.AddActor(self.model._base_actor)
            logger.log('Added path actor to the scene')
            modelActor = self.model.readActor()
            modelActor.GetProperty().SetOpacity(0)
            self.qvtkWidget.GetRenderWindow().Render()
            self.loadModelTree()
        
    def populatePrinterPort(self):
        ports = printerports.scan()
        for port in ports:
            self.portComboBox.addItem(port[1])
            index = self.portComboBox.findText(settings.value("Printer/Port", QVariant('')).toString())
            self.portComboBox.setCurrentIndex(index)
        logger.log('Adding serial ports to port combobox')
                
    def populatePrinterComboBox(self):
        self.printerComboBox.clear()
        for printername in self.printerDict.keys():
            self.printerComboBox.addItem(printername)
            index = self.printerComboBox.findText(settings.value("Printer/Printer", QVariant('## No Printer ##')).toString())
            self.printerComboBox.setCurrentIndex(index)
        logger.log('Adding printers to printer combobox')

    def populateToolComboBox(self):
        self.syringe1ComboBox.clear()
        self.syringe2ComboBox.clear()
        self.syringe1ComboBox.addItem('## No Tool ##')
        self.syringe2ComboBox.addItem('## No Tool ##')
        for toolname in self.toolDict.keys():
            self.syringe1ComboBox.addItem(toolname)
            self.syringe2ComboBox.addItem(toolname)
            index = self.syringe1ComboBox.findText(settings.value("Printer/Tool1", QVariant('## No Tool ##')).toString())
            self.syringe1ComboBox.setCurrentIndex(index)
            index = self.syringe2ComboBox.findText(settings.value("Printer/Tool2", QVariant('## No Tool ##')).toString())
            self.syringe2ComboBox.setCurrentIndex(index)
        logger.log('Adding tools to tool comboboxes')
            
    def resetView(self):
        '''Resets the camera to its initial position'''
        self.camera.SetFocalPoint(0, 0, 0)
        self.camera.SetPosition(300, 0, 100)
        self.camera.SetViewUp(-1, 0, 0)
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Reseted camera position to initial postion')

    def set_ca(self):
        self.updateTranslation('ca')
        logger.log('Changed language to Catalan')

    def set_en(self):
        self.updateTranslation('en')
        logger.log('Changed language to English')

    def set_es_ES(self):
        self.updateTranslation('es_ES')
        logger.log('Changed language to Spanish')

    def set_pt_BR(self):
        self.updateTranslation('pt_BR')
        logger.log('Changed language to Portuguese')

    def showAboutDialog(self):
        Dialog = aboutDialog(self)
        Dialog.exec_()

    def showConfigCustomContextMenu(self, pos):
        ## Save some settings, because of reloading comboboxes
        settings.setValue("Printer/Printer", QVariant(self.printerComboBox.currentText()))
        settings.setValue("Printer/Tool1", QVariant(self.syringe1ComboBox.currentText()))
        settings.setValue("Printer/Tool2", QVariant(self.syringe2ComboBox.currentText()))
        ## Only menu in an item
        index = self.configTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return
        item = self.configTreeWidget.itemAt(pos)
        ## What kind of item --> kind of context menu
        try:
            if item.parent().text(0) == 'Tools': # It's a tool
                self.configToolName = item.text(0)
                logger.log('Clicked on tool: ' + str(self.configToolName))
                self.toolMenu.exec_(QCursor.pos())
            elif item.parent().text(0) == 'Printers': # It's a printer
                self.configPrinterName = item.text(0)
                logger.log('Clicked on printer: ' + str(self.configPrinterName))
                self.printerMenu.exec_(QCursor.pos())
            else:
                return
        except AttributeError: # When clicking on root items, nothing to do
            return
        
    def showImportDialog(self):
        logger.log('Showing import Dialog')
        self.importDialog.exec_()

    def showModelCustomContextMenu(self, pos):
        index = self.modelTreeWidget.indexAt(pos) 
        if not index.isValid(): # if not valid, nothing to edit
            return 
        item = self.modelTreeWidget.itemAt(pos) 
        if item.parent(): # if it has parent, it is a slice, not a model
            return
        modelName = item.text(0)
        logger.log('Clicked on model: ' + modelName)
        self.model = self.modelDict[str(modelName)]
        self.modelMenu.exec_(QCursor.pos())
        
    def showPropertiesDialog(self):
        if self.model.hasModelPath():
            QMessageBox().about(self, self.tr("Error"), self.tr("Model sliced, you cannot change it's properties."))
        else:
            logger.log('Showing model properties Dialog')
            Dialog = propertiesDialog(self, self.model, self.toolDict, self.currentPrinter)
            Dialog.exec_()
        
    def showPrinterDialog(self, new):
        logger.log('Showing printer edit Dialog')
        if new:
            Dialog = printerDialog(self)
        else:
            printer = self.printerDict[str(self.configPrinterName)]
            Dialog = printerDialog(self, printer)
        Dialog.exec_()
        self.printerDict = loadPrinters()
        self.populatePrinterComboBox()
        self.loadConfigTree()

    def showToolDialog(self, new):
        logger.log('Showing tool edit Dialog')
        if new:
            logger.log('New Tool')
            Dialog = toolDialog(self)
        else:
            logger.log('Edit Tool')
            tool = self.toolDict[str(self.configToolName)]
            Dialog = toolDialog(self, tool)
        Dialog.exec_() 
        self.toolDict = loadTools()
        self.populateToolComboBox() # Reload data for comboboxes and tool tree
        self.loadConfigTree()

    def startPrinting(self): # need to be implemented
        logger.log('Starting printing process')
        pass
        pool = ThreadPool(2) 
        pool.add_task('####')
        
    def updateCurrentPrinter(self, printerName):
        self.currentPrinter = self.printerDict[str(printerName)]
        # Change printer base on the renderer also

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

    def updateTranslation(self, lang):
        settings.setValue("Language", QVariant('languages/fabqt_' + lang))
        QMessageBox().about(self, self.tr("Translation Info"), self.tr("You need to restart the application to change the language"))
        logger.log('* Language changed: you need to restart the application to apply changes')

## Execution of main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("FabQt") # Need to save settings
    app.setOrganizationName("FabQt") # Need to save settings
    ## Load settings and update translation
    settings = QSettings()
    translator = QTranslator()
    translator.load(settings.value("Language", QVariant(QString("languages/fabqt_en"))).toString())
    app.installTranslator(translator)
    language = settings.value("Language", QVariant(QString("languages/fabqt_en"))).toString()
    ## Start the GUI
    form = FabQtMain()
    form.show()
    form.updateDialogs()
    if language == "languages/fabqt_en":
        form.actionEnglish.setChecked(True)
    elif language == "languages/fabqt_es_ES":
        form.actionSpanish.setChecked(True)
    elif language == "languages/fabqt_ca":
        form.actionCatalan.setChecked(True)
    elif language == "languages/fabqt_pt_BR":
        form.actionPortuguese_Brazil.setChecked(True)
    ## Start application event loop
    app.exec_()
