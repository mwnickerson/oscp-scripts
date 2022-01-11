#!/bin/python3
# a basic  ping sweep in python
# TODO: add ctrl +c to exit
# TODO: put hosts that are up into a document
# TODO: add multithreading to make it go faster



import ipaddress
import os

# Takes user input for target network
target_network = input("Enter Target network and subnet (10.0.0.0/24): ")

network = ipaddress.ip_network(f"{target_network}")

print(f"Running ping sweep on {target_network}...")

for i in network.hosts():
    response = os.system("ping %s -c 1 > /dev/null" %i)

    if response == 0:
        print("%s UP" %i)
    else:
        print("%s is down or blocking pings" %i)

print(f"[+] Ping sweep of {target_network} complete [+]")

