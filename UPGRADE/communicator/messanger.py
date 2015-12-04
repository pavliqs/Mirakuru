import socket
import time

# send socket
def mSend(Sock, cmd, end="[ENDOFMESSAGE]"):
    try:
        Sock.sendall((cmd + end).encode('utf-8'))
        return True
    except socket.error:
        return False

# recieve socket
def mReceive(Sock, end="[ENDOFMESSAGE]"):
    data = ""
    try:
        l = Sock.recv(1024)
        while l:
            time.sleep(0.1)
            data += l
            if data.endswith(end):
                break
            else:
                l = Sock.recv(1024)
    except socket.timeout:
        pass
    return data[:-len(end)].decode('utf-8')