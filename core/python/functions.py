#include <QFile>
import codecs
from PyQt4.QtXml import *
from PyQt4.QtCore import *

CODEC = "UTF-8"
NEWPARA = unichr(0x2029)
NEWLINE = unichr(0x2028)

def saveTool(tool, newTool):
    fh = QFile('tools/' + tool.name + '.tool')
#    fh = QFile('tools/prova.txt')
#    if newTool and fh.exists():
#        raise FileExistsError
    if fh.open(QIODevice.WriteOnly):
        stream = QTextStream(fh)
        stream.setCodec(CODEC)
        stream << ("<?xml version='1.0' encoding='%s'?>\n"
                       "<!DOCTYPE TOOL>\n<TOOL\n" % CODEC)
        stream << ("TIPDIAM='%s'\nSYRDIAM='%s'\nPATHWIDTH='%s'\nPATHHEIGHT='%s'\nJOGSPEED='%s'\nSUCKBACK='%s'\nPUSHOUT='%s'\nPATHSPEED='%s'\nPAUSEPATHS='%s'\nCLEARANCE='%s'\nDEPOSITIONRATE='%s'\n>" % (tool.tipDiam, tool.syrDiam, tool.pathWidth, tool.pathHeight, tool.jogSpeed, tool.suckback, tool.pushout, tool.pathSpeed, tool.pausePaths, tool.clearance, tool.depRate))
        stream << ("\n</TOOL>")
        fh.close()

def loadTool(name):
    pass
