import random

# 创建一个空列表用于存储四个数字
ipv4_parts = []

# 循环四次，每次生成一个0到255之间的随机数
for _ in range(4):
    part = random.randint(0, 255)  # 生成随机数
    ipv4_parts.append(str(part))  # 将随机数转换为字符串并添加到列表中

# 使用点号 (.) 将四个部分连接起来，形成一个完整的IPv4地址
random_ipv4_address = '.'.join(ipv4_parts)

# 打印一个随机的IPv4地址
print(random_ipv4_address)

