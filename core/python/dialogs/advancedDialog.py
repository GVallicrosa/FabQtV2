#!/usr/bin/env python
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QDialogButtonBox, QMessageBox
import ui.ui_advancedDialog as ui_advancedDialog

class advancedDialog(QDialog, ui_advancedDialog.Ui_advancedDialog):
    def __init__(self, parent = None, options = None): # ok
        super(advancedDialog, self).__init__(parent)
        self.setupUi(self)
        self.options = options
        
    def accept(self):
        options = dict()
        options['activateRaft'] = str(self.activateRaft.isChecked())
        if self.activateRaft.isChecked():
            options['addRaft'] = str(self.addRaft.isChecked())
            options['baseDensity'] = str(self.baseDensity.value())
            options['baseOver'] = str(self.baseOver.value())
            options['baseLayers'] = str(self.baseLayers.value())
            options['interfaceDensity'] = str(self.interfaceDensity.value())
            options['interfaceOver'] = str(self.interfaceOver.value())
            options['interfaceLayers'] = str(self.interfaceLayers.value())
            options['raftMargin'] = str(self.raftMargin.value())
        self.options.save(options)
        self.close()
