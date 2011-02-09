#!/usr/bin/env python

import os

command = "pyuic4 -o ui/ui_fabqtDialog.py ui/fabqtDialog.ui"
print 'Generating....'
os.system(command)

# Need to do some substitution in generated file to make the UI work  
# when the QVTKWidget was created to be used in C++

f = open('ui/ui_fabqtDialog.py', 'r')
s = f.read()
f.close()

s = s.replace('QVTKWidget','QVTKRenderWindowInteractor')
s = s.replace('from QVTK', 'from vtk.qt4.QVTK')
s = s.replace('from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor', 'from ui.vtkCustom import QVTKRenderWindowInteractorCustom')
s = s.replace('self.qvtkWidget = QVTKRenderWindowInteractor(self.centralwidget)', 'self.qvtkWidget = QVTKRenderWindowInteractorCustom(self.centralwidget)')

w = open('ui/ui_fabqtDialog.py', 'w')
w.write(s)
w.close()
