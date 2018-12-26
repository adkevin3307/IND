from scapy.all import IP, TCP, sr1, send, raw, sniff, sendp, Ether
import argparse

def check(pkts):
    global count, data
    for pkt in pkts:
        if 'Raw' in pkt:
            s = pkt['Raw'].load.decode('utf-8')
            if s[0: 15] == 'HTTP/1.1 200 OK':
                count += 1
            if count == 1:
                data.append(s)
            if count == 2:
                for i in range(len(data)):
                    print(data[i])

def ths():
    syn = ip / TCP(sport = sport, seq = 0, flags = 'S')
    syn_ack = sr1(syn)
    ack = ip / TCP(sport = sport, seq = syn_ack.ack, ack = syn_ack.seq + 1, flags = 'A')
    send(ack)

    def get_website():
        nonlocal syn_ack
        s = '' # destination website get packet

        get = ip / TCP(sport = sport, seq = syn_ack.ack, ack = syn_ack.seq + 1, flags = 'PA') / raw(s)
        send(get)
        sniff(filter = 'host {}' .format(dst), prn = check, count = 10)
    get_website()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'three handshake')

    parser.add_argument('-p', dest = 'port', type = int, help = 'source port')
    parser.add_argument('-d', dest = 'destination', type = str, help = 'destination ip')

    args = parser.parse_args()

    sport = args.port
    dst = args.destination
    ip = IP(dst = dst)
    data = []
    count = 0

    ths()