import vtk
import random
import logging
import os
from core.python.gcode import readGcode
from core.python.vtkLinePlotter import vtkLinePlotter

from core.skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins import export
logger = logging.getLogger('core.python.model')

class Model(object):           
            
    _slice_vtkpolydata = None
    _slice_mapper = None
    _slice_Actor = None
    
    def __init__(self, name = None, actor = None, mapper = None, supportMaterial = None, modelMaterial = None, layer = list(), vtkpolydata = None):
        self.name = name
        self._actor = actor
        self._mapper = mapper
        self._supportMaterial = supportMaterial
        self._modelMaterial = modelMaterial
        self._layer = layer
        self._vtkpolydata = vtkpolydata

    def load(self, fname): # from source, returns vtkPolydata, mapper and actor
        self.name = fname.split('/')[-1] # name with extension
        logger.debug('++ Importing model: ' + self.name)
        extension = fname.split('.')[1]
        if extension.lower() == 'stl': 
            reader = vtk.vtkSTLReader()
            reader.SetFileName(str(fname))
            vtkPolyData = reader.GetOutput()
            self.setPolyData(vtkPolyData)
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInput(vtkPolyData)
            self.setMapper(mapper)
            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetColor(random.random(), random.random(), random.random()) # Colorizes randomly
            actor.GetProperty().SetOpacity(0.5)
            actor.GetProperty()
            self.setActor(actor)
        else:
            logger.debug('No valid file extension')
        
    def save(self): # writer to new file
        logger.debug('Exporting temp STL of model %s...' % self.name)
        # Extract transformations done to the actor
        matrix = vtk.vtkMatrix4x4() 
        self.readActor().GetMatrix(matrix)
        # Apply transformation
        transform = vtk.vtkTransform()
        transform.SetMatrix(matrix)
        t_filter = vtk.vtkTransformPolyDataFilter()
        t_filter.SetInput(self.readPolyData())
        t_filter.SetTransform(transform)
        # Save data to a STL file
        writer = vtk.vtkSTLWriter()
        writer.SetFileName('temp.stl')
        writer.SetInputConnection(t_filter.GetOutputPort())
        writer.SetFileTypeToBinary()
        writer.Write()
        logger.debug('End exporting...')
            
    def readActor(self): # if no one set yet return false or null
        return self._actor
    
    def readMapper(self): # if no one set yet return false or null
        return self._mapper
   
    def readModelMaterial(self): # if no one set yet return false or null
        return self._modelMaterial
        
    def readPolyData(self):
        return self._vtkpolydata
    
    def readSupportMaterial(self): # if no one set yet return false or null
        return self._supportMaterial
            
    def setActor(self, actor): # points to private attribute _actor
        self._actor = actor
        
    def setMapper(self, mapper): # points to private attribute _mapper
        self._mapper = mapper
        
    def setModelMaterial(self, material):
        self._modelMaterial = material
        
    def setPolyData(self, polyData):
        self._vtkpolydata = polyData
        
    def setSupportMaterial(self, material):
        self._supportMaterial = material
        
    def setLayers(self, layers):
        self._layer = layers
    
    def Slice(self): # calls skeinforge
        self.save()
        export.writeOutput('temp.stl')
        os.remove('temp.stl')
        ok, layers = readGcode('temp_export.gcode')
        #os.remove('temp_export.gcode')
        if ok:
            self.setLayers(layers)
        else:
            logger.debug('Error importing GCode')
        self.generatePaths(layers)
        
    def getPathActor(self):
        return self._slice_actor
            
    def generatePaths(self, layers):
        color = random.random()
        linePlotter = vtkLinePlotter()
        for layer in layers: # layer
            for path in layer.readModelPaths(): # path
                vectors = path.read()
                for i in range(len(vectors) - 1): # vector
                    vec1 = [0, 0, 0]
                    vec2 = [0, 0, 0]
                    vec1[0] = vectors[i].x
                    vec1[1] = vectors[i].y
                    vec1[2] = vectors[i].z
                    vec2[0] = vectors[i + 1].x
                    vec2[1] = vectors[i + 1].y
                    vec2[2] = vectors[i + 1].z
                    linePlotter.PlotLine(vec1, vec2, color)
        mapper, actor = linePlotter.CreateActor()
        self._slice_mapper = mapper
        self._slice_actor = actor
        
    def transform(self): # transformation = vtkMatrix4x4
        pass
