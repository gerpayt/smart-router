#!/usr/bin/python
# coding:utf8
print "Content-type: text/html"
print
import cgi,socket,sys
import commands
try:
    form = cgi.FieldStorage()
    content = form.getvalue('saywhat')
except:
    content = ''

if content:
    content = content.replace(' ','_')
    content = content.replace('\t','_')
    content = content.replace('\r','_')
    content = content.replace('\n','_')
    #commands.getstatusoutput('say 1')
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect("/tmp/say.sock")
        sock.send(content)
        print sock.recv(1024)
        sock.close()
    except:
        print "Error",sys.exc_type

print "<html>"
print "<head><title>路由器说话</title><meta charset='UTF-8'></head>"
print "<body>"
print "said:", content
print "<form method='post' action=''>"
print "    <input type='text' name='saywhat' />"
print "    <input type='submit' value='SAY' />"
print "</form>"
print "</body>"
print "</html>"

