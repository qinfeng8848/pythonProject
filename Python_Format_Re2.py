import re

vlanid1='VLAN ID'
mac1='MAC'
type1='Type'
interface1='Interface'
str1="166 54a2.74f7.0326 DYNAMIC Gi1/0/1"

first_word = str1.split()[0]
print(f'{vlanid1:<15}: {first_word:}')

mac_pattern = r'([0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4})'
mac_addresses = re.findall(mac_pattern, str1)
mac_addresses_str = '\n'.join(mac_addresses)
print(f'{mac1:<15}: {mac_addresses_str:}')

type_word = str1.split()[2]
print(f'{type1:<15}: {type_word:}')

inter_word = str1.split()[3]
print(f'{interface1:<15}: {inter_word:}')