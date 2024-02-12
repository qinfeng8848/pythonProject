#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
import os
# sys.path.extend(['/PythonProject/'])
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_dir not in sys.path:
    sys.path.append(project_dir)

from day5.snmpv2_getall import snmpv2_getall
import datetime
from influxdb import InfluxDBClient

ip_list = ['192.168.124.100', '192.168.124.200']

snmp_community = 'tcpipro'

influxdb_host_ip='192.168.192.128'

client = InfluxDBClient(influxdb_host_ip,8086,'qytdbuser','Cisc0123','qytdb')

recode_list = []

for router_ip in ip_list:
    getall_result = snmpv2_getall(router_ip, snmp_community)
    # current_time = datetime.datetime.utcnow().isoformat('T')
    # interface_list = getall_result.get("if_list")
    # ----------------------写入接口进出数据------------------------
    current_time = datetime.datetime.utcnow().isoformat("T")
    if_bytes_body = []

    for if_info in getall_result.get('if_list'):
        if if_info.get('in_bytes') and if_info.get('out_bytes'):
            if_info_dict = {
                "measurement": "if_monitor",
                "time": current_time,
                "tags": {
                    "device_ip": getall_result.get('ip'),
                    "device_type": "IOS-XE",
                    "interface_name": if_info.get('name')
                },
                "fields": {
                    "in_bytes": if_info.get('in_bytes'),
                    "out_bytes": if_info.get('out_bytes'),
                },
            }
            if_bytes_body.append(if_info_dict)
    print(if_bytes_body)
    client.write_points(if_bytes_body)
