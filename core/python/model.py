import vtk
import random

from core.skeinforge.skeinforge_application.skeinforge_plugins.craft_plugins import export

class Model(object):
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
        print '++ Importing model: ' + self.name
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
            self.setActor(actor)
        else:
            print 'No valid file extension'
        
    def save(self): # writer to new file
        print 'Exporting temp STL of model %s...' % self.name
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
        print 'End exporting...'
            
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
    
    def Slice(self): # calls skeinforge
        self.save()
        export.writeOutput('temp.stl')
        
    def transform(self): # transformation = vtkMatrix4x4
        pass
