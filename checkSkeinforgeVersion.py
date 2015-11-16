import requests

def download(version):
    #o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    fileURL = 'http://fabmetheus.crsndoo.com/files/%s_reprap_python_beanshell.zip' % version
    data = requests.get(fileURL).content
    output = open('skeinforge.zip', "wb")
    output.write(data)
    
    #chunk = fh.read()
    #while chunk:
      #  output.write(chunk)
     #   chunk = fh.read()
    #fh.close()
    output.close()
    
def extract():
    import zipfile
    fh = zipfile.ZipFile('skeinforge.zip', 'r')
    fh.extractall('core/skeinforge/')

def main():
    have = False
    # Search current version
    try:
        fh = file('core/skeinforge/fabmetheus_utilities/version.txt', 'r')
        current = fh.readline()
        current = '20' + current
        current = current.replace('.','-')
        print 'Current version: ' + current 
        fh.close()
        have = True
    except:
        current = 'nothing'
        print 'Skeinforge: not in disk' 
    
    try:
        r = requests.get("http://fabmetheus.crsndoo.com/rss.xml")
        print 'Checking online...'
        data = r.content
        date = data.split('<item><title>')[1][:10]
        version = int(data.split('http://fabmetheus.crsndoo.com/files/')[1][:2])
        print 'New version: ' + date + '  Number: ' + str(version)
        if not date == current:
            update = True
            if have:
                ans = raw_input('Do you want to update skeinforge? (Y/N): ')
                if not ans.lower() == 'y':
                    update = False
                
            if update:
                print 'Updating...'
                print '   Dowloading...'
                download(version)
                print '   Extracting...'
                extract()
                import os
                os.remove('skeinforge.zip')
        elif date == current:
            print 'Already lastest version'
        else:
            print 'Error'
    except Exception, e:
        print "Failed to download:\n%s" % e
        
if __name__ == '__main__':
    main()
