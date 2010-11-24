from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
from core.python.render import generateAxes

class QVTKRenderWindowInteractorCustom(QVTKRenderWindowInteractor):
    def __init__(self, parent = None):
        super(QVTKRenderWindowInteractorCustom, self).__init__(parent)
        self.camera = vtk.vtkCamera()
        self.camera.SetFocalPoint(0, 0, 0)
        self.camera.SetPosition(300, 0, 100)
        self.camera.SetViewUp(-1, 0, 0)
        #self.camera.SetParallelProjection(1)#######
        self.ren = vtk.vtkRenderer()
        self.ren.SetActiveCamera(self.camera)
        self.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.GetRenderWindow().AddRenderer(self.ren)
        self.AddObserver("KeyPressEvent", self.Keypress)
        self.ren.InteractiveOn()
        ## Variables
        self.tubeOn = False
        self.currentIndex = -1
        self.newActors = list()
        self.toolDict = None
        self.modelDict = None
        
    def AddActorCustom(self, model):
        for actor in [model._actor, model._slice_actor, model._support_actor, model._base_actor]:
            if actor is not None:
                self.ren.AddActor(actor)
            
    def customStart(self, printer):
        axesActor, XActor, YActor, ZActor = generateAxes(printer)
        XActor.SetCamera(self.camera)
        YActor.SetCamera(self.camera)
        ZActor.SetCamera(self.camera)
        base = vtk.vtkCubeSource()
        xmax, ymax, zmax = printer.getPrintingDimensions()
        base.SetBounds(-xmax/2, xmax/2, -ymax/2, ymax/2, -5, 0)
        baseMapper = vtk.vtkPolyDataMapper()
        baseMapper.SetInput(base.GetOutput())
        baseActor = vtk.vtkActor()
        baseActor.SetMapper(baseMapper)
        baseActor.PickableOff()
        self.ren.AddActor(axesActor)
        self.ren.AddActor(XActor)
        self.ren.AddActor(YActor)
        self.ren.AddActor(ZActor)
        self.ren.AddActor(baseActor)
        self.Initialize()
        self.ren.GetRenderWindow().Render()
        self.Start()
        
    def cutter(self):
        #plane = vtk.vtkPlane() 
        #plane.SetOrigin(0, 0, self.currentIndex -0.001) 
        #plane.SetNormal(0, 0, 1)
        #window = vtk.vtkImplicitWindowFunction()
        #window.SetImplicitFunction(plane)
        #window.SetWindowRange(0, 1) #(you will need to define the range)
        for model in self.modelDict.values():
            for actor in [model._actor, model._slice_actor, model._support_actor, model._base_actor]:
                if actor is not None:
                    actor.GetProperty().SetOpacity(0)
            print model.layerValues
            for polydata in [model._slice_vtkpolydata, model._support_vtkpolydata, model._base_vtkpolydata]:
                if polydata is not None:
                    i = self.currentIndex
                    if i < 0:
                        i = 0
                        self.currentIndex = -1
                    elif i > len(model.layerValues) - 1:
                        i = len(model.layerValues) - 1
                    plane = vtk.vtkPlane() 
                    plane.SetOrigin(0, 0, model.layerValues[i] -0.005) # some errors
                    plane.SetNormal(0, 0, 1)
                    window = vtk.vtkImplicitWindowFunction()
                    window.SetImplicitFunction(plane)
                    pathHeight = float(self.toolDict[str(model._modelMaterial)].pathHeight)
                    window.SetWindowRange(0, pathHeight/2.0)
                    clipper = vtk.vtkClipPolyData()
                    clipper.AddInput(polydata) 
                    clipper.SetClipFunction(window)
                    clipper.GenerateClippedOutputOn()
                    if self.tubeOn:
                        clipActor = self.tubeView(clipper, float(self.toolDict[str(model._modelMaterial)].pathWidth))
                    else:
                        clipMapper = vtk.vtkPolyDataMapper()
                        clipMapper.SetInputConnection(clipper.GetOutputPort())
                        clipActor = vtk.vtkActor()
                        clipActor.SetMapper(clipMapper)
                    self.ren.AddActor(clipActor)
                    self.newActors.append(clipActor)
        
    def Keypress(self, obj, event):
        key = obj.GetKeyCode()
        if self.modelDict is not None:
            if key in ['b', 'n', 'm', 'x']:
                for actor in self.newActors:
                        self.ren.RemoveActor(actor)
                self.newActors = list()
                if key == 'm':
                    self.currentIndex += 1
                    self.cutter()
                elif key == 'n':
                    self.currentIndex -= 1
                    self.cutter()
                elif key == 'b':
                    if self.tubeOn:
                        self.tubeOn = False
                    else:
                        self.tubeOn = True
                    self.cutter()
                elif key == 'x':
                    self.currentIndex = 1
                    for model in self.modelDict.values():
                        for actor in [model._slice_actor, model._support_actor, model._base_actor]:
                            if actor is not None:
                                actor.GetProperty().SetOpacity(1)
                self.ren.GetRenderWindow().Render()
            elif key == 'z':
                self.currentIndex = -1
            
    def tubeView(self, clipper, pathWidth = 1.2):
        tubes = vtk.vtkTubeFilter()
        tubes.SetInputConnection(clipper.GetOutputPort())
        tubes.SetRadius(pathWidth/2.0)
        tubes.SetNumberOfSides(4)
        tubesMapper = vtk.vtkPolyDataMapper()
        tubesMapper.SetInputConnection(tubes.GetOutputPort())
        tubesActor = vtk.vtkActor()
        tubesActor.SetMapper(tubesMapper)
        return tubesActor
            
    def RemoveActorCustom(self, actor):
        if actor is not None:
            self.ren.RemoveActor(actor)
        
