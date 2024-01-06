import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import IP, ICMP, sr1
def qyt_ping(host):
    # 创建一个 IP 层和 ICMP 层
    ip = IP(dst=host)
    icmp = ICMP()
    # 发送数据包并接收回复
    reply = sr1(ip/icmp, timeout=1, verbose=0)
    if reply:
        # print(f"Reply from {host}: bytes={len(reply)} time={reply.time}ms")
        return reply
    else:
        # print(f" 没有数据发送No reply from {host}")
        return None

if __name__ == "__main__":
   qyt_ping("192.168.123.1")