import re

str1="Port-channel1.189    192.168.189.254 YES  CONFIG  up "
print('-'*80)

first_word = str1.split()[0]
print('接口      :'+ first_word)
# 匹配IP地址
pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ip_addresses = re.findall(pattern, str1)
print('ip地址    :' + ', '.join(ip_addresses))

last_word = str1.split()[-1]
print('状态      :'+ last_word)



