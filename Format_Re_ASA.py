import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

# 正则表达式，用于匹配源 IP、目标 IP、bytes 和 flags
pattern = r'TCP Student (\d+\.\d+\.\d+\.\d+):(\d+) Teacher (\d+\.\d+\.\d+\.\d+):(\d+),.*bytes (\d+), flags (\w+)'

# 创建字典以存储信息
asa_dict = {}
for conn in asa_conn.split('\n'):
    re_result = re.match(pattern, conn)
    if re_result:
        src_ip, src_port, dst_ip, dst_port, bytes_, flags = re_result.groups()
        key = (src_ip, src_port, dst_ip, dst_port)
        value = (bytes_, flags)
        asa_dict[key] = value

print("打印分析之后的字典！")
print(asa_dict)
src= 'src'
src_port = 'src_port'
dst = 'dst'
dst_port = 'dst_port'
bytes_name = 'bytes'
flags = 'flags'


print('\n格式化打印输出')
for key,value in asa_dict.items():
    print(f'{src:^10}:{key[0]:^16}|{src_port:^10}:{key[1]:^10}|{dst:^10}:{key[2]:^16}|{dst_port:^10}:{key[3]:^10}')
    print(f'{bytes_name:^10}:{value[0]:^16}|{flags:^10}:{value[1]:^10}')
    print('='*102)


