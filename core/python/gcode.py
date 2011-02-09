#!/usr/bin/env python
from core.python.layer import Layer
from core.python.path import Path
from core.skeinforge.fabmetheus_utilities.vector3 import Vector3
import codecs

def readGcode(fname):
    error = None
    fh = None
    try:
        fh = codecs.open(unicode(fname), "rU", 'UTF8')
        text = fh.readlines()
        linemax = len(text)
        printing = False
        lastZ = None
        kind = 'model'
        layerlist = list()
        lino = 18
        for line in text: #avoiding useless information
            if line.startswith('M10'):
            # M101 Turn extruder on forward
            # M103 Turn extruder off
            # M104 Temperature control
                if 'M101' in line: # When starts to extrude a new path is starting
                    printing = True
                    path = Path()
                    path.addVector(vec) # We are in the last point when starting to extrude
                elif 'M103' in line:
                    printing = False
                    try:
                        if kind == 'base':
                            layer.addBasePath(path) # Save path to its layer
                        if kind == 'support':
                            layer.addSupportPath(path) # Save path to its layer
                        if kind == 'model':
                            layer.addModelPath(path) # Save path to its layer
                    except:
                        pass
                elif 'M104' in line: # temperature hack
                    m, s = line.split(' ')
                    s = float(s[1:])
                    if s == 200: # base
                        kind = 'base'
                    elif s == 250: # support
                        kind = 'support'
                    elif s == 300: # model
                        kind = 'model'
                    elif s == 0: # end
                        break
            elif 'G1' in line:
            # G1 Coordinated Motion Implemented - supports X, Y, and Z axes.
                sline = line.split(' ')
                if len(sline) >= 4:
                    if len(sline) == 5:
                        g, x, y, z, f = line.split(' ') # Take all parameters splitting in spaces
                    elif len(sline) == 4:
                        g, x, y, z = line.split(' ') # Same when no SPEED is active
                    x = float(x[1:]) # Avoids the character X, and return a float
                    y = float(y[1:]) # Avoids the character Y, and return a float
                    z = float(z[1:]) # Avoids the character Z, and return a float
                    vec = Vector3(x, y, z) # Creates a vector
                    if printing: # if extruding, adds a vector
                        path.addVector(vec)
                    if not z == lastZ: # Z change = layer change
                        lastZ = z
                        try:
                            layerlist.append(layer)
                        except: # Layer no exists at first execution
                            pass
                        layer = Layer()
            lino += 1
            if lino == linemax:
                layerlist = layerList.append(layer)
            line = fh.readline()
    except (IOError, OSError, ValueError), e:
        error = "Failed to load: %s on line %d" % (e, lino)
        print error
    finally:
        if fh is not None:
            fh.close()
        if error is not None:
            return False, error
        return True, layerlist
