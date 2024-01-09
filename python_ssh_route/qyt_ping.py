from kamene.all import IP, ICMP, sr1, conf
class KamenePing:
    def __init__(self, target_ip, src_ip=None):
        self.target_ip = target_ip
        self.srcip = src_ip if src_ip else conf.route.route("0.0.0.0")[1]  # 如果没有提供源IP，则使用默认值
        self.length = 56  # 默认ICMP负载长度为56字节
        self.timeout = 2  # 响应超时时间
    def one(self):
        """发送一个ICMP Echo请求以检查目标的可达性"""
        packet = IP(dst=self.target_ip, src=self.srcip) / ICMP() / ("X" * self.length)
        reply = sr1(packet, timeout=self.timeout, verbose=0)
        if reply:
            print(f"{self.target_ip} 可达")
            return True
        else:
            print(f"{self.target_ip} 不可达")
            return False
    def ping(self):
        """模拟标准ping程序发送五个ICMP Echo请求包"""
        results = ""
        for _ in range(5):  # 发送五个包
            packet = IP(dst=self.target_ip, src=self.srcip) / ICMP() / ("X" * self.length)
            reply = sr1(packet, timeout=self.timeout, verbose=0)
            if reply:
                results += "!"
            else:
                results += "."
        print(results)
        return results
    def __str__(self):
        """自定义打印输出"""
        srcip_str = f"srcip: {self.srcip}, " if self.srcip != conf.route.route("0.0.0.0")[1] else ""
        return f"<{self.__class__.__name__} => {srcip_str}dstip: {self.target_ip}, size: {self.length}>"

class NewPing(KamenePing):
    def ping(self):
        """模拟标准ping程序发送五个ICMP Echo请求包，'+'表示通，'?'表示不通"""
        results = ""
        for _ in range(5):  # 发送五个包
            packet = IP(dst=self.target_ip, src=self.srcip)/ICMP()/("X"*self.length)
            reply = sr1(packet, timeout=self.timeout, verbose=0)
            if reply:
                results += "+"
            else:
                results += "?"
        print(results)
        return results

if __name__ == '__main__':
    ping=KamenePing('8.8.8.8')
    total_len=70
    def print_new(word,s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2),word,s*int((70-len(word))/2)))

    print_new('print class')
    print(ping)
    print_new('print one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload lenth')
    ping.length=200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '192.168.1.123'
    print(ping)
    ping.ping()
    print_new('new class NewPing','=')
    newPing=NewPing('8.8.8.8')
    newPing.length =300
    print(newPing)
    newPing.ping()