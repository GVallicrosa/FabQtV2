import ui.ui_propertiesDialog as ui_propertiesDialog
from PyQt4.QtGui import QDialog, QMessageBox
from core.python.render import validateMove

class propertiesDialog(QDialog, ui_propertiesDialog.Ui_propertiesDialog):
    def __init__(self, parent, model, actorDict, toolList):
        super(propertiesDialog, self).__init__(parent)
        self.setupUi(self)
        self.model = model
        self.actorDict = actorDict
        pos = actorDict[str(model)].GetPosition()
        self.x_translate.setValue(pos[0])
        self.y_translate.setValue(pos[1])
        self.z_translate.setValue(pos[2])
        scale = actorDict[str(model)].GetScale()
        self.x_scale.setValue(scale[0])
        self.y_scale.setValue(scale[1])
        self.z_scale.setValue(scale[2])
        for tool in toolList:
            self.modelMaterialComboBox.addItem(tool.name)
            self.modelMaterialComboBox.setCurrentIndex(-1) # No tool

    def accept(self):
        actor = self.actorDict[str(self.model)]
        actor.SetPosition(self.x_translate.value(), self.y_translate.value(), self.z_translate.value())
        actor.RotateX(self.x_rotate.value())
        actor.RotateY(self.y_rotate.value())
        actor.RotateZ(self.z_rotate.value())
        actor.SetScale(self.x_scale.value(), self.y_scale.value(), self.z_scale.value())
        if not validateMove(actor):
            QMessageBox().about(self, self.tr("Error"), self.tr("Model exceeds limits. Need to be scaled."))
        self.close()
