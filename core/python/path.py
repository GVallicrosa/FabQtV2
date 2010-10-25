#!/usr/bin/env python
class Path(object):
    def __init__(self, vectorList = tuple()):
        self._vector = vectorList
        
    def addVector(self, vector = None):
        if vector is None:
            return
        self._vector = self._vector + (vector,)
        
    def getVector(self):
        return self._vector
        
    def __len__(self):
        return len(self._vector)
        
    def length(self):
        value = 0
        for i in range(len(self._vector) - 1):
            value += self._vector[i].distance(self._vector[i + 1])
        return value
        
    def read(self):
        return self._vector
        
    def delete(self):
        self._vector = list()
