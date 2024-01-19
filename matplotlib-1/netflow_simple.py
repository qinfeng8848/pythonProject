from netmiko import ConnectHandler
import matplotlib.pyplot as plt
from netflow_moban import mat_bing
# 路由器连接配置
router = {
    'device_type': 'cisco_ios',  # 假设路由器是Cisco IOS设备
    'host': '192.168.124.1',     # 路由器的IP地址
    'username': 'admin',  # SSH用户名
    'password': 'Cisc0123',  # SSH密码
    'port': 22,                   # SSH端口，默认为22
}

# 连接到路由器
net_connect = ConnectHandler(**router)

# 发送命令并获取NetFlow数据
output = net_connect.send_command('show flow monitor name qytang-monitor cache format table')

# 关闭连接
net_connect.disconnect()

# 解析输出并提取NetFlow数据
lines = output.splitlines()
app_names = []
byte_counts = []
for line in lines:
    if line.startswith('port') or line.startswith('layer7'):
        parts = line.split()
        app_names.append(parts[0] + '_' + parts[1])
        byte_counts.append(int(parts[-1]))
print(app_names)
print(byte_counts)

mat_bing(app_names, byte_counts, "Netflow流量比例")

