#!/usr/bin/env python
from PyQt4.QtCore import QFile, QIODevice, SIGNAL, QTextStream
from PyQt4.QtGui import QDialog, QDialogButtonBox, QMessageBox
from PyQt4.QtXml import QDomDocument
import os
import logging

CODEC = "UTF-8"
logger = logging.getLogger('core.python.printer')

def loadPrinters(): # ok
    logger.debug('** Loading printers')
    dirList = os.listdir('config/')
    printerDict = dict()
    printer = Printer()
    printer.name = '## No Printer ##'
    printer.xMax = 200
    printer.yMax = 200
    printer.zMax = 200
    printerDict[printer.name] = printer
    for fname in dirList:
        if fname[-8:] == '.printer':
            printer = Printer()
            printer.load(fname)
            printerDict[printer.name] = printer
            logger.debug('*** Loading printer: ' + fname.split('.')[0])
    logger.debug('Finished loading printers')
    return printerDict

class Axis(object): # ok
    def __init__(self, direction = None, motor = None, arange = None, limits = None, increment = None):
        self.direction = direction # 4 values
        self.motor = motor # number
        self.arange = arange # 3 values
        self.limits = limits # 2 values binary
        self.increment = increment # number

class Printer(object): # ok
    def __init__(self, name = None, updatePeriod = None, jogSpeed = None, maxTools = None, toolLimit = None, maxAccel = None,
            xMax = None, yMax = None, zMax = None, base = Axis(), x = Axis(), y = Axis(), z = Axis(), u = Axis(), v = Axis()):
        self.name = name
        self.updatePeriod = updatePeriod
        self.jogSpeed = jogSpeed
        self.maxTools = maxTools
        self.toolLimit = toolLimit
        self.maxAccel = maxAccel
        self.xMax = xMax # number
        self.yMax = yMax # number
        self.zMax = zMax # number
        self.base = base # Axis()
        self.x = x # Axis()
        self.y = y # Axis()
        self.z = z # Axis()
        self.u = u # Axis()
        self.v = v # Axis()
                    
    def load(self, fname):
        self.name = fname.split('.')[0]
        fh = QFile('config/' + fname)
        fh.open(QIODevice.ReadOnly)
        dom = QDomDocument()
        dom.setContent(fh)
        fh.close()
        root = dom.documentElement()
        if root.tagName() != "PRINTER":
            raise ValueError, "not a Printer XML file"
        self.updatePeriod = str(root.attribute("UPDATEPERIOD"))
        self.jogSpeed = str(root.attribute("JOGSPEED"))
        self.maxTools = str(root.attribute("MAXTOOLS"))
        self.toolLimit = str(root.attribute("TOOLLIMIT"))
        self.maxAccel = str(root.attribute("MAXACCEL"))
        self.xMax = str(root.attribute("XMAX"))
        self.yMax = str(root.attribute("YMAX"))
        self.zMax = str(root.attribute("ZMAX"))
        ## Base
        root = root.firstChild()
        child = root.toElement()
        self.base.direction = str(child.attribute("DIRECTION"))
        self.base.motor = str(child.attribute("MOTOR"))
        self.base.arange = str(child.attribute("RANGE"))
        self.base.limits = str(child.attribute("LIMITS"))
        self.base.increment = str(child.attribute("INCREMENT"))
        ## X Axis
        root = root.nextSibling()
        child = root.toElement()
        self.x.direction = str(child.attribute("DIRECTION"))
        self.x.motor = str(child.attribute("MOTOR"))
        self.x.arange = str(child.attribute("RANGE"))
        self.x.limits = str(child.attribute("LIMITS"))
        self.x.increment = str(child.attribute("INCREMENT"))
        ## Y Axis
        root = root.nextSibling()
        child = root.toElement()
        self.y.direction = str(child.attribute("DIRECTION"))
        self.y.motor = str(child.attribute("MOTOR"))
        self.y.arange = str(child.attribute("RANGE"))
        self.y.limits = str(child.attribute("LIMITS"))
        self.y.increment = str(child.attribute("INCREMENT"))
        ## Z Axis
        root = root.nextSibling()
        child = root.toElement()
        self.z.direction = str(child.attribute("DIRECTION"))
        self.z.motor = str(child.attribute("MOTOR"))
        self.z.arange = str(child.attribute("RANGE"))
        self.z.limits = str(child.attribute("LIMITS"))
        self.z.increment = str(child.attribute("INCREMENT"))
        ## U Axis
        root = root.nextSibling()
        child = root.toElement()
        self.u.direction = str(child.attribute("DIRECTION"))
        self.u.motor = str(child.attribute("MOTOR"))
        self.u.arange = str(child.attribute("RANGE"))
        self.u.limits = str(child.attribute("LIMITS"))
        self.u.increment = str(child.attribute("INCREMENT"))
        ## V Axis
        if int(self.maxTools) == 2:
            root = root.nextSibling()
            child = root.toElement()
            self.v.direction = str(child.attribute("DIRECTION"))
            self.v.motor = str(child.attribute("MOTOR"))
            self.v.arange = str(child.attribute("RANGE"))
            self.v.limits = str(child.attribute("LIMITS"))
            self.v.increment = str(child.attribute("INCREMENT"))
    
    def getPrintingDimensions(self):
        return int(self.xMax), int(self.yMax), int(self.zMax)
    
    def save(self, new):
        fh = QFile('config/' + self.name + '.printer')
        if new and fh.exists():
            return False
        if fh.open(QIODevice.WriteOnly):
            stream = QTextStream(fh)
            stream.setCodec(CODEC)
            stream << ("<?xml version='1.0' encoding='%s'?>\n<!DOCTYPE PRINTER>\n<PRINTER\n" % CODEC)
            stream << ("UPDATEPERIOD='%s'\nJOGSPEED='%s'\nMAXTOOLS='%s'\nTOOLLIMIT='%s'\nMAXACCEL='%s'\n"
                "XMAX='%s'\nYMAX='%s'\nZMAX='%s'\n>\n" % (self.updatePeriod, self.jogSpeed, self.maxTools,
                self.toolLimit, self.maxAccel, self.xMax, self.yMax, self.zMax))
            now = self.base
            stream << ("<BASE\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                % (now.direction, now.motor, now.arange, now.limits, now.increment))
            stream << ("</BASE>\n")
            now = self.x
            stream << ("<XAXIS\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                % (now.direction, now.motor, now.arange, now.limits, now.increment))
            stream << ("</XAXIS>\n")
            now = self.y
            stream << ("<YAXIS\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                % (now.direction, now.motor, now.arange, now.limits, now.increment))
            stream << ("</YAXIS>\n")
            now = self.z
            stream << ("<ZAXIS\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                % (now.direction, now.motor, now.arange, now.limits, now.increment))
            stream << ("</ZAXIS>\n")
            now = self.u
            stream << ("<UAXIS\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                % (now.direction, now.motor, now.arange, now.limits, now.increment))
            stream << ("</UAXIS>\n")
            if self.maxTools > 1:
                now = self.v
                stream << ("<VAXIS\nDIRECTION='%s'\nMOTOR='%s'\nRANGE='%s'\nLIMITS='%s'\nINCREMENT='%s'\n>\n"
                    % (now.direction, now.motor, now.arange, now.limits, now.increment))
                stream << ("</VAXIS>\n")
            stream << ("</PRINTER>\n")
            fh.close()
        return True
