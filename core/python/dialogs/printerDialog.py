#!/usr/bin/env python
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QDialogButtonBox, QMessageBox
import ui.ui_printerDialog as ui_printerDialog

class printerDialog(QDialog, ui_printerDialog.Ui_printerDlg):
    def __init__(self, parent = None, printer = None): # ok
        super(printerDialog, self).__init__(parent)
        self.setupUi(self)
        saveAs = self.printerButtonBox.addButton('Save As', QDialogButtonBox.ActionRole)
        self.connect(saveAs, SIGNAL('clicked(bool)'), self.nameChangeable)
        if printer is not None: # if you edit you cannot change the printer name, and load the parameters
            self.printerNameLineEdit.setEnabled(False)
            self.printerNameLineEdit.setText(printer.name)
            self.updatePeriodLineEdit.setText(printer.updatePeriod)
            self.jogSpeedLineEdit.setText(printer.jogSpeed)
            self.maxToolsLineEdit.setText(printer.maxTools)
            self.toolLimitLineEdit.setText(printer.toolLimit)
            self.maxAccelLineEdit.setText(printer.maxAccel)
            self.xMaxLineEdit.setText(printer.xMax)
            self.yMaxLineEdit.setText(printer.yMax)
            self.zMaxLineEdit.setText(printer.zMax)
            ## Base
            self.baseDirection.setText(printer.base.direction)
            self.baseMotor.setText(printer.base.motor)
            self.baseRange.setText(printer.base.arange)
            self.baseLimit.setText(printer.base.limits)
            self.baseIncrement.setText(printer.base.increment)
            ## X
            self.xDirection.setText(printer.x.direction)
            self.xMotor.setText(printer.x.motor)
            self.xRange.setText(printer.x.arange)
            self.xLimit.setText(printer.x.limits)
            self.xIncrement.setText(printer.x.increment)
            ## Y
            self.yDirection.setText(printer.y.direction)
            self.yMotor.setText(printer.y.motor)
            self.yRange.setText(printer.y.arange)
            self.yLimit.setText(printer.y.limits)
            self.yIncrement.setText(printer.y.increment)
            ## Z
            self.zDirection.setText(printer.z.direction)
            self.zMotor.setText(printer.z.motor)
            self.zRange.setText(printer.z.arange)
            self.zLimit.setText(printer.z.limits)
            self.zIncrement.setText(printer.z.increment)
            ## U
            self.uDirection.setText(printer.u.direction)
            self.uMotor.setText(printer.u.motor)
            self.uRange.setText(printer.u.arange)
            self.uLimit.setText(printer.u.limits)
            self.uIncrement.setText(printer.u.increment)
            ## V
            if int(printer.maxTools) > 1:
                self.vDirection.setText(printer.v.direction)
                self.vMotor.setText(printer.v.motor)
                self.vRange.setText(printer.v.arange)
                self.vLimit.setText(printer.v.limits)
                self.vIncrement.setText(printer.v.increment)
            self.new = False
            saveAs.setEnabled(True)
        else:
            printer = Printer()
            self.new = True
            saveAs.setEnabled(False)
        self.printer = printer

    def accept(self): # ok
        if self.verify():
            self.printer = self.updatePrinter(self.printer)
            if self.printer.save(self.new):
                self.printer = None
                self.close()
            else:
                QMessageBox().about(self, self.tr("Error"), self.tr("Printer with same name already exists.\nChange the printer name."))
        else:
            QMessageBox().about(self, self.tr("Error"), self.tr("Not all paramaters are filled"))

    def nameChangeable(self): # ok
        self.printerNameLineEdit.setEnabled(True)
        self.new = True

    def updatePrinter(self, printer): # ok
        printer.name = self.printerNameLineEdit.text()
        printer.updatePeriod = self.updatePeriodLineEdit.text()
        printer.jogSpeed = self.jogSpeedLineEdit.text()
        printer.maxTools = self.maxToolsLineEdit.text()
        printer.toolLimit = self.toolLimitLineEdit.text()
        printer.maxAccel = self.maxAccelLineEdit.text()
        printer.xMax = self.xMaxLineEdit.text()
        printer.yMax = self.yMaxLineEdit.text()
        printer.zMax = self.zMaxLineEdit.text()
        ## Base
        printer.base.direction = self.baseDirection.text()
        printer.base.motor = self.baseMotor.text()
        printer.base.arange = self.baseRange.text()
        printer.base.limits = self.baseLimit.text()
        printer.base.increment = self.baseIncrement.text()
        ## X
        printer.x.direction = self.xDirection.text()
        printer.x.motor = self.xMotor.text()
        printer.x.arange = self.xRange.text()
        printer.x.limits = self.xLimit.text()
        printer.x.increment = self.xIncrement.text()
        ## Y
        printer.y.direction = self.yDirection.text()
        printer.y.motor = self.yMotor.text()
        printer.y.arange = self.yRange.text()
        printer.y.limits = self.yLimit.text()
        printer.y.increment = self.yIncrement.text()
        ## Z
        printer.z.direction = self.zDirection.text()
        printer.z.motor = self.zMotor.text()
        printer.z.arange = self.zRange.text()
        printer.z.limits = self.zLimit.text()
        printer.z.increment = self.zIncrement.text()
        ## U
        printer.u.direction = self.uDirection.text()
        printer.u.motor = self.uMotor.text()
        printer.u.arange = self.uRange.text()
        printer.u.limits = self.uLimit.text()
        printer.u.increment = self.uIncrement.text()
        ## V
        if int(printer.maxTools) > 1:
            printer.v.direction = self.vDirection.text()
            printer.v.motor = self.vMotor.text()
            printer.v.arange = self.vRange.text()
            printer.v.limits = self.vLimit.text()
            printer.v.increment = self.vIncrement.text()
        return printer
        

    def verify(self): # ok
        if self.printerNameLineEdit.text().isEmpty() or self.updatePeriodLineEdit.text().isEmpty() or self.jogSpeedLineEdit.text().isEmpty() or self.maxToolsLineEdit.text().isEmpty() or self.toolLimitLineEdit.text().isEmpty() or self.maxAccelLineEdit.text().isEmpty() or self.xMaxLineEdit.text().isEmpty() or self.yMaxLineEdit.text().isEmpty() or self.zMaxLineEdit.text().isEmpty() or self.baseDirection.text().isEmpty() or self.baseMotor.text().isEmpty() or self.baseRange.text().isEmpty() or self.baseLimit.text().isEmpty() or self.baseIncrement.text().isEmpty() or self.xDirection.text().isEmpty() or self.xMotor.text().isEmpty() or self.xRange.text().isEmpty() or self.xLimit.text().isEmpty() or self.xIncrement.text().isEmpty() or self.yDirection.text().isEmpty() or self.yMotor.text().isEmpty() or self.yRange.text().isEmpty() or self.yLimit.text().isEmpty() or self.yIncrement.text().isEmpty() or self.zDirection.text().isEmpty() or self.zMotor.text().isEmpty() or self.zRange.text().isEmpty() or self.zLimit.text().isEmpty() or self.zIncrement.text().isEmpty() or self.uDirection.text().isEmpty() or self.uMotor.text().isEmpty() or self.uRange.text().isEmpty() or self.uLimit.text().isEmpty() or self.uIncrement.text().isEmpty():
            return False
        else:
            if int(self.maxToolsLineEdit.text()) > 1:
                if self.vDirection.text().isEmpty() or self.vMotor.text().isEmpty() or self.vRange.text().isEmpty() or self.vLimit.text().isEmpty() or self.vIncrement.text().isEmpty():
                    return False
                else:
                    return True
            else:
                return True
