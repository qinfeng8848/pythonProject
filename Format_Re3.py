import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# Extract protocol
protocol = str1.split()[0]

# Define patterns
pattern_server = r"(?<!local)server\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})"
pattern_localserver = r"localserver\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})"
pattern_idle = r"idle\s+(\d+:\d+:\d+)"
pattern_bytes = r"bytes\s+(\d+)"
pattern_flags = r"flags\s+(\w+)"

# Extract data
server_ip = ', '.join(re.findall(pattern_server, str1))
localserver_ip = ', '.join(re.findall(pattern_localserver, str1))
idle_time = re.findall(pattern_idle, str1)[0]
bytes_used = ', '.join(re.findall(pattern_bytes, str1))
flags = ', '.join(re.findall(pattern_flags, str1))

# Convert idle time to formatted string
hours, minutes, seconds = map(int, idle_time.split(":"))
formatted_idle_time = f"{hours} 小时 {minutes:02d} 分钟 {seconds:02d} 秒"

# Print results
print(f'{"protocol":<20}: {protocol}')
print(f'{"server":<20}: {server_ip}')
print(f'{"localserver":<20}: {localserver_ip}')
print(f'{"idle":<20}: {formatted_idle_time}')
print(f'{"bytes":<20}: {bytes_used}')
print(f'{"flags":<20}: {flags}')
