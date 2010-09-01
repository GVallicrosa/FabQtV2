import ui.ui_aboutDialog as ui_aboutDialog
from PyQt4.QtGui import QDialog

class aboutDialog(QDialog, ui_aboutDialog.Ui_AboutDlg):
    def __init__(self, parent = None):
        super(aboutDialog, self).__init__(parent)
        self.setupUi(self)
