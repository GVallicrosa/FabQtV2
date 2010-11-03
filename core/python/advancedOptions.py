class Options(object):
    def __init__(self):
        self.dict = dict()
        
    def save(self, opts):
        self.dict.update(opts)
