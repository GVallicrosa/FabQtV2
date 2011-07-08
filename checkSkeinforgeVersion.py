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

def main():
    # Search current version
    try:
        fh = file('core/skeinforge/fabmetheus_utilities/version.txt', 'r')
        current = fh.readline()
        current = '20' + current
        current = current.replace('.','-')
        print 'Current version: ' + current 
        fh.close()
    except:
        current = 'nothing'
        print 'Current version: no skeinforge' 
    
    try:
        fh = urllib2.urlopen("http://fabmetheus.crsndoo.com/rss.xml")
        #print 'Checking online...'
        data = fh.readlines()
        data = data[0]
        fh.close()
        new = data.split('<item><title>')
        new = new[1]
        new = new[:10]
        version = data.split('http://fabmetheus.crsndoo.com/files/')
        version = version[1]
        version = int(version[0:2])
        print 'New version: ' + new + '  Number: ' + str(version)
        if not new == current:
            print 'Updating...'
            print '   Dowloading...'
            download(version)
            print '   Extracting...'
            extract()
            import os
            os.remove('skeinforge.zip')
        elif new == current:
            print 'Already lastest version'
        else:
            print 'Error'
    except Exception, e:
        print "Failed to download:\n%s" % e
        
if __name__ == '__main__':
    main()
