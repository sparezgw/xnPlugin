'''
Created on 2011-2-11

@author: sparezgw
'''

from platform import xnPlatform
from qjiangsanguo import qjsanguo


if __name__ == '__main__':
    info = {'email':'sparezgw@msn.com',
            'password':'xiaonei4me',
#            'flag':0,
#            'id':'224207693'
            } 
    xnpf = xnPlatform(info)
    if not xnpf.isLogin():
        xnpf.doLogin()
    
    qsg = qjsanguo(xnpf.opener)
    qsg.appStart()
    qsg.getServer()
    qsg.getPets(43323)
    
#    app = appMain(info)
#    app.start()