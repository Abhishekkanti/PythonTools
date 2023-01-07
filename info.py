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
print(f"[+] Domain : {domain}  and  IP : {ip}")


#whois Module
try:
    print("[+] Getting Whois info...")

#Creating a Instance of Whois
    py = whois.whois(domain)
    print("Whois info found\n")
    print("Name :",py.name)
    print("Registrant",py.registrant)
    print("Creation Date :",py.creation_date)
    print("Expiration Date :",py.expiration_date)
    print("Registrar :",py.registrar)
    print("Country:",py.registrant_country)
except:
    print("\n Failed to find Whois info...\n")
    pass

print("\n ***********************************\n")

#Dns module from dnspython
try:
     print("[+] Getting Whois info...")
     #dns = dns.resolver.resolve(domain,"NS")
   
     for i in dns.resolver.resolve(domain,'A'):
        print("[+] A record : ",str(i))
        
        
except:
    print("\nFailed to fetch Dns Records...\n")
    pass 