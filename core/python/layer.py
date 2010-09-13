#!/usr/bin/env python
class Layer(object):
    def __init__(self, modelPaths = tuple(), supportPaths = tuple()):
        self._model = modelPaths
        self._support = supportPaths
        #self._contourSupport ## (list of path) future implementation for custom path planning
        #self._contourModel ## (list of path) future implementation for custom path planning
    
    def addModelPath(self, path = None):
        if path is None:
            return
        self._model = self._model + (path,)
        
    def delete(self):
        self._model = list()
        
    def addSupportPath(self, path = None):
        if path is None:
            return
        self._support.append(path)
        
    def getSupportLength(self):
        value = 0
        for i in range(len(self._support)):
            value += self._support[i].length()
            
    def getModelLenght(self):
        value = 0
        for i in range(len(self._model)):
            value += self._model[i].length()
            
    def getPathModelNumber(self):
        return len(self._model)
        
    def getPathSupportNumber(self):
        return len(self._support)
    
    def readModelPaths(self):
        return self._model
            
    def optimize(self): # TSP algorithm to minimize the distance among all paths
        pass
