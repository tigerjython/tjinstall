import socket 
import sys
from ch.aplu.util import HtmlPane

host = "www.aplu.ch";
port = 80;
remote_ip = socket.gethostbyname(host)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((remote_ip , port))
request = "GET /home/welcomex.html HTTP/1.1\r\nHost: " + host + "\r\n\r\n" 
s.sendall(request)
reply = s.recv(4096)

index = reply.find("<html")
html = reply[index:]

pane = HtmlPane()
pane.insertText(html)
