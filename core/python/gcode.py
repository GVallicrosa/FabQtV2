#!/usr/bin/env python
from core.python.layer import Layer
from core.python.path import Path
from core.python.vector3 import Vector3
import codecs

CODEC = 'UTF8'

def readGcode(fname):
    error = None
    fh = None
    try:
        fh = codecs.open(unicode(fname), "rU", CODEC)
        lino = 0
        printing = False
        lastZ = None
        layerList = list()
        line = fh.readline()
        while line:
            if 'M' in line:
            #M101 Turn extruder on Forward
            #M103 Turn extruder off.
                if 'M101' in line:
                    printing = True # new path
                    path = Path()
                elif 'M103' in line:
                    printing = False # close path
                    try:
                        layer.addModelPath(path)
                    except:
                        pass                    
            if printing:
                if 'G1' in line:
                #G0 Rapid Motion Implemented - supports X, Y, and Z axes.
                #G1 Coordinated Motion Implemented - supports X, Y, and Z axes.
                #G2 Arc - Clockwise Not used by Skienforge
                #G3 Arc - Counter Clockwise Not used by Skienforge
                #G4 Dwell Implemented.
                #G20 Inches as units Implemented.
                #G21 Millimetres as units Implemented.
                #G28 Go Home Implemented. (X = -135mm, Y = 100mm, Z = 0mm)
                #G90 Absolute Positioning Implemented. V1.0.5
                #G92 Set current as home Implemented V1.0.5
                    g, x, y, z, f = line.split(' ')
                    x = float(x[1:]) # Avoids the character X, and return a float
                    y = float(y[1:])
                    z = float(z[1:])
                    vec = Vector3(x, y, z)
                    path.addVector(vec)
                    if not z == lastZ: # Z change = layer change
                        lastZ = z
                        try:
                            layerList.append(layer)
                        except: # Layer no exists at first execution
                            pass
                        layer = Layer()
            lino += 1
            line = fh.readline()
    except (IOError, OSError, ValueError), e:
        error = "Failed to load: %s on line %d" % (e, lino)
    finally:
        if fh is not None:
            fh.close()
        if error is not None:
            return False, error
        return True, layerList
