'''
Created on 2011-2-11

@author: sparezgw
'''
import urllib2
from apps import app

class qjsanguo(app):
    '''
    @summary: The class of QJiangSanGuo application in RenRen.com
    '''

    def appStart(self):
        req = urllib2.Request('http://apps.renren.com/qjiangsanguo/?origin=104')
        data = self.openr.open(req).read()
        #self.toFile(data, 'index.html')
        url = self.getUrl('iframe.*iframe_canvas.*iframe_canvas.*src=\"(.*?)\"', data).replace('&amp;','&')
        self.getData(url, True, 'index.html')
    
    
    
        
        
    def getServer(self):
        url = 'http://renren.qjsg.the9.com/handler/server.ashx?rancode=586276ead57aab98fc188722e2f97e06'
        self.toFile(self.getData(url), 'server.xml')
        
    def getPets(self, uid):
        url = 'http://renren.qjsg.the9.com/handler/user/pets.ashx?userid=' + uid
        self.getData(url, True, 'pets.xml')
    
    
    def viewPets(self):
        self.getPets(43323)
        