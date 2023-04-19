import sys
import whois
import requests
import shodan
import dns.resolver
import argparse


desp = "This is a Basic Information Gathering Tool."
ug = "python3 sys.argv[0] -d Domain [-s IP]"


#Created a Class Object of Argparse
parser= argparse.ArgumentParser(description=desp ,usage=ug)


#Accepting Argument from user
parser.add_argument("-d","--domain",help="Enter Domain Name for Footprinting..")

parser.add_argument("-s","--shodan",help="Enter the IP for Shodan Search..")

#Fetch Argument to the object
args = parser.parse_args()
domain = args.domain
ip = args.shodan

#printing Domain Name and Shodan
print(f"[+] Domain : {domain} and  IP : {ip}")
