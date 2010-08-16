#include <QFile>
import codecs
import os
import vtk
from PyQt4.QtXml import *
from PyQt4.QtCore import *
from core.python.classes import *

CODEC = "UTF-8"
NEWPARA = unichr(0x2029)
NEWLINE = unichr(0x2028)

def saveTool(tool, newTool):
    fh = QFile('tools/' + tool.name + '.tool')
    if newTool and fh.exists():
        return False
    if fh.open(QIODevice.WriteOnly):
        stream = QTextStream(fh)
        stream.setCodec(CODEC)
        stream << ("<?xml version='1.0' encoding='%s'?>\n<!DOCTYPE TOOL>\n<TOOL\n" % CODEC)
        stream << ("TIPDIAM='%s'\nSYRDIAM='%s'\nPATHWIDTH='%s'\nPATHHEIGHT='%s'\nJOGSPEED='%s'\nSUCKBACK='%s'\nPUSHOUT='%s'\nPATHSPEED='%s'\nPAUSEPATHS='%s'\nCLEARANCE='%s'\nDEPOSITIONRATE='%s'\n>" % (tool.tipDiam, tool.syrDiam, tool.pathWidth, tool.pathHeight, tool.jogSpeed, tool.suckback, tool.pushout, tool.pathSpeed, tool.pausePaths, tool.clearance, tool.depRate))
        stream << ("\n</TOOL>")
        fh.close()
    return True

def loadTool(fname):
    tool = Tool()
    tool.name = fname.split('.')[0]
    fh = QFile('tools/' + fname)
    fh.open(QIODevice.ReadOnly)
    dom = QDomDocument()
    dom.setContent(fh)
    fh.close()
    root = dom.documentElement()
    if root.tagName() != "TOOL":
        raise ValueError, "not a Tool XML file"
    tool.tipDiam = str(root.attribute("TIPDIAM"))
    tool.syrDiam = str(root.attribute("SYRDIAM"))
    tool.pathWidth = str(root.attribute("PATHWIDTH"))
    tool.pathHeight = str(root.attribute("PATHHEIGHT"))
    tool.jogSpeed = str(root.attribute("JOGSPEED"))
    tool.suckback = str(root.attribute("SUCKBACK"))
    tool.pushout = str(root.attribute("PUSHOUT"))
    tool.pathSpeed = str(root.attribute("PATHSPEED"))
    tool.pausePaths = str(root.attribute("PAUSEPATHS"))
    tool.clearance = str(root.attribute("CLEARANCE"))
    tool.depRate = str(root.attribute("DEPOSITIONRATE")) 
    return tool

def loadTools(): # look /tools and call loadTool to parse it, the put all in a list
    print '** Loading tools'
    dirList=os.listdir('tools/')
    toolList =list()
    toolList.insert(-1, Tool('## No Tool ##'))
    for fname in dirList:
        if fname[-5:] == '.tool':
            toolList.insert(-1, loadTool(fname))
            print '*** Loading tool: ' + fname.split('.')[0]
    print '** Finished loading tools\n'
    return toolList
