from router_sqlite import RouterMonitor, engine
from sqlalchemy.orm import sessionmaker
from snmpv2_getall_2023 import snmpv2_getall
import time
import sys
sys.path.extend(['//pythonProject/'])

# 创建数据库会话
Session = sessionmaker(bind=engine)
session = Session()

def insert_router_data(ip, community):
    try:
        # 获取路由器数据
        data = snmpv2_getall(ip, community)
        # from pprint import pprint
        # pprint(data)
        cpu_usage = data['cpu_usage']
        mem_usage = data['mem_usage']

        # 创建新记录
        new_record = RouterMonitor(
            device_ip=ip,
            cpu_usage_percent=cpu_usage,
            mem_use=mem_usage,
            mem_free=100 - mem_usage  # 假设总内存为100单位
        )

        # 添加到会话并提交
        session.add(new_record)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

if __name__ == "__main__":
    # router_ips = ["192.168.124.100", "192.168.124.200"]  # 替换为您的路由器IPs
    community_string = "tcpipro" # 替换为您的SNMP community字符串
    insert_router_data("192.168.124.100", community_string)
    insert_router_data("192.168.124.200", community_string)