import vtk
import random
import os
from core.python.gcode import readGcode
from core.python.vtkLinePlotter import vtkLinePlotter
from core.skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins import export
from core.python.fablog import Fablog

logger = Fablog()

class Model(object):           
    
    def __init__(self, name = None, actor = None, mapper = None, supportMaterial = None, modelMaterial = None, layer = list(), vtkpolydata = None):
        self.name = name
        # 3D model
        self._actor = actor
        self._mapper = mapper
        self._vtkpolydata = vtkpolydata
        # model path
        self._slice_vtkpolydata = None
        self._slice_mapper = None
        self._slice_actor = None
        # support path
        self._support_vtkpolydata = None
        self._support_mapper = None
        self._support_actor = None
        # base path
        self._base_vtkpolydata = None
        self._base_mapper = None
        self._base_actor = None
        # properties
        self._supportMaterial = supportMaterial # string
        self._modelMaterial = modelMaterial # string
        # model layers
        self._layer = layer 
           
    def hasModel(self):
        if self._actor is None:
            return False
        else:
            return True
            
    def hasModelPath(self):
        if self._slice_actor is None:
            return False
        else:
            return True
            
    def hasSupportPath(self):
        if self._support_actor is None:
            return False
        else:
            return True
            
    def hasBasePath(self):
        if self._base_actor is None:
            return False
        else:
            return True
            
    def deletePath(self):# delete all data related to paths
        self._layer = list()
        self._slice_vtkpolydata = None
        self._slice_mapper = None
        self._slice_actor = None
        self._support_vtkpolydata = None
        self._support_mapper = None
        self._support_actor = None
        self._base_vtkpolydata = None
        self._base_mapper = None
        self._base_actor = None

    def load(self, fname): # from source, returns vtkPolydata, mapper and actor
        self.name = fname.split('/')[-1] # name with extension
        logger.log('Importing model: ' + self.name)
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
            self.setActor(actor)
        if extension.lower() == 'gcode':
            logger.log('Reading GCode...')
            ok, layers = readGcode(str(fname))
            if ok:
                self.setLayers(layers)
                logger.log('GCode correctly readed')
                self.layerValues = list()
                for layer in layers:
                    z = layer.readModelPaths()[0].read()[0].z # or others
                    self.layerValues.append(z)
            else:
                logger.log('Error importing GCode')
            self.generatePaths(layers)
        else:
            logger.log('No valid file extension for model import')
        
    def save(self): # writer to new file
        logger.log('Exporting temp STL of model %s...' % self.name)
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
        logger.log('End exporting')
            
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
        logger.log('Creating GCode...')
        os.remove('temp.stl')
        ok, layers = readGcode('temp_export.gcode') 
        logger.log('Reading GCode...')
        #os.remove('temp_export.gcode')
        if ok:
            self.setLayers(layers)
            logger.log('GCode correctly readed')
            #########################
            self.layerValues = list()
            for layer in layers:
                z = layer.readModelPaths()[0].read()[0].z # or others
                self.layerValues.append(z)
            #########################
        else:
            logger.log('Error importing GCode')
        self.generatePaths(layers)
        
    def getPathActor(self):
        return self._slice_actor
            
    def getSupportPathActor(self):
        return self._support_actor   
        
    def getBasePathActor(self):
        return self._base_actor 
            
    def generatePaths(self, layers, basic = True):
        color1 = 0#random.random()
        modelPlotter = vtkLinePlotter()
        if not basic:
            color2 = 0.5
            color3 = 1
            supportPlotter = vtkLinePlotter()
            basePlotter = vtkLinePlotter()
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
                    modelPlotter.PlotLine(vec1, vec2, color1)
            if not basic:
                for path in layer.readSupportPaths(): # path
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
                        supportPlotter.PlotLine(vec1, vec2, color2)
                for path in layer.readBasePaths(): # path
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
                        basePlotter.PlotLine(vec1, vec2, color3)
        polydata, mapper, actor = modelPlotter.CreateActor()
        self._slice_vtkpolydata = polydata
        self._slice_mapper = mapper
        self._slice_actor = actor
        if not basic:
            polydata, mapper, actor = supportPlotter.CreateActor()
            self._support_vtkpolydata = polydata
            self._support_mapper = mapper
            self._support_actor = actor
            polydata, mapper, actor = basePlotter.CreateActor()
            self._base_vtkpolydata = polydata
            self._base_mapper = mapper
            self._base_actor = actor
        
    def transform(self): # transformation = vtkMatrix4x4
        pass
