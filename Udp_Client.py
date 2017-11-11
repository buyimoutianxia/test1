import socket;

s = socket.socket(family=socket.AF_INET , type =socket.SOCK_DGRAM);
for data in [b'Mickle', b'Tracy',b'Sarah']:
    s.sendto(data , ('127.0.0.1',9999));
    print(s.recv(1024).decode('utf-8'));
s.close();