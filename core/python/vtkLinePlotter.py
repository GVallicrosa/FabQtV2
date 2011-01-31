import vtk

class vtkLinePlotter(object):

    def __init__(self):
        self.m_scalarMin = 0.0
        self.m_scalarMax = 1.0
        self.m_lookupTable = None
        self.m_curPointID = 0
        self.m_allLineWidth = 1

        self.m_points = vtk.vtkPoints()
        self.m_lines = vtk.vtkCellArray()
        self.m_lineScalars = vtk.vtkFloatArray()

    def SetScalarRange(self, minval, maxval):
        self.m_scalarMin = minval
        self.m_scalarMax = maxval

    def SetLookupTable(self, table):
        self.m_lookupTable = table

    def PlotLine(self, m, n, scalar):
        self.m_lineScalars.SetNumberOfComponents(1)
        self.m_points.InsertNextPoint(m)
        self.m_lineScalars.InsertNextTuple1(scalar)
        self.m_points.InsertNextPoint(n)
        self.m_lineScalars.InsertNextTuple1(scalar)
        self.m_lines.InsertNextCell(2)
        self.m_lines.InsertCellPoint(self.m_curPointID)
        self.m_lines.InsertCellPoint(self.m_curPointID + 1)
        self.m_curPointID += 2

    def SetAllLineWidth(self, width):
        self.m_allLineWidth = width
        
    def CreatePolyData(self):
        '''Create poly data '''
        polyData = vtk.vtkPolyData()
        polyData.SetPoints(self.m_points)
        polyData.SetLines(self.m_lines)
        polyData.GetPointData().SetScalars(self.m_lineScalars)
        return polyData

    def CreateActor(self):
        '''Create poly data'''
        polydata = self.CreatePolyData()
        #create a color lookup table
        if self.m_lookupTable is None:
            m_lookupTable = vtk.vtkLookupTable()
        #create mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(self.CreatePolyData())
        mapper.SetLookupTable(self.m_lookupTable)
        mapper.SetColorModeToMapScalars()
        mapper.SetScalarRange(self.m_scalarMin, self.m_scalarMax)
        mapper.SetScalarModeToUsePointData()
        #create actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetLineWidth(self.m_allLineWidth)
        return polydata, actor
