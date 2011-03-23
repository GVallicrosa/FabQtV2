import vtk
import random
import os
from core.python.gcode import readGcode
from core.python.vtkLinePlotter import vtkLinePlotter
from core.skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins import export
from core.python.fablog import Fablog
from core.python.planner import Vec, slicevtk, fill
from core.python.layer import Layer
from core.python.path import Path

logger = Fablog()

class Model(object):           
    
    def __init__(self, name = None, actor = None, supportMaterial = None, modelMaterial = None, layer = list(), vtkpolydata = None):
        self.name = name
        # 3D model
        self._actor = actor
        self._vtkpolydata = vtkpolydata # basic data
        # model path
        self._slice_vtkpolydata = None
        self._slice_actor = None
        # support path
        self._support_vtkpolydata = None
        self._support_actor = None
        # base path
        self._base_vtkpolydata = None
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
        self._slice_actor = None
        self._support_vtkpolydata = None
        self._support_actor = None
        self._base_vtkpolydata = None
        self._base_actor = None

    def load(self, fname): # from source, returns vtkPolydata and actor
        self.name = fname.split('/')[-1] # filename with extension
        logger.log('Importing model: ' + self.name)
        extension = fname.split('.')[1]
        extension = extension.lower()
        if extension == 'stl': 
            importer = vtk.vtkSTLReader()
            importer.SetFileName(str(fname))
            vtkPolyData = importer.GetOutput()
            self.setPolyData(vtkPolyData)
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInput(vtkPolyData)
            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetColor(random.random(), random.random(), random.random()) # Colorizes randomly
            actor.GetProperty().SetOpacity(0.5) # Some transparency
            self.setActor(actor)
        #if extension == '3ds':
            #importer = vtk.vtk3DSImporter()
            #importer.ComputeNormalsOn()
            #importer.SetFileName(str(fname))
            #importer.Read()
            #importer.GeneratePolyData()
        if extension == 'gcode':
            logger.log('Reading GCode...')
            ok, layers = readGcode(str(fname))
            if ok:
                self.setLayers(layers)
                logger.log('GCode correctly readed')
                self.layerValues = list()
                for layer in layers:
                    if layer.hasModelPaths():
                        z = layer.getModelPaths()[0].read()[0].z
                    elif layer.hasBasePaths():
                        z = layer.getBasePaths()[0].read()[0].z
                    elif layer.hasSupportPaths():
                        z = layer.getSupportPaths()[0].read()[0].z
                    else: # to future erase
                        z = layer.getModelPaths()[0].read()[0].z
                    self.layerValues.append(z)
                self.pathHeight = float(layers[1].getModelPaths()[0].read()[0].z) - float(layers[0].getModelPaths()[0].read()[0].z)
            else:
                logger.log('Error importing GCode')
            self.generatePaths(layers)
        else:
            logger.log('No valid file extension for model import')
        
    def save(self): # writer to new file
        logger.log('Exporting temp STL of model %s...' % self.name)
        # Extract transformations done to the actor
        matrix = vtk.vtkMatrix4x4() 
        self.getActor().GetMatrix(matrix)
        # Apply transformation
        transform = vtk.vtkTransform()
        transform.SetMatrix(matrix)
        # T
        t_filter = vtk.vtkTransformPolyDataFilter()
        t_filter.SetInput(self.getPolyData())
        t_filter.SetTransform(transform)
        # Triangle filter
        #vtkTriangleFilter
        # Clean Polydata
        #vtkcleanpolydata
        # Simplify the model
        #vtk.vtkDecimate
        # Save data to a STL file
        writer = vtk.vtkSTLWriter()
        writer.SetFileName('temp.stl')
        writer.SetInputConnection(t_filter.GetOutputPort())
        writer.SetFileTypeToBinary()
        writer.Write()
        logger.log('End exporting')
            
    def getActor(self): # if no one set yet return false or null
        return self._actor
   
    def getModelMaterial(self): # if no one set yet return false or null
        return self._modelMaterial
        
    def getPolyData(self):
        return self._vtkpolydata
    
    def getSupportMaterial(self): # if no one set yet return false or null
        return self._supportMaterial
            
    def setActor(self, actor): # points to private attribute _actor
        self._actor = actor
        
    def setModelMaterial(self, material):
        self._modelMaterial = material
        
    def setPolyData(self, polyData):
        self._vtkpolydata = polyData
        
    def setSupportMaterial(self, material):
        self._supportMaterial = material
        
    def setLayers(self, layers):
        self._layer = layers
    
    def SliceCustom(self, toolDict, onlycontour = False): ######################################################
        logger.log('Custom slice starting...')
        
        # Get model and apply transformations done
        matrix = vtk.vtkMatrix4x4() 
        self.getActor().GetMatrix(matrix)
        transform = vtk.vtkTransform()
        transform.SetMatrix(matrix)
        t_filter = vtk.vtkTransformPolyDataFilter()
        t_filter.SetInput(self.getPolyData())
        t_filter.SetTransform(transform)
        t_filter.Update()
        vtkmesh = t_filter.GetOutput()
        
        # Get path height and path width
        tool = toolDict[str(self.getModelMaterial())]
        h = float(tool.pathHeight)
        w = float(tool.pathWidth)
        
        # Slice and get polygons of each layer
        layerspoly, zs = slicevtk(vtkmesh, h)
        assert len(layerspoly) == len(zs)
        self.layerValues = zs
        
        # Start gathering points
        deg = 45
        layerList = list()
        for i in range(len(layerspoly)):
            # Get polygons of each layer
            polygons = layerspoly[i]
            # Get current layer z
            z = zs[i]
            # Create layer
            layer = Layer()
            for polygon in polygons:
                # Extract contours
                #### Exterior
                contour = polygon.exterior.xy
                xs = contour[0]
                ys = contour[1]
                for a in range(len(xs)):
                    if a == 0:
                        path = Path()
                    vec = Vec([xs[a], ys[a], z])
                    path.addVector(vec)
                    if a == len(xs)-1:
                            layer.addModelPath(path)
                            
                #### Interiors = Holes
                interiors = polygon.interiors
                for interior in interiors:
                    xs = interior.xy[0]
                    ys = interior.xy[1]
                    for a in range(len(xs)):
                        if a == 0:
                            path = Path()
                        vec = Vec([xs[a], ys[a], z])
                        path.addVector(vec)
                        if a == len(xs)-1:
                                layer.addModelPath(path)
                
                # Calculate filling paths
                allx,ally = fill(polygon, w, deg)
                for j in range(len(allx)):
                    # Take each path points
                    xs = allx[j]
                    ys = ally[j]
                    for k in range(len(xs)):
                        # Add points to path
                        if k == 0:
                            path = Path()
                        vec = Vec([xs[k], ys[k], z])
                        path.addVector(vec)
                        if k == len(xs)-1:
                            layer.addModelPath(path)
            layerList.append(layer)
            deg = -deg
            
        # Generate actors for paths
        self.generatePaths(layerList)
    
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
            self.layerValues = list()
            for layer in layers:
                if layer.hasModelPaths():
                    z = layer.getModelPaths()[0].read()[0].z
                elif layer.hasBasePaths():
                    z = layer.getBasePaths()[0].read()[0].z
                elif layer.hasSupportPaths():
                    z = layer.getSupportPaths()[0].read()[0].z
                self.layerValues.append(z)
        else:
            logger.log('Error importing GCode')
        self.generatePaths(layers)
        
    def getPathActor(self):
        return self._slice_actor
            
    def getSupportPathActor(self):
        return self._support_actor   
        
    def getBasePathActor(self):
        return self._base_actor 
            
    def generatePaths(self, layers):
        color1 = 0 #random.random()
        color2 = 0.5
        color3 = 1
        modelPlotter = vtkLinePlotter()
        supportPlotter = vtkLinePlotter()
        basePlotter = vtkLinePlotter()
        base = False
        support = False  
        for layer in layers: # layer
            for path in layer.getModelPaths(): # path
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
            for path in layer.getSupportPaths(): # path
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
                    support = True
            for path in layer.getBasePaths(): # path
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
                    base = True
        polydata, actor = modelPlotter.CreateActor()
        self._slice_vtkpolydata = polydata
        self._slice_actor = actor
        if support:
            polydata, actor = supportPlotter.CreateActor()
            self._support_vtkpolydata = polydata
            self._support_actor = actor
        if base:
            polydata, actor = basePlotter.CreateActor()
            self._base_vtkpolydata = polydata
            self._base_actor = actor
        
    def transform(self): # transformation = vtkMatrix4x4
        pass
