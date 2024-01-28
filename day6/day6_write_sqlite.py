#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# import sys
# sys.path.extend(['/PythonProject/'])
import sys
import os

# 添加 pythonProject 目录到 sys.path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_dir not in sys.path:
    sys.path.append(project_dir)


from sqlalchemy.orm import sessionmaker
from day6_create_db import InterfaceMonitor,engine
from day5.snmpv2_getall import snmpv2_getall




Session = sessionmaker(bind=engine)
session = Session()

ip_list = ['192.168.124.100','192.168.124.200']

def get_info_writedb(ip_list,recomnuity):
    router_info_list=[]
    for device_ip in ip_list:
            try:
                get_all=snmpv2_getall(device_ip,recomnuity)
                interface_list=get_all.get('if_list')
                for interface in interface_list:
                    interface_name=interface.get('name')
                    in_bytes=interface.get('in_bytes')
                    out_bytes=interface.get('out_bytes')

                    interface_info = InterfaceMonitor(device_ip=device_ip,
                                                      interface_name=interface_name,
                                                      in_bytes=in_bytes,
                                                      out_bytes=out_bytes,
                                                      )
                    # print(interface_info)
                    router_info_list.append(interface_info)
            except Exception as e:
                print(e)
    # print(router_info_list)
    session.add_all(router_info_list)
    session.commit()

if __name__=='__main__':
    community_string = "tcpipro"
    get_info_writedb(ip_list,community_string)