from ipaddress import IPv4Address
import sys


try:
    addr = IPv4Address(input("Please input a vali Ip address:"))
    if addr < IPv4Address("127.0.0.1"):
        print("not the correct IP range")
    elif addr > IPv4Address("255.255.255.255"):
        print("not the correct IP range")
    else:
        print(addr)
except ValueError:
    print("Ip address is not valid")




