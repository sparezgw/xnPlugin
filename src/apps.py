'''
Created on 2011-2-11

@author: sparezgw

@class app
'''
import re, sys, urllib2

class app:
    '''
    @param openr: The opener of main platform
    
    @function
    
    @summary: The foundation class of applications.
    '''

    def __init__(self, pf):
        '''
        Initital of class
        '''
        self.openr = pf
        
    def toFile(self, data, file):
        f = open(file, 'w')
        f.write(data)
        f.close()
        
    def getUrl(self, pattern, data):
        try:
            url = re.search(pattern,data).group(1)
        except:
            print 'URL got ERROR!'
            sys.exit()
        else:
            return url
        
    def getData(self, url, tofile=False, file=''):
        req = urllib2.Request(url)
        data = self.openr.open(req).read()
        if tofile:
            self.toFile(data, file)
            return True
        else:
            return data