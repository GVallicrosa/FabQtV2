from shapely.geometry import Point, LineString, Polygon
from core.python.layer import Layer
from core.python.path import Path
from math import *
from core.python.vtkLinePlotter import vtkLinePlotter
import vtk


# Vec class
class Vec(object):
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]
        
    def __str__(self):
        return '%s %s %s' % (self.x, self.y, self.z)

def slicevtk(vtkmesh, h, init = 0, end = 0):
    # Get limits
    xmin, xmax, ymin, ymax, zmin, zmax = vtkmesh.GetBounds()
    zmin += init
    zmax -= end

    # Plane to cut
    plane = vtk.vtkPlane()
    plane.SetOrigin(0, 0, zmin + h/2.0)
    plane.SetNormal(0, 0, 1)

    # Cut function
    cutter = vtk.vtkCutter()
    cutter.SetInput(vtkmesh)
    cutter.SetCutFunction(plane)
    cutter.GenerateCutScalarsOn()
    cutter.SetValue(0, 0)
    
    # Catch the points
    cutStrips = vtk.vtkStripper()
    cutStrips.SetInputConnection(cutter.GetOutputPort())
    cutStrips.Update()
    
    # Slice and create polygons
    layers = list()
    zreal = h/2.0
    z = zmin + h/2.0 # because set an reliable zero can broke the tip
    zs = list()
    while z <= zmax:
        zs.append(zreal)
        plane.SetOrigin(0,0,z)
        cutStrips.Update()
        polygons = list() # of the layer
        for i in range(cutStrips.GetOutput().GetNumberOfCells()): # number of polylines that will define polygons
            coords = tuple()
            for j in range(cutStrips.GetOutput().GetCell(i).GetPoints().GetNumberOfPoints()): # retrieve all points from the line
                vec = Vec(cutStrips.GetOutput().GetCell(i).GetPoints().GetPoint(j))
                coords += ((vec.x, vec.y),)
            polygon = Polygon(coords)
            polygons.append(polygon)
            #actor2 = dibuixa(polygon)
            #ren.AddActor(actor2)
        fora = list()
        for i in range(len(polygons)):
            if i not in fora:
                for j in range(len(polygons)):
                    if i == j:
                        pass
                    elif j in fora:
                        pass
                    elif polygons[i].contains(polygons[j]):
                        polygons[i] = polygons[i].difference(polygons[j])
                        fora.append(j)
        values = list()
        for val in fora:
            values.append(polygons[val])
        for val in values:
            polygons.remove(val)
        layers.append(polygons)
        z += h
        zreal += h
    return layers, zs
    
def slicevtkcontour(vtkmesh, h, init = 0, end = 0):
    # Get limits
    xmin, xmax, ymin, ymax, zmin, zmax = vtkmesh.GetBounds()
    zmin += init
    zmax -= end

    # Plane to cut
    plane = vtk.vtkPlane()
    plane.SetOrigin(0, 0, zmin + h/2.0)
    plane.SetNormal(0, 0, 1)

    # Cut function
    cutter = vtk.vtkCutter()
    cutter.SetInput(vtkmesh)
    cutter.SetCutFunction(plane)
    cutter.GenerateCutScalarsOn()
    cutter.SetValue(0, 0)
    
    # Catch the points
    cutStrips = vtk.vtkStripper()
    cutStrips.SetInputConnection(cutter.GetOutputPort())
    cutStrips.Update()
    
    # Slice and create polygons
    layers = list()
    #zreal = h/2.0
    z = zmin + h/2.0 # because set an reliable zero can broke the tip
    zs = list()
    polygons = list() # one for layer
    while z < zmax:
        zs.append(z)
        plane.SetOrigin(0,0,z)
        cutStrips.Update()
        coords = tuple()
        for j in range(cutStrips.GetOutput().GetCell(0).GetPoints().GetNumberOfPoints()): # retrieve all points from the line
            vec = Vec(cutStrips.GetOutput().GetCell(0).GetPoints().GetPoint(j))
            coords += ((vec.x, vec.y),)
        polygon = Polygon(coords)
        polygons.append(polygon)
        z += h
    return polygons, zs

def fill(fig, w, deg = 45, s = None): # Falta buffer a -w/2
    # fig = Polygon
    # w = path width
    # deg = degree angle fill pattern
    # s = separation of fill from contour
    if s is None:
        s = w
    # Angle to radians
    ang = deg*pi/180.0
    
    # Bounding box, get limits
    xmin = min(fig.buffer(0.99*w).exterior.envelope.boundary.xy[0])
    xmax = max(fig.buffer(0.99*w).exterior.envelope.boundary.xy[0])
    ymin = min(fig.buffer(0.99*w).exterior.envelope.boundary.xy[1])
    ymax = max(fig.buffer(0.99*w).exterior.envelope.boundary.xy[1])
    
    # Initial parameters
    cuts = list()
    if 90 > deg > 0: # Start from left bottom
        x = xmin - (ymax - ymin)/abs(tan(ang)) 
        y = ymin
        incx = abs(w/sin(ang))
        incy = 0
    elif -90 < deg < 0: # Start from left top
        x = xmin - (ymax - ymin)/abs(tan(ang))
        y = ymax
        incx = abs(w/sin(ang))
        incy = 0
    elif deg == 0:
        x = xmin
        y = ymin
        incx = 0
        incy = w
    elif abs(deg) == 90:
        x = xmin
        y = ymin
        incx = w
        incy = 0
    else: # Raise Exception
        raise 'Exception: wrong degree value [-90, 90].'
    
    # Obtain intersections
    cuts = list()
    while x < xmax:# - incx/2.0:
        line = LineString(((x, y),(xmax, xmax*tan(ang) + y - x*tan(ang)))) # Equacio linia: y = x*tan(deg) + (yo - xo*tan(deg))
        x += incx
        y += incy
        try:
            lines = list(line.intersection(fig.buffer(-s))) # multiple intersections
            for line in lines:
                cuts.append(line)
        except:
            lines = line.intersection(fig.buffer(-s)) # one intersection
            cuts.append(lines)
        if ang == 0 and y > ymax:
            x = xmax + 1
    
    # Create paths from intersections
    allx = list()
    ally = list()
    finished = False
    while not finished:
        x = list()
        y = list()
        if len(cuts)>0:
            pather = True
            # Add the first line and erase it !!!!!! need to check which point to take first
            firstline = cuts.pop(0)
            data = firstline.xy
            lastx = data[0][0]
            lasty = data[1][0]
            #x.append(lastx)
            #y.append(lasty)
            #if len(data[0]) > 1: # if the intersection is not only a point
                #lastx = data[0][1]
                #lasty = data[1][1]
                #x.append(lastx)
                #y.append(lasty)
            
            while pather:
                # Look for next line and erase if fits conditions
                distances = list()
                nextCandidates = list()
                idxs = list()
                
                # If it is the first line, test each point to choose from which is better to start
                if firstline is not None:
                    for segment in cuts:
                        val = 1.9*w
                        idx = None
                        if segment.boundary[0].distance(firstline.boundary[0]) <= val:
                            val = segment.boundary[0].distance(firstline.boundary[0])
                            idx = 0,0
                        if segment.boundary[0].distance(firstline.boundary[1]) <= val:
                            val = segment.boundary[0].distance(firstline.boundary[1])
                            idx = 0,1
                        if segment.boundary[1].distance(firstline.boundary[0]) <= val:
                            val = segment.boundary[1].distance(firstline.boundary[0])
                            idx = 1,0
                        if segment.boundary[1].distance(firstline.boundary[1]) <= val:
                            val = segment.boundary[1].distance(firstline.boundary[1])
                            idx = 1,1
                        if idx is not None:
                            nextCandidates.append(segment)
                            distances.append(val)
                            idxs.append(idx)
                
                # If not the firts line, only continue adding lines according to some conditions  
                else:
                    lastpoint = Point((lastx,lasty))
                    for segment in cuts:
                        if segment.distance(lastpoint) <= 1.9*w:
                            nextCandidates.append(segment)
                            distances.append(lastpoint.distance(segment))
                
                # Start bending lines
                if len(distances) == 0: # No candidates
                    pather = False
                else:
                    val = min(distances)
                    idx = distances.index(val)
                    line = nextCandidates[idx]
                    lastline = line
                    idx2 = cuts.index(line)
                    if firstline is not None:
                        # Add first line points and then continue adding lines
                        if idxs[idx][1] == 0:
                            lastpoint = firstline.boundary[1] # Start point
                            x.append(lastpoint.x)
                            y.append(lastpoint.y)
                            lastpoint = firstline.boundary[0]
                            x.append(lastpoint.x)
                            y.append(lastpoint.y)
                        else:
                            lastpoint = firstline.boundary[0] # Start point
                            x.append(lastpoint.x)
                            y.append(lastpoint.y)
                            lastpoint = firstline.boundary[1]
                            x.append(lastpoint.x)
                            y.append(lastpoint.y)
                        firstline = None

                    # Find nearest point of the line
                    point1 = line.boundary[0]#Point(data[0][0],data[1][0])
                    point2 = line.boundary[1]#Point(data[0][1],data[1][1])
                    if point1.distance(lastpoint) > 2.0*w and point2.distance(lastpoint) > 2.0*w:
                        pather = False
                    else:
                        cuts.pop(idx2) # Erase line
                        dist = point1.distance(lastpoint) - point2.distance(lastpoint)
                        if dist < 0: # Point 1 nearer
                            lastx = point1.xy[0][0]
                            lasty = point1.xy[1][0]
                            x.append(lastx)
                            y.append(lasty)
                            lastx = point2.xy[0][0]
                            lasty = point2.xy[1][0]
                            x.append(lastx)
                            y.append(lasty)
                        else: # Point 2 nearer
                            lastx = point2.xy[0][0]
                            lasty = point2.xy[1][0]
                            x.append(lastx)
                            y.append(lasty)
                            lastx = point1.xy[0][0]
                            lasty = point1.xy[1][0]
                            x.append(lastx)
                            y.append(lasty)
            allx.append(x)
            ally.append(y)
        else:
            finished = True

    return allx,ally

# Veure polygon
def dibuixa(polygon, z = 0, color = 0.5):
    plot = vtkLinePlotter()
    contour = polygon.exterior.xy
    x = contour[0]
    y = contour[1]
    for i in range(len(x)-1):
        vec1 = [0, 0, z]
        vec2 = [0, 0, z]
        vec1[0] = x[i]
        vec1[1] = y[i]
        vec2[0] = x[i+1]
        vec2[1] = y[i+1]
        plot.PlotLine(vec1, vec2, color)
        #color += 1.0/len(points)

    holes = polygon.interiors
    if len(holes) > 0:
        for hole in holes:
            x = hole.xy[0]
            y = hole.xy[1]
            for i in range(len(x)-1):
                vec1 = [0, 0, z]
                vec2 = [0, 0, z]
                vec1[0] = x[i]
                vec1[1] = y[i]
                vec2[0] = x[i+1]
                vec2[1] = y[i+1]
                plot.PlotLine(vec1, vec2, color)
    polydata, actor = plot.CreateActor()
    return actor
# Obtenir xs ys del contorn
def contorn(polygon):
    allx = list()
    ally = list()
    contour = polygon.exterior.xy
    x = contour[0]
    y = contour[1]
    xs = list()
    ys = list()
    for i in range(len(x)):
        xs.append(x[i])
        ys.append(y[i])
    allx.append(xs)
    ally.append(ys)

    holes = polygon.interiors
    if len(holes) > 0:
        for hole in holes:
            x = hole.xy[0]
            y = hole.xy[1]
            xs = list()
            ys = list()
            for i in range(len(x)):
                xs.append(x[i])
                ys.append(y[i])
            allx.append(xs)
            ally.append(ys)
    return allx, ally
    
def plot3d(x, y, z = 0):
    plot = vtkLinePlotter()
    color = 0
    for i in range(len(x)-1):
        vec1 = [0, 0, z]
        vec2 = [0, 0, z]
        vec1[0] = x[i]
        vec1[1] = y[i]
        vec2[0] = x[i+1]
        vec2[1] = y[i+1]
        plot.PlotLine(vec1, vec2, color)
        color += 1.0/len(x)
    polydata, actor = plot.CreateActor()
    return actor
