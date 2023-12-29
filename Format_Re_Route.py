import os
import re

ifconfig_result = os.popen("route -n").read()
print(ifconfig_result)

# Regular expression to match the lines containing gateways
gateway_regex = re.compile(r'^\S+\s+(\S+)\s+\S+\s+UG', re.MULTILINE)

# Find all matches
gateways = gateway_regex.findall(ifconfig_result)

print("网关为："+ gateways[0])
