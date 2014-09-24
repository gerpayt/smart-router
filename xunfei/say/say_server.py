#!/usr/bin/python
from daemon import daemonize
import socket,os,commands,stat
path = os.path.dirname(__file__)

def main():
    sockfile="/tmp/say.sock"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    if os.path.exists(sockfile):
        os.unlink(sockfile)
    sock.bind(sockfile)
    sock.listen(5)
    os.chmod(sockfile,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
    while True:
        connection,address = sock.accept()
        content = connection.recv(1024)
        if content:
            print 'say "%s"' % content
            content = content.replace('"', '\\"')
            (rc,rs) = commands.getstatusoutput('cd "' + path + '"; ./say-stdout "' + content +'" | mplayer -cache 256 - > /dev/null 2>&1 ')
            connection.send(rs)
        connection.close()

if __name__ == "__main__": 
    daemonize()
    main()

