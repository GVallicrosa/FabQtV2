#!/usr/bin/env python
class Layer(object):
    def __init__(self, modelPaths = tuple(), supportPaths = tuple(), basePaths = tuple()):
        self._model = modelPaths
        self._support = supportPaths
        self._base = basePaths
        #self._contourSupport ## (list of path) future implementation for custom path planning
        #self._contourModel ## (list of path) future implementation for custom path planning

    def addBasePath(self, path = None):
        if path is None:
            return
        self._base += (path,)
    
    def addModelPath(self, path = None):
        if path is None:
            return
        self._model += (path,)
        
    def addSupportPath(self, path = None):
        if path is None:
            return
        self._support += (path,)
        
    def delete(self):
        self._model = tuple()
        self._support = tuple()
        self._base = tuple()
        
    def getBaseLenght(self):
        value = 0
        for i in range(len(self._base)):
            value += self._base[i].length()
        
    def getModelLenght(self):
        value = 0
        for i in range(len(self._model)):
            value += self._model[i].length()
            
    def getSupportLenght(self):
        value = 0
        for i in range(len(self._support)):
            value += self._support[i].length()
           
    def getPathBaseNumber(self):
        return len(self._base)
            
    def getPathModelNumber(self):
        return len(self._model)
        
    def getPathSupportNumber(self):
        return len(self._support)
        
    def hasBasePaths(self):
        if self._base:
            return True
        else:
            return False
        
    def hasModelPaths(self):
        if self._model:
            return True
        else:
            return False
            
    def hasSupportPaths(self):
        if self._support:
            return True
        else:
            return False
    
    def readBasePaths(self):
        return self._base
    
    def readModelPaths(self):
        return self._model
        
    def readSupportPaths(self):
        return self._support
                    
    def optimize(self): # TSP algorithm to minimize the distance among all paths
        pass
