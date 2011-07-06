import urllib2

def download(version):
    o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    fileURL = 'http://fabmetheus.crsndoo.com/files/%s_reprap_python_beanshell.zip' % version
    fh = o.open(fileURL)
    output = open('skeinforge.zip', "wb")
    chunk = fh.read()
    while chunk:
        output.write(chunk)
        chunk = fh.read()
    fh.close()
    output.close()
    
def extract():
    import zipfile
    fh = zipfile.ZipFile('skeinforge.zip', 'r')
    fh.extractall('core/skeinforge/')

currentVersion = 38
try:
    fh = urllib2.urlopen("http://fabmetheus.crsndoo.com/rss.xml")
    data = fh.readlines()
    print data
    print '========================================================'
    data = data[0]
    data = data.split('http://fabmetheus.crsndoo.com/files/')
    data = data[1]
    data = int(data[0:2])
    print data
    if data > currentVersion:
        print 'Please update'
        print 'http://fabmetheus.crsndoo.com/files/%s_reprap_python_beanshell.zip' % data
        #ask for download
        print 'Dowloading...',
        download(data)
        print 'done'
        print 'Extracting...',
        extract()
        print 'done'
    elif data == currentVersion:
        print 'Already lastest version'
    else:
        print 'Error'
except Exception, e:
    print "Failed to download:\n%s" % e
