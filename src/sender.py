
#!/usr/bin/env python

import argparse
from scapy.all import *

# Import protocol
from Protocol import Protocol

# [TODO] Set source and destination IP address (Task 1.)
src_ip = '10.0.1.1'
dst_ip = '10.0.1.2'   # h2 IP address

# Set source and destination port
src_port = 1024
dst_port = 80

'''
Main function
'''
def main():
    # Define IP header
    ip = IP(src = src_ip, dst = dst_ip)

    # Define customized header 
    # [TODO] Add 'id' field in customized header here (Task 2.)
    #        And fill in your department
    student = Protocol(dept = 'cs',id='0716030')
    msg=['This lab is a little hard.','I am just kidding.','It is so damn difficult.']
    
    # [TODO] Fill in the message payload (Task 2.)
 
    
    # Send packets
    for i in range(0, len(msg)):
        # TCP connection - SYN / SYN-ACK
        tcp_syn = TCP(sport = src_port, dport = dst_port, flags = 'S', seq = 0)
        packet = ip / tcp_syn
        tcp_syn_ack = sr1(packet)
        print '[INFO] Send SYN and receive SYN-ACK'
        #tcp_syn_ack.show()

        # TCP connection - ACK
        ack = tcp_syn_ack.seq + 1
        tcp_ack = TCP(sport = src_port, dport = dst_port, flags = 'A', seq = 1, ack = ack)
        packet = ip / tcp_ack
        send(packet)
        print '[INFO] Send ACK'

        # Send packet with customized header
        ack = tcp_ack.seq + 1
        tcp = TCP(sport = src_port, dport = dst_port, flags = '', seq = 2, ack = ack)
        packet = ip / tcp / student
        send(packet)
        print '[INFO] Send packet with customized header'

        # Send packet with payload
        ack = tcp.seq + 1
        tcp = TCP(sport = src_port, dport = dst_port, flags = '', seq = 3, ack = ack)
        payload = Raw(msg[i])
        packet = ip / tcp / payload
        send(packet)
        print '[INFO] Send packet with payload'

if __name__ == '__main__':
    main()
