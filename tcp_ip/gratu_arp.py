from kamene.all import ARP, Ether, sendp

def send_gratuitous_arp(source_ip, source_mac, interface='ens160'):
    # 创建以太网帧
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # 创建ARP数据包
    arp = ARP(pdst=source_ip, psrc=source_ip, hwsrc=source_mac, op=2)

    # 组合以太网帧和ARP请求
    packet = ether / arp

    # 发送数据包
    sendp(packet, iface=interface)

# 使用具体的IP和MAC地址调用函数
send_gratuitous_arp("192.168.123.1", "00:11:22:33:44:55")
