class Layer(object):
    #_contourSupport ## (list of path) future implementation for custom path planning
    _support (list of path)
    #_contourModel ## (list of path) future implementation for custom path planning
    _model (list of path)
    def __init__
    def getSupportLength()
    def getModelLenght()
    def optimize() # TSP algorithm to minimize the distance among all paths
