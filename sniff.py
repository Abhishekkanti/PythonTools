from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest,TCP

from colorama import Fore, Back, Style



#Colorama
red =  Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET

#getting packets send it to process_packet fun
def sniff_packet(iface):
    if iface:
        sniff(prn = process_packet,iface = iface, store = False)
    else:
        sniff(prn = process_packet, iface = iface)

#Capture and filtering of packets and displaying only TCP & IP packets
def process_packet(packet):
    if packet.haslayer(TCP):
        src = packet[IP].src
        dst = packet[IP].dst
        
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"{green}[+] src:{src} IP using src port :{src_port} to connect to dst:{dst} IP on dst port:{dst_port} {reset}")
        
print(sniff_packet("eth0"))
