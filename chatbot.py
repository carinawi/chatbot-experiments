import re
from socket import socket

parse_regex = re.compile(':[^ ]* (\w+) ([^ ]+) ?(.*)')
def parse(string):
    m = parse_regex.match(string)
    return (m.group(1), m.group(2), m.group(3))

s1 = socket()
s1.connect(('irc.freenode.net', 8001))

s1.send('NICK therealr2d2\n')
s1.send('USER carina 8 * :Carina\n')


def readlines(sock, recv_buffer=4096, delim='\n'):
    buffer = ''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buffer += data

        while buffer.find(delim) != -1:
            line, buffer = buffer.split('\n', 1)
            yield line
    return


for line in readlines(s1):
    status, recipient, rest = parse(line)
    print (status, recipient, rest)
    pp = re.compile('PING :?(.*)')
    mm = pp.match(line)

    if status == '001':
        s1.send('JOIN #dasistdummundeintest\n')

    if status == 'PRIVMSG':
        s1.send('PRIVMSG #dasistdummundeintest :' + rest)

    if mm:
        s1.send('PONG ' + mm(1))
