#!/usr/bin/env python
from __future__ import division
import sys
import os
import vtk
from time import localtime, asctime
# Import Qt
from PyQt4.QtCore import QString, QUrl, QVariant, QSettings, QTranslator, QStringList, QSize, QPoint, SIGNAL, QStringList
from PyQt4.QtGui import QTreeWidgetItem, QApplication, QMenu, QMainWindow, QFileDialog, QCursor, QMessageBox

if os.path.exists('log.txt'):
    if os.path.getsize('log.txt') >= 1024*1024: # 1MB
        os.remove('log.txt')
        import checkSkeinforgeVersion
        checkSkeinforgeVersion.main()
else:
    import checkSkeinforgeVersion
    checkSkeinforgeVersion.main()
    
if not os.path.exists('profiles/'):
    import zipfile
    fh = zipfile.ZipFile('profiles.zip', 'r')
    fh.extractall('./')

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
        
logger = Fablog()
logger.log('\n\n' + str(asctime(localtime())) + '\n')

class FabQtMain(QMainWindow, ui_fabqtDialog.Ui_MainWindow):
    def __init__(self, parent = None):
        ## Init parent
        super(FabQtMain, self).__init__(parent)
        self.setupUi(self)
        ## Start log
        self.connect(logger, SIGNAL('Fablogging'), self.logText)
        logger.log('--> Initialising application')
        ## Variables
        self.configToolName = None # handles the current clicked tool
        self.configPrinterName = None # handles the current clicked printer
        self.model = None # handles the current clicked model
        self.toolDict = loadTools() # toolname: Tool()
        self.qvtkWidget.toolDict = self.toolDict # copy to vtk for layer by layer view
        self.printerDict = loadPrinters() # printername: Printer()
        self.modelDict = dict() # modelname: Model(), nothing at the start
        self.options = Options() # advanced path options
        ## Config tree and comboboxes, load initial values
        self.populateConfigTree()
        self.populateMaterialListWidget()
        self.populateToolComboBox()
        self.populatePrinterComboBox()
        self.populatePrinterPort()
        self.currentPrinter = self.printerDict[str(self.printerComboBox.currentText())]
        ## Render window using VTK lib
        self.qvtkWidget.customStart(self.currentPrinter)
        self.camera = self.qvtkWidget.camera
        ## Thread pool
        #self.pathPool = ThreadPool(2)
        #self.importPool = ThreadPool(2)
        self.importing = False
        self.planning = False
        
## CONNECTIONS AND MENUS
        ## Import model file dialog
        filters = QStringList()
        filters.append("STL Models (*.stl)")
        filters.append("GCode file (*.gcode)")
        #filters.append("GCode file (*.txt)")
        filters.append("All files (*)")
        self.importDialog = QFileDialog(self, 'Import model', settings.value("Path/ModelDir", QVariant(QString('./'))).toString())
        self.importDialog.setNameFilters(filters)
        self.connect(self.importDialog, SIGNAL('fileSelected(QString)'), self.importModel)
        ## Load preferences (called at the main loop)
        self.resize(settings.value("MainWindow/Size", QVariant(QSize(600, 500))).toSize())
        self.move(settings.value("MainWindow/Position", QVariant(QPoint(0, 0))).toPoint())
        self.restoreState(settings.value("MainWindow/State").toByteArray())
        ## Show/hide dialogs from the menu
        self.connect(self.actionMain_tools, SIGNAL("triggered()"), self.mainDock_setVisible)
        self.connect(self.actionStatus_Info, SIGNAL("triggered()"), self.infoDock_setVisible)
        self.connect(self.actionToolbar, SIGNAL("toggled(bool)"), self.toolBar.setVisible)
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
        self.connect(self.resetViewButton, SIGNAL("clicked()"), self.qvtkWidget.resetView)
        ## Ortographic view
        self.connect(self.actionBehind_view, SIGNAL("triggered()"), self.qvtkWidget.behindView)
        self.connect(self.actionDefault_view, SIGNAL("triggered()"), self.qvtkWidget.defaultView)
        self.connect(self.actionFront_view, SIGNAL("triggered()"), self.qvtkWidget.frontView)
        self.connect(self.actionLeft_view, SIGNAL("triggered()"), self.qvtkWidget.leftView)
        self.connect(self.actionRight_view, SIGNAL("triggered()"), self.qvtkWidget.rightView)
        self.connect(self.actionTop_view, SIGNAL("triggered()"), self.qvtkWidget.topView)
        ## Context menus (right click)
        self.connect(self.modelTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showModelCustomContextMenu)
        self.connect(self.configTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.showConfigCustomContextMenu)
        ## Model context menu
        self.modelMenu = QMenu()
        actionProperties = self.modelMenu.addAction("Properties/Transform")
        actionStandard = self.modelMenu.addAction("Standard Path Planning")
        actionAdvanced = self.modelMenu.addAction("Advanced Path Planning")
        actionCustom = self.modelMenu.addAction("Custom Path Planning")
        actionCustom2 = self.modelMenu.addAction("Custom Path Planning (new)")
        actionExport = self.modelMenu.addAction("Export to vector file")
        actionDeletePath = self.modelMenu.addAction("Erase Path")
        actionOrigin = self.modelMenu.addAction("Move to Origin")
        actionDelete = self.modelMenu.addAction("Delete")
        self.connect(actionProperties, SIGNAL('triggered()'), self.showPropertiesDialog)
        self.connect(actionStandard, SIGNAL('triggered()'), self.pathPlanning)
        self.connect(actionAdvanced, SIGNAL('triggered()'), self.pathAdvanced)
        self.connect(actionCustom, SIGNAL('triggered()'), self.pathCustom)
        self.connect(actionCustom2, SIGNAL('triggered()'), self.pathCustom2)
        self.connect(actionExport, SIGNAL('triggered()'), self.pathExport)
        self.connect(actionDeletePath, SIGNAL('triggered()'), self.pathDelete)
        self.connect(actionOrigin, SIGNAL('triggered()'), self.moveToOrigin)
        self.connect(actionDelete, SIGNAL('triggered()'), self.deleteModel)
        self.modelMenu.addAction(actionProperties)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionStandard)
        self.modelMenu.addAction(actionAdvanced)
        self.modelMenu.addAction(actionCustom)
        self.modelMenu.addAction(actionCustom2)
        self.modelMenu.addAction(actionExport)
        self.modelMenu.addAction(actionDeletePath)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionOrigin)
        self.modelMenu.addSeparator()
        self.modelMenu.addAction(actionDelete)
        ## Model materials
        self.connect(self.materialListWidget, SIGNAL('itemSelectionChanged()'), self.materialClicked)
        ## Printer context menu
        self.printerMenu = QMenu()
        actionEditPrinter = self.printerMenu.addAction("Edit Printer")
        actionNewPrinter = self.printerMenu.addAction("New Printer")
        self.connect(actionEditPrinter, SIGNAL('triggered()'), self.printerDialogEdit)
        self.connect(actionNewPrinter, SIGNAL('triggered()'), self.printerDialogNew)
        self.printerMenu.addAction(actionEditPrinter)
        self.printerMenu.addSeparator()
        self.printerMenu.addAction(actionNewPrinter)
        ## Tool context menu
        self.toolMenu = QMenu()
        actionEditTool = self.toolMenu.addAction("Edit Tool")
        actionNewTool = self.toolMenu.addAction("New Tool")
        self.connect(actionEditTool, SIGNAL('triggered()'), self.toolDialogEdit)
        self.connect(actionNewTool, SIGNAL('triggered()'), self.toolDialogNew)
        self.toolMenu.addAction(actionEditTool)
        self.toolMenu.addSeparator()
        self.toolMenu.addAction(actionNewTool)
        ## Translations (en, ca, es_ES, pt_BR)
        self.connect(self.actionEnglish, SIGNAL("triggered()"), self.set_en)
        self.connect(self.actionSpanish_Spain, SIGNAL("triggered()"), self.set_es_ES)
        self.connect(self.actionCatalan, SIGNAL("triggered()"), self.set_ca)
        self.connect(self.actionPortuguese_Brazil, SIGNAL("triggered()"), self.set_pt_BR)
        logger.log('--> End Initialisation')
        
    def infoDock_setVisible(self):
        self.infoDock.setVisible(True)
        
    def mainDock_setVisible(self):
        self.mainDock.setVisible(True)
        
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
        self.qvtkWidget.RemoveActorCustom(self.model)
        self.modelDict.pop(str(self.model.name))
        self.qvtkWidget.modelDict = self.modelDict
        self.populateModelTree()        
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Deleted model: ' + self.model.name)
    
    def printerDialogEdit(self):
        '''Edits printer configuration, general options and axes options.'''
        logger.log('Edit printer Dialog')
        self.showPrinterDialog(False)
        
    def toolDialogEdit(self):
        logger.log('Edit tool Dialog')
        self.showToolDialog(False)
             
    def importModel(self, fname):
        self.importing = True
        fname = str(fname)
        settings.setValue("Path/ModelDir", QVariant(fname[0:fname.find(fname.split('/')[-1])]))
        #def importer():
        model = Model()
        model.load(fname)
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
        self.qvtkWidget.modelDict = self.modelDict #for view slices
        printer = str(self.printerComboBox.currentText())
        printer = self.printerDict[printer]
        self.qvtkWidget.AddActorCustom(model)
        if self.modelDict[str(model.name)].hasModel():
            validateMove(model.getActor(), printer)
        else:
            validateMove(model.getPathActor(), printer)
        self.qvtkWidget.GetRenderWindow().Render()
        self.populateModelTree()
        self.importing = False
        #self.importPool.add_task(importer)
        
    def materialClicked(self):
        toolname = str(self.materialListWidget.currentItem().text())
        try:
            item = self.modelTreeWidget.currentItem()
            if item.text(0).contains('Model') or item.text(0).contains('Mat:'):
                item = item.parent()
            elif item.text(0).contains('path'):
                return
            modelname = str(item.text(0))
            pathdone = False
            for i in range(item.childCount()): # Check path calculated
                if item.child(i).text(0).contains('path'):
                    pathdone = True
            if not pathdone:
                self.modelDict[modelname].setModelMaterial(toolname)
                logger.log('Model: ' + modelname + ' Material: ' + toolname)
            self.populateModelTree()
        except: # No models in modelTreeWidget
            pass

    def populateConfigTree(self):
        logger.log('Delete config tree')
        self.configTreeWidget.clear()
        logger.log('Loading tools in config tree')
        self.populateToolTree()
        logger.log('Loading printers in config tree')
        self.populatePrinterTree()
        
    def populateMaterialListWidget(self):
        self.materialListWidget.clear()
        for toolname in self.toolDict.keys():
            self.materialListWidget.addItem(toolname)

    def populateModelTree(self):
        logger.log('Loading model tree')
        self.modelTreeWidget.clear()
        for model in self.modelDict.keys():
            logger.log('Adding model: ' + model)
            modelItem = QTreeWidgetItem(self.modelTreeWidget)
            modelItem.setText(0, model)
            if self.modelDict[model].hasModel():
                modelItem.addChild(QTreeWidgetItem(QStringList('Model')))
            if self.modelDict[model].hasModelMaterial():
                modelItem.addChild(QTreeWidgetItem(QStringList('Mat: ' + self.modelDict[model]._modelMaterial)))
            if self.modelDict[model].hasModelPath():
                modelItem.addChild(QTreeWidgetItem(QStringList('model_path')))
            if self.modelDict[model].hasSupportPath():
                modelItem.addChild(QTreeWidgetItem(QStringList('support_path')))
            if self.modelDict[model].hasBasePath():
                modelItem.addChild(QTreeWidgetItem(QStringList('base_path')))
        self.modelTreeWidget.expandAll()
            
    def populatePrinterTree(self):
        printerTree = QTreeWidgetItem(self.configTreeWidget)
        printerTree.setText(0, "Printers")
        for printer in self.printerDict.values():
            if not printer.name == '## No Printer ##':
                logger.log('Adding printer: ' + printer.name)
                actualPrinter = QTreeWidgetItem(printerTree)
                actualPrinter.setText(0, printer.name)
    
    def populateToolTree(self):
        toolTree = QTreeWidgetItem(self.configTreeWidget)
        toolTree.setText(0, "Tools")
        for tool in self.toolDict.values():
            if not tool.name == '## No Tool ##':
                logger.log('Adding tool: ' + tool.name)
                actualTool = QTreeWidgetItem(toolTree)
                actualTool.setText(0, tool.name)
                
    def logText(self, text):
        self.logTextBrowser.append(QString(text))

    def modelDoubleClicked(self, index):
        item = self.modelTreeWidget.itemFromIndex(index)
        if not item.parent(): # its a model
            modelName = item.text(0)
            logger.log('Double clicked on model: ' + modelName)
            model = self.modelDict[str(modelName)]
            if model.hasModel():
                actor = model.getActor()
            else:
                actor = model.getPathActor()
            center = actor.GetCenter()
            self.camera.SetFocalPoint(center)
        else: # is 'Model' or 'Toolpath'
            parent = item.parent()
            modelName = parent.text(0)
            model = self.modelDict[str(modelName)]
            text = str(item.text(0))
            if text == 'Model':
                actor = model.getActor()
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
        moveToOrigin(self.model.getActor())
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Moved to Origin, model: ' + self.model.name)

    def printerDialogNew(self):
        logger.log('New printer Dialog')
        self.showPrinterDialog(True)
        
    def toolDialogNew(self):
        logger.log('New tool Dialog')
        self.showToolDialog(True)

    def okToContinue(self): # To implement not saved changes closing
        logger.log("It's ok to close")
        #if not self.importing and not self.planning:
        return True
        #else:
        #    return False
        
    def on_mainDock_closeEvent(self, event): # It never enters here, I don't know why (it could be a solution to the dock problem)
        print 'Entered mainDock close event' # For testing
        self.actionMain_tools.setChecked(False)
        event.accept()
        
    def pathExport(self):
        if not self.model.hasModelPath():
            QMessageBox().about(self, self.tr("Error"), self.tr("No path to export, please calculate it before exporting."))
        else:
            logger.log('+ Start vector file export')
            fname = settings.value("Path/ModelDir", QVariant(QString('./'))).toString() + str(self.model.name) + '.txt'
            fh = file(fname, 'w')
            layers = self.model._layer
            for layer in layers:
                paths = layer.getModelPaths()
                for path in paths:
                    vectors = path.getVector()
                    for vec in vectors:
                        print >> fh, '%s %s %s' % (vec.x, vec.y, vec.z)
                    print >> fh, ''
            logger.log('- Finished vector file export')
        
    def pathCustom(self):
        if self.model.getModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        elif self.planning:
            QMessageBox().about(self, self.tr("Error"), self.tr("You already doing a path planning, wait for completition."))
        else:
            try:
                logger.log('Starting custom path planning')
                self.planning = True
                self.pathDelete()
                self.model.SliceCustom(self.toolDict)
                self.qvtkWidget.AddActorCustom(self.model)
                logger.log('Added path actor/s to the scene')
                modelActor = self.model.getActor()
                modelActor.GetProperty().SetOpacity(0)
                self.qvtkWidget.GetRenderWindow().Render()
                self.populateModelTree()
                self.planning = False
            except:
                self.planning = False
                QMessageBox().about(self, self.tr("Error"), self.tr("Problem encountered during path planning, try another one."))
                
    def pathCustom2(self):
        if self.model.getModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        elif self.planning:
            QMessageBox().about(self, self.tr("Error"), self.tr("You already doing a path planning, wait for completition."))
        else:
            try:
                logger.log('Starting custom path planning (new)')
                self.planning = True
                self.pathDelete()
                self.model.SliceCustom2(self.toolDict)
                self.qvtkWidget.AddActorCustom(self.model)
                logger.log('Added path actor/s to the scene')
                modelActor = self.model.getActor()
                modelActor.GetProperty().SetOpacity(0)
                self.qvtkWidget.GetRenderWindow().Render()
                self.populateModelTree()
                self.planning = False
            except StandardError, e:
                print e
                self.planning = False
                QMessageBox().about(self, self.tr("Error"), self.tr("Problem encountered during path planning, try another one."))
    
    def pathAdvanced(self):
        if self.model.getModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        elif self.planning:
            QMessageBox().about(self, self.tr("Error"), self.tr("You already doing a path planning, wait for completition."))
        else:
            try:
                logger.log('Starting advanced path planning')
                self.planning = True
                Dialog = advancedDialog(self, self.options)
                Dialog.exec_()
                skeinmod.applyConfig(self.model, self.toolDict, True, self.options)
                self.pathDelete()
                printer = str(self.printerComboBox.currentText())
                printer = self.printerDict[printer]
                if self.model.hasModel():
                    validateMove(self.model.getActor(), printer, float(self.options.dict['raftMargin']))
                self.model.Slice()
                pathActor = self.model.getPathActor()
                self.qvtkWidget.AddActorCustom(self.model)
                logger.log('Added path actor/s to the scene')
                modelActor = self.model.getActor()
                modelActor.GetProperty().SetOpacity(0)
                self.qvtkWidget.GetRenderWindow().Render()
                self.populateModelTree()
                self.planning = False
            except StandardError, e:
                print e
                self.planning = False
                QMessageBox().about(self, self.tr("Error"), self.tr("Problem encountered during path planning, try another one."))
        
    def pathDelete(self):
        self.qvtkWidget.RemoveActorCustom(self.model, False)
        self.model.deletePath()
        modelActor = self.model.getActor()
        modelActor.GetProperty().SetOpacity(0.5)
        self.populateModelTree()        
        self.qvtkWidget.GetRenderWindow().Render()
        logger.log('Deleted path of model: ' + self.model.name)
        
    def pathPlanning(self):
        if self.model.getModelMaterial() is None:
            QMessageBox().about(self, self.tr("Error"), self.tr("You need to define model material to slice it."))
        elif self.planning:
            QMessageBox().about(self, self.tr("Error"), self.tr("You already doing a path planning, wait for completition."))
        else:
            try:
                logger.log('Starting path planning')
                self.planning = True
                skeinmod.applyConfig(self.model, self.toolDict)
                self.pathDelete()
                self.model.Slice()
                pathActor = self.model.getPathActor()
                self.qvtkWidget.AddActorCustom(self.model)
                logger.log('Added path actor to the scene')
                modelActor = self.model.getActor()
                modelActor.GetProperty().SetOpacity(0)
                self.qvtkWidget.GetRenderWindow().Render()
                self.populateModelTree()
                self.planning = False
            except StandardError, e:
                print e
                self.planning = False
                QMessageBox().about(self, self.tr("Error"), self.tr("Problem encountered during path planning, try another one."))
        
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
        if self.importing:
            QMessageBox().about(self, self.tr("Error"), self.tr("Model already importing, wait for completition."))
        else:
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
        self.populateConfigTree()

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
        self.qvtkWidget.toolDict = self.toolDict
        self.populateToolComboBox() # Reload data for comboboxes and tool tree
        self.populateConfigTree()

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
    global bar
    bar = form.progressBar
    app.exec_()
