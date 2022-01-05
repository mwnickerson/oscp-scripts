#!/bin/python3
# Python3 script to find NS for a domain and attempt a zone transfer
import dns.zone as dz
import dns.resolver as dr
import dns.query as dq


ns_servers = []
target_domain = input("Enter domain to attempt zone transfer on: ")

def dns_zone_transfer(domain):
    ns_answer = dr.resolve(domain, "NS")
    for ns in ns_answer:
        print(f"[*] Found Name Server: {ns}")
        ip_answer = dr.resolve(ns.target, "A")
        for ip in ip_answer:
            print(f"[*] IP for {ns} is {ip}")
            try:
                zone = dz.from_xfr(dq.xfr(str(ip), domain))
                for host in zone:
                    print(f"[*] Found Host: {host}")
            except Exception as e:
                print(f"[X] NS {ns} refused zone transfer!")
                continue

dns_zone_transfer(target_domain)

