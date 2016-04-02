import sys
from scapy.all import sr1, IP, TCP


def main():
    """
    To prevent the kernel sending RST immediately when it gets SYN,ACK from remote host, add this iptables rule:
    iptables -A OUTPUT -p tcp --tcp-flags RST RST -s <source_ip> -j DROP
    """

    destination_host = sys.argv[1]
    source_port = int(sys.argv[2])

    synack = sr1(IP(dst=destination_host) / TCP(sport=source_port, dport=2553, flags='S'), timeout=1)
    if not synack:
        print('No response to syn.')
        sys.exit(0)

    synack.display()

    packet = sr1(IP(dst=destination_host) / TCP(sport=synack.dport, dport=synack.sport, flags='R', seq=synack.ack + 1, ack=synack.seq + 1), timeout=1, retry=0)
    if packet:
        print('Response to RST:')
        packet.show()
    else:
        print('No response to RST.')
