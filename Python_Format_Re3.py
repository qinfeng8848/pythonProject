import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

first_word = str1.split()[0]
print(f'{"protocol":<20}'+':'+first_word)

pattern_server = r"(?<!local)server\b\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})"

ip_addresses = re.findall(pattern_server, str1)
print(f'{"server":<20}' +':' +', '.join(ip_addresses) )

pattern_localserver = r"localserver\b\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})"
ip_addresses = re.findall(pattern_localserver, str1)
print(f'{"localserver":<20}'  +':' + ', '.join(ip_addresses) )

pattern_idle=r"idle\s+(\d+:\d+:\d+)"
idle_idle = re.findall(pattern_idle, str1)
hours, minutes, seconds = map(int, idle_idle[0].split(":"))
formatted_idle_time_f = f"{hours} 小时 {minutes:02d} 分钟 {seconds:02d} 秒"
print(f'{"idel":<20}'  +':' + formatted_idle_time_f )

pattern_bytes=r"bytes\s+(\d+)"
byte_byte = re.findall(pattern_bytes, str1)
print(f'{"bytes":<20}'  +':' + ', '.join(byte_byte) )

pattern_flags=r"flags\s+(\w+)"
flag_flag = re.findall(pattern_flags, str1)
print(f'{"flags":<20}'  +':' + ', '.join(flag_flag) )