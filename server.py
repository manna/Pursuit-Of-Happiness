#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("lagrassa@buzzword-bingo.mit.edu", 22)
handler.cgi_directories = ["/web_scripts/Pursuit-Of-Happiness"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
