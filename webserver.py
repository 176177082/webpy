#!C:\Python27\ArcGIS10.2\python.exe  
# -*- coding: UTF-8 -*-
"""
__author__ = 'changxiong'
"""

import os, sys
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
webdir = '.'
port = 80

os.chdir(webdir)
srvraddr = ('', port)111
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()