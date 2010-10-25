#!/usr/bin/env python
class Layer(object):
    def __init__(self, modelPaths = tuple(), supportPaths = tuple()):
        self._model = modelPaths
        self._support = supportPaths
        self._base = tuple()
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
        
    def getBaseLenght(self):
        value = 0
        for i in range(len(self._base)):
            value += self._base[i].length()
        
    def getModelLenght(self):
        value = 0
        for i in range(len(self._model)):
            value += self._model[i].length()
            
    def getSupportLength(self):
        value = 0
        for i in range(len(self._support)):
            value += self._support[i].length()
           
    def getPathBaseNumber(self):
        return len(self._base)
            
    def getPathModelNumber(self):
        return len(self._model)
        
    def getPathSupportNumber(self):
        return len(self._support)
    
    def readBasePaths(self):
        return self._base
    
    def readModelPaths(self):
        return self._model
        
    def readSupportPaths(self):
        return self._support
                    
    def optimize(self): # TSP algorithm to minimize the distance among all paths
        pass
