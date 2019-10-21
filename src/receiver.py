#!/usr/bin/env python

from random import *
from scapy.all import *
from time import *

# [TODO] Set source IP address (Task 3.)


src_ip = '10.0.1.1' # h1 IP address

# Store the receiving message
id = ''
received = []

'''
Handle the received packet
'''
def packetHandler(packet):
    global id, received

    # Show the receiving packet
    packet.show()

    # Filtering packet
    if TCP in packet and packet['IP'].src == src_ip:
        if packet['TCP'].seq == 2: 
            print '[INFO] Receive packet with customized protocol'
            id = str(packet['Raw'])[-7:]
        elif packet['TCP'].seq == 3: 
            print '[INFO] Receive packet with payload message'
            received.append(packet['Raw'])

'''
Main function
'''
def main():
    # Sniff the packets from specific source IP
    print '[INFO] Start to sniff'
    filter_msg = "ip src " + src_ip + " and tcp"
    packets = sniff(filter=filter_msg, prn = lambda x: packetHandler(x))

    # Dump the sniffed packet into PCAP file
    print '[INFO] Stop sniffing ... Write into PCAP file'
    filename = './out/lab1_' + id + '.pcap'
    wrpcap(filename, packets)
    
    # Finishing receiving in a duration
    print '[INFO] Finish receiving packets in a duration'

if __name__ == '__main__':
    main()
