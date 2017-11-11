import socket;

s = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM);
s.bind(('127.0.0.1', 9999));
print('bind up to 9999 ...');
while True:
    data ,addr = s.recvfrom(1024);
    print('recvied from %s:%s' % addr);
    s.sendto(b'hello , %s!' % data,addr);