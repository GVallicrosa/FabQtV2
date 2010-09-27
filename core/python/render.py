from __future__ import division
import vtk

def generateAxes():
    axes = vtk.vtkAxes()
    axes.SetOrigin(0, 0, 0)
    axes.SetScaleFactor(40)
    axesTubes = vtk.vtkTubeFilter()
    axesTubes.SetInputConnection(axes.GetOutputPort())
    axesTubes.SetRadius(2)
    axesTubes.SetNumberOfSides(6)
    axesMapper = vtk.vtkPolyDataMapper()
    axesMapper.SetInputConnection(axesTubes.GetOutputPort())
    axesActor = vtk.vtkActor()
    axesActor.SetMapper(axesMapper)
    XText = vtk.vtkVectorText()
    XText.SetText('X')
    XTextMapper = vtk.vtkPolyDataMapper()
    XTextMapper.SetInputConnection(XText.GetOutputPort())
    XActor = vtk.vtkFollower()
    XActor.SetMapper(XTextMapper)
    XActor.SetScale(10, 10, 10)
    XActor.SetPosition(40, -20, 0)
    XActor.GetProperty().SetColor(1, 0, 0)
    YText = vtk.vtkVectorText()
    YText.SetText('Y')
    YTextMapper = vtk.vtkPolyDataMapper()
    YTextMapper.SetInputConnection(YText.GetOutputPort())
    YActor = vtk.vtkFollower()
    YActor.SetMapper(YTextMapper)
    YActor.SetScale(10, 10, 10)
    YActor.SetPosition(-20, 40, 0)
    YActor.GetProperty().SetColor(1, 1, 0)
    ZText = vtk.vtkVectorText()
    ZText.SetText('Z')
    ZTextMapper = vtk.vtkPolyDataMapper()
    ZTextMapper.SetInputConnection(ZText.GetOutputPort())
    ZActor = vtk.vtkFollower()
    ZActor.SetMapper(ZTextMapper)
    ZActor.SetScale(10, 10, 10)
    ZActor.SetPosition(-20, -20, 40)
    ZActor.GetProperty().SetColor(0, 1, 0)
    return axesActor, XActor, YActor, ZActor
    
def moveToOrigin(actor):
    actor.SetPosition(0, 0, 0)
    xmin, xmax = actor.GetXRange()
    ymin, ymax = actor.GetYRange()
    zmin, zmax = actor.GetZRange()
    actor.SetPosition(-xmin, -ymin, -zmin)
    
def validateMove(actor, printer):
    XMAX, YMAX, ZMAX = printer.getPrintingDimensions()
    x, y, z = actor.GetPosition()
    xmin, xmax = actor.GetXRange()
    ymin, ymax = actor.GetYRange()
    zmin, zmax = actor.GetZRange()
    if xmin < -XMAX/2 and not xmax > XMAX/2:
        newx = x - (xmin + XMAX/2)
    elif xmax > XMAX/2 and not xmin < -XMAX/2:
        newx = x - (xmax - XMAX/2)
    elif xmin >= -XMAX/2 and xmax <= XMAX/2:
        newx = x
    else:
        return False # Model too big
    if ymin < -YMAX/2 and not ymax > YMAX/2:
        newy = y - (ymin + YMAX/2)
    elif ymax > YMAX/2 and not ymin < -YMAX/2:
        newy = y - (ymax - YMAX/2)
    elif ymin >= -YMAX/2 and ymax <= YMAX/2:
        newy = y
    else:
        return False # Model too big
    if zmin < 0 and not zmax > ZMAX:
        newz = z - zmin
    elif zmax > ZMAX and not zmin < 0:
        newz = z - zmin # Always touching the table
    elif zmin >= 0 and zmax <= ZMAX:
        newz = z - zmin
    else:
        return False # Model too big
    actor.SetPosition(newx, newy, newz)
    return True    
    
    
