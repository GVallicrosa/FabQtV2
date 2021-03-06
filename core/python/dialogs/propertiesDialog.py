import ui.ui_propertiesDialog as ui_propertiesDialog
from PyQt4.QtGui import QDialog, QMessageBox
from core.python.render import validateMove

class propertiesDialog(QDialog, ui_propertiesDialog.Ui_propertiesDialog):
    def __init__(self, parent, model, toolDict, printer):
        super(propertiesDialog, self).__init__(parent)
        self.setupUi(self)
        self.model = model
        self.printer = printer
        pos = self.model.getActor().GetPosition()
        self.x_translate.setValue(pos[0])
        self.y_translate.setValue(pos[1])
        self.z_translate.setValue(pos[2])
        scale = self.model.getActor().GetScale()
        self.x_scale.setValue(scale[0])
        self.y_scale.setValue(scale[1])
        self.z_scale.setValue(scale[2])
        for toolname in toolDict.keys():
            self.modelMaterialComboBox.addItem(toolname)
        if self.model.getModelMaterial() is None:
            self.modelMaterialComboBox.setCurrentIndex(-1) # No tool
        else:
            index = self.modelMaterialComboBox.findText(toolDict[str(self.model.getModelMaterial())].name)
            self.modelMaterialComboBox.setCurrentIndex(index)

    def accept(self):
        if self.modelMaterialComboBox.currentText() != '':
            self.model.setModelMaterial(self.modelMaterialComboBox.currentText())
        actor = self.model.getActor()
        actor.SetPosition(self.x_translate.value(), self.y_translate.value(), self.z_translate.value())
        actor.RotateWXYZ(self.x_rotate.value(), 1, 0, 0)
        actor.RotateWXYZ(self.y_rotate.value(), 0, 1, 0)
        actor.RotateWXYZ(self.z_rotate.value(), 0, 0, 1)
        actor.SetScale(self.x_scale.value(), self.y_scale.value(), self.z_scale.value())
        if not validateMove(actor, self.printer):
            QMessageBox().about(self, self.tr("Error"), self.tr("Model exceeds limits. Need to be scaled."))
        self.close()
