#!/usr/bin/python3
import socket
from os import system

#Initialize network socket for listening
host = ''
port = 50007
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)


while True:
  client, address = s.accept()
  data = client.recv(size)
  datastr = data.decode('ascii')
  data_array = datastr.split(' ')
  cmd1=('echo "'+datastr+'" >/home/pi/python/FIFO_piservo')
  system(cmd1)
  client.close()

