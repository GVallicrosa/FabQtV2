#!/bin/bash
cd ui
pyrcc4 -o resources_rc.py resources.qrc
cd ../ui
#pyuic4 -o ui_fabqtDialog.py fabqtDialog.ui # it's done in the fixUI
pyuic4 -o ui_aboutDialog.py aboutDialog.ui
pyuic4 -o ui_toolDialog.py toolDialog.ui
pyuic4 -o ui_propertiesDialog.py propertiesDialog.ui
cd ..
pylupdate4 fabqt.pro
python fixUI.py
cd languages
lrelease *.ts
sleep 3
