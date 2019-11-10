#!/usr/bin/env python

"""Code from Credle's 2020 capstone 

This code is from a sprint to control DJI Tello (non-edu) from a laptop.
He saved it as Laptop_Controlled_Flight_Code_Python.docx, which is kind 
of strange, so here it is as an actual usable Python code.

No comments on how this was written? Adapted from a Tello how to tutorial?
If so the link should be given. 
"""

import threading 
import socket
import sys
import time
import platform 

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

print ('Tello: command takeoff land flip forward back left right \r\n \
up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
        # print (version_init_num)
        if version_init_num == 3:
            msg = input("");
        elif version_init_num == 2:
            msg = raw_input("");

        if not msg:
            break 

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
