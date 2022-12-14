#웹페이지 사용
from socket import *
import threading
import time


def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))
        
        if sendData.encode('utf-8') == "":break
        

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))
        if recvData.decode('utf-8') == "":
            break

serverip = '192.168.29.238'
# serverip = '172.0.0.1'
port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((serverip, port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass