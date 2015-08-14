import socket 
import sys
 
host = 'www.aplu.ch';
port = 80;
remote_ip = socket.gethostbyname(host)

# Phase 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip , port))
print "Socket Connected to " + host + " on ip " + remote_ip

# Phase 2
request = "GET /home/welcomex.html HTTP/1.1\r\nHost: " + host + "\r\n\r\n" 
s.sendall(request)

# Phase 4
reply = s.recv(4096)
print "\nReply:\n"
print reply
