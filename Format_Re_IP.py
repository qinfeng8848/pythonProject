import os
import re
ifconfig_result = os.popen("ifconfig "+"en0").read()
print(ifconfig_result)

pattern_ip=r"inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
ipv4_add=re.findall(pattern_ip, ifconfig_result)[0]
print(ipv4_add)

pattern_broadcast=r"broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
broadcast = re.findall(pattern_broadcast, ifconfig_result)[0]
print(broadcast)

pattern_mac=r"ether\s+([0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2})"
mac = re.findall(pattern_mac, ifconfig_result)[0]
print(mac)

# 产生网关的IP地址
segments = broadcast.split('.')
ipv4_gw = '.'.join(segments[:-1])+'.254'
print(ipv4_gw)

# ping网关
ping_result = os.popen("ping "+ipv4_gw+" -c 1").read()
print(ping_result)

re_ping_result = re.search(r'\d+ bytes from.*time=', ping_result)

if re_ping_result:
    print("网关可达")
else:
    print("网关不可达")

