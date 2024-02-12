#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# pip3 install numpy
from sqlalchemy.orm import sessionmaker
from day6.day6_create_db import InterfaceMonitor, engine
import numpy as np
from day6.tools.mat_line import mat_Line

from random import choice
from pprint import pprint
from datetime import datetime, timedelta

Session = sessionmaker(bind=engine)
session = Session()

# 这是一个小时以内的数据获取
now = datetime.now()
one_hours_before = now - timedelta(hours=1)

# 随机颜色列表，随机选择
color_List = ['red', 'blue', 'green', 'yellow']

# 随机线型列表，随机选择
line_style_list = ['solid', 'dashed']

# 获取到唯一的device_ip和interface_name的组合
router_if_infos = (session.query(InterfaceMonitor.device_ip,
                                 InterfaceMonitor.interface_name).group_by(InterfaceMonitor.device_ip,
                                                                           InterfaceMonitor.interface_name).all())

# print(router_if_infos)
# [('10.1.1.1', 'GigabitEthernet1'), ('10.1.1.2', 'GigabitEthernet1')]

# 入接口速率的列表
in_speed_lines_list = []

# 出接口速率的列表
out_speed_lines_list = []

# 对应关系进行计数
count = 0

for device_ip, interface_name in router_if_infos:
    # 过滤最近一个小时，符合device_ip和interface_name组合的全部记录数据
    device_if_info = session.query(InterfaceMonitor). \
        filter(InterfaceMonitor.device_ip == device_ip,
               InterfaceMonitor.interface_name == interface_name). \
        filter(InterfaceMonitor.record_datetime >= one_hours_before)

    # 获取入口字节的列表
    in_bytes_list = []
    # 获取出口字节的列表
    out_bytes_list = []
    # 获取记录时间的列表
    record_time_list = []

    # 从获取的记录数据中提取出来，形成独立的列表用于后续计算
    for device_if in device_if_info:
        in_bytes_list.append(device_if.in_bytes)
        out_bytes_list.append(device_if.out_bytes)
        record_time_list.append(device_if.record_datetime)
    # print(in_bytes_list)
    # print(out_bytes_list)
    # print(record_time_list)

    # 使用numpy库计算两个数据之间的差值
    diff_in_bytes_List = list(np.diff(in_bytes_list))
    diff_out_bytes_List = list(np.diff(out_bytes_list))
    diff_record_time_List = [x.seconds for x in np.diff(record_time_list)]

    # 计算速率
    # 8 个字节等于 1 个字bit
    # 1000 个字Kb
    # x[1] 单位秒
    in_speed_List = list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2),
                             zip(diff_in_bytes_List, diff_record_time_List)))
    out_speed_List = list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2),
                              zip(diff_out_bytes_List, diff_record_time_List)))

    # 切掉第一个时间记录点
    record_time_list = record_time_list[1:]
    # 判断是否有一个时间点速率为零，如果为零的话就剔除掉
    clean_record_time_list = []
    clean_in_speed_list = []
    clean_out_speed_list = []

    for r, i, o in zip(record_time_list, in_speed_List, out_speed_List):
        if i > 0 and o > 0:  # 如果入口和出口速率都不为0，写入临时列表
            clean_record_time_list.append(r)
            clean_in_speed_list.append(i)
            clean_out_speed_list.append(o)

    # 写入速度线的Lines_list
    in_speed_lines_list.append([clean_record_time_list,
                                clean_in_speed_list,
                                line_style_list[count % len(line_style_list)],
                                color_List[count % len(color_List)],
                                f"RX:{device_ip}:{interface_name}"])
    out_speed_lines_list.append([clean_record_time_list,
                                 clean_out_speed_list,
                                 line_style_list[count % len(line_style_list)],
                                 color_List[count % len(color_List)],
                                 f"TX:{device_ip}:{interface_name}"])
    count += 1

# 画出线条图表
mat_Line(in_speed_lines_list, '入口速率', '记录时间', 'kbps')
mat_Line(out_speed_lines_list, '出口速率', '记录时间', 'kbps')
