#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import re
from glob import glob
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../support/'))
#sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../mishkal/lib/'))
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../mishkal'))
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), './lib'))
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../'))
from okasha2.baseWebApp import *
from okasha2.utils import fromFs, toFs

from adawaty import *

def test():
    # this requires python-paste package
    import logging
    from paste import httpserver

    d=fromFs(os.path.dirname(sys.argv[0]))
    LOG_FILENAME = os.path.join(d,u'tmp','logging_example.out')
    logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,)
    myLogger=logging.getLogger('Mishkal')

    #HB
    #h=logging.StreamHandler() # in production use WatchedFileHandler or RotatingFileHandler
    import logging.handlers
    h = logging.handlers.SysLogHandler(address = '/dev/log')
    #END HB
    
    h.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    myLogger.addHandler(h)
    myLogger.setLevel(logging.INFO) # in production use logging.INFO
    d=fromFs(os.path.dirname(sys.argv[0]))
    app=webApp(
      os.path.join(d,u'resources/templates'),
      staticBaseDir={u'/_files/':os.path.join(d,u'resources/files')},
	  logger=myLogger
    );
    # for options see http://pythonpaste.org/modules/httpserver.html

    # org
    httpserver.serve(app, host='0.0.0.0', port='8080')
    # END org
    
    # HL changes
    # import socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # result = sock.connect_ex(('0.0.0.0',8080))
    # if result == 1:
    #     httpserver.serve(app, host='0.0.0.0', port='8080')
    # else:
    #     print("Cannot start mishkal: a server is already up and running on 0.0.0.0:8080")
    # END HL changes


if __name__ == '__main__':
	test();
