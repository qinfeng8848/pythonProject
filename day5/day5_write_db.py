#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
sys.path.extend(['/PythonProject/'])

from snmpv2_getall import snmpv2_getall
import datetime
from influxdb import InfluxDBClient

ip_list = ['192.168.124.100', '192.168.124.200']

snmp_community = 'tcpipro'

influxdb_host_ip='192.168.192.128'

client = InfluxDBClient(influxdb_host_ip,8086,'qytdbuser','Cisc0123','qytdb')

recode_list=[]

for router_ip in ip_list:
    getall_result = snmpv2_getall(router_ip,snmp_community)
    current_time = datetime.datetime.utcnow().isoformat('T')

    cpu_mem_body = {
        "measurement": "router_monitor",
        "time": current_time,
        "tags": {
            "device_ip": getall_result.get('ip'),
            "device_type": "IOS-XE"
        },
        "fields": {
            "cpu_usage": getall_result.get('cpu_usage'),
            "mem_usage": getall_result.get('mem_usage'),
            "mem_free": getall_result.get('mem_free'),
        },
    }
    recode_list.append(cpu_mem_body)

client.write_points(recode_list)