#!/bin/python3
# python script to enumerate a single user using smtp
# TODO: Ability to use a username list 
# TODO: Clean up responses to be easily read (User exists/User does not exist)


import socket 
import sys


print("SMTP User Enumeration")

# Take user input and assign variables
ip_address = input("Enter the ip of the smtp server: ")
username = input("Enter the user account to investigate: ")

# create a socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connect = s.connect((ip_address,25))

# Receive the banner
banner = s.recv(1024)

print(banner)

# Verify a user
s.send("VRFY " + f"username" + b'\r\n')
result = s.recv(1024)

print(result)

# close the connection
s.close()


