#!/usr/bin/env python
from PyQt4.QtCore import QFile, QIODevice, QTextStream
from PyQt4.QtXml import QDomDocument
import os
from core.python.fablog import Fablog

logger = Fablog()
CODEC = "UTF-8"

def loadTools(): # look /tools and call loadTool to parse it, the put all in a list
    logger.log('Loading tools')
    dirList = os.listdir('tools/')
    toolDict = dict()
    for fname in dirList:
        if fname[-5:] == '.tool':
            tool = Tool()
            tool.load(fname)
            toolDict[tool.name] = tool
            logger.log('++ Loading tool: ' + fname.split('.')[0])
    logger.log('Finished loading tools')
    return toolDict

class Tool(object):
    def __init__(self, name = None, tipDiam = None, syrDiam = None, pathWidth = None, pathHeight = None, jogSpeed = None,
                suckback = None, pushout = None, pathSpeed = None, pausePaths = None, clearance = None, depRate = None):
        self.name = name
        self.tipDiam = tipDiam
        self.syrDiam = syrDiam
        self.pathWidth = pathWidth
        self.pathHeight = pathHeight
        self.jogSpeed = jogSpeed
        self.suckback = suckback
        self.pushout = pushout
        self.pathSpeed = pathSpeed
        self.pausePaths = pausePaths
        self.clearance = clearance
        self.depRate = depRate
        
    def __str__(self):
        return self.name
        
    def load(self, fname):
        '''Loads information of a *.tool file to actual Tool object.
        fname is tool name plus the extension (name.tool)'''
        self.name = fname.split('.')[0]
        fh = QFile('tools/' + fname)
        fh.open(QIODevice.ReadOnly)
        dom = QDomDocument()
        dom.setContent(fh)
        fh.close()
        root = dom.documentElement()
        if root.tagName() != "TOOL":
            raise ValueError, "not a Tool XML file"
        self.tipDiam = str(root.attribute("TIPDIAM"))
        self.syrDiam = str(root.attribute("SYRDIAM"))
        self.pathWidth = str(root.attribute("PATHWIDTH"))
        self.pathHeight = str(root.attribute("PATHHEIGHT"))
        self.jogSpeed = str(root.attribute("JOGSPEED"))
        self.suckback = str(root.attribute("SUCKBACK"))
        self.pushout = str(root.attribute("PUSHOUT"))
        self.pathSpeed = str(root.attribute("PATHSPEED"))
        self.pausePaths = str(root.attribute("PAUSEPATHS"))
        self.clearance = str(root.attribute("CLEARANCE"))
        self.depRate = str(root.attribute("DEPOSITIONRATE")) 
    
    def save(self, new):
        fh = QFile('tools/' + self.name + '.tool')
        if new and fh.exists():
            return False
        if fh.open(QIODevice.WriteOnly):
            stream = QTextStream(fh)
            stream.setCodec(CODEC)
            stream << ("<?xml version='1.0' encoding='%s'?>\n<!DOCTYPE TOOL>\n<TOOL\n" % CODEC)
            stream << ("TIPDIAM='%s'\nSYRDIAM='%s'\nPATHWIDTH='%s'\nPATHHEIGHT='%s'\nJOGSPEED='%s'\nSUCKBACK='%s'\nPUSHOUT='%s'\n"
                "PATHSPEED='%s'\nPAUSEPATHS='%s'\nCLEARANCE='%s'\nDEPOSITIONRATE='%s'\n>" % (self.tipDiam, self.syrDiam,
                self.pathWidth, self.pathHeight, self.jogSpeed, self.suckback, self.pushout, self.pathSpeed, self.pausePaths,
                self.clearance, self.depRate))
            stream << ("\n</TOOL>")
            fh.close()
        return True
