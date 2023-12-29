import os
import re
ifconfig_result = os.popen("ifconfig "+"en0").read()
# print(ifconfig_result)

pattern_ip=r"inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
ipv4_add=re.findall(pattern_ip, ifconfig_result)[0]
print(f'{"ipv4_add":<10}:{ipv4_add}')

# linux
# pattern_netmask=r"netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
# netmask1=re.findall(pattern_netmask, ifconfig_result)[0]
# print(f'{"netmask":<10}:{netmask1}')

# mac
pattern_netmask=r"netmask\s+(0x[0-9a-fA-F]{8})"
netmask=re.findall(pattern_netmask, ifconfig_result)[0]
# Remove the '0x' prefix and convert to binary
binary_netmask = bin(int(netmask, 16))[2:].zfill(32)
# Split into 8-bit chunks and convert each to decimal
dot_decimal_netmask = '.'.join(str(int(binary_netmask[i:i+8], 2)) for i in range(0, 32, 8))
print(f'{"netmask":<10}:{dot_decimal_netmask}')


pattern_broadcast=r"broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
broadcast = re.findall(pattern_broadcast, ifconfig_result)[0]
print(f'{"broadcast":<10}:{broadcast}')

pattern_mac=r"ether\s+([0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2})"
mac = re.findall(pattern_mac, ifconfig_result)[0]
print(f'{"mac":<10}:{mac}')

# 产生网关的IP地址
segments = broadcast.split('.')
ipv4_gw = '.'.join(segments[:-1])+'.254'
print('\n我们假设网关IP地址是为最后一位为254，因此网关IP地址为：'+ ipv4_gw +'\n')
# ping网关
ping_result = os.popen("ping "+ipv4_gw+" -c 1").read()
# print(ping_result)

re_ping_result = re.search(r'\d+ bytes from.*time=', ping_result)
if re_ping_result:
    print("网关可达")
else:
    print("网关不可达")

