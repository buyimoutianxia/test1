from wsgiref.simple_server import make_server;
from First import application;

httpd = make_server('', 8000, application)
print('Servering http on port 8000');
httpd.serve_forever();