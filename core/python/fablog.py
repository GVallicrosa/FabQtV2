import logging
from PyQt4.QtCore import QString, SIGNAL, QObject

class Fablog(QObject):
    def __init__(self):
        super(Fablog, self).__init__()
        logging.basicConfig(filename='log.txt', level=logging.DEBUG)
        self.logger = logging.getLogger("Fablog")
    
    def log(self, text):
        self.logger.debug(text)
        self.emit(SIGNAL('Fablogging'), text)
