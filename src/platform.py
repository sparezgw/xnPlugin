'''
Created on 2011-2-11

@author: sparezgw

@class xnPlatform
'''
#import re,sys,time,string,os.path
#import urllib, urllib2, cookielib, json
import urllib, urllib2, cookielib

class xnPlatform:
    '''
    @param info: the information of account of RenRen.com
    
    @function doLogin: 
    @function isLogin:
    
    @summary: Some functions of RenRen(xiaonei) platform, such as 'login', 'logout', 'getFriendList' and etc.
    '''
    
    def __init__(self, info):
        '''
        Initial of XN class.
        '''
        
        self.cj = cookielib.LWPCookieJar()
        try:
            self.cj.revert('renren.cookies')
        except:
            None
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        self.info = info
        
    def doLogin(self):
        '''
        Function for login to RenRen.com
        '''
        params = {'autoLogin':'true','origURL':'http://www.renren.com/SysHome.do','domain':'renren.com'}
        params.update(self.info)
        req = urllib2.Request('http://passport.renren.com/PLogin.do', urllib.urlencode(params))
        print '-------======= Logging in! =======-------'
        oper = self.opener.open(req)
        if oper.geturl() == 'http://www.renren.com/home':
            self.cj.save('renren.cookies')
            print 'Login successfully!'
        else:
            print 'Something wrong in Login!'
            
    def isLogin(self):
        oper = self.opener.open('http://www.renren.com')
        if oper.geturl() != 'http://www.renren.com/home':
            print 'Not Login, need information to login!'
            return False
        else:
            print 'Already Login!';
            return True