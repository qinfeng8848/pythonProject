#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# pip3 install matplotlib==3.5.3
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
# plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'

def mat_Line(lines_list, title, x_label, y_label):
    # 画多个折线对比图, %d, %m
    fig = plt.figure(figsize=(6, 6))

    # 一块画布, 每画一图, 就是一块
    ax = fig.add_subplot(111)

    # 处理x轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))  # 设置时间格式,显示为日期
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间格式,显示为小时和分钟

    # # 处理y轴百分比格式
    # import matplotlib.ticker as mtick
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f%%'))
    #
    # # Y轴的取值范围
    # ax.set_ylim(ymin=0, ymax=100)

    # 添加图表和轴标签
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # 画出所有传进来的折线并赋予标签名
    for x_list, y_list, line_style, color, line_name in lines_list:
        # ------每一条线将使用的属性
        # x_list     : X轴数据集
        # y_list     : Y轴数据集
        # line_style : 线条类型 (solid:实线, dashed:虚线)
        # color      : 线条颜色
        # line_name  : 线条名称
        ax.plot(x_list, y_list, linestyle=line_style, color=color, label=line_name)

    # 显示图例的位置
    ax.legend(loc='upper left')

    # 保存到图片
    # plt.savefig('result1.png')

    # 显示图形
    plt.show()

if __name__ == "__main__":
    from datetime import datetime, timedelta
    from random import random, choice

    # 测试用:生成的折线数
    line_no = 2

    # 测试用:生成的每条折线数据点数
    data_points_count = 10

    # 折线的颜色列表, 随机选择
    color_list = ['red', 'blue', 'green', 'yellow']

    # 折线的类型列表, 随机选择
    line_style_list = ['solid', 'dashed']

    # 当前时间, 选择为系统当前时间作为终点
    now = datetime.now()

    # 最终的折线数据及线条属性列表
    lines_list = []

    # 随机产生多组数据并添加到数据集
    for l in range(line_no):
        # 生成线的名称
        line_name = f"line{l+1}"
        # 生成线的X轴数据集列表
        line_x_list = []
        # 生成线的Y轴数据集列表
        line_y_list = []

        # 互不一致的数据集创建列表
        for d in range(data_points_count):
            # 互不X轴的时间点, 在now基础之上加分钟数
            line_x_list.append(now + timedelta(minutes=d))
            # 互不Y轴的百分比, 随机在1-100之间生成一个整数
            line_y_list.append(random() * 100)

        # 把每一条线的数据集，加入X_Y_list
        lines_list.append([line_x_list, line_y_list, choice(line_style_list), choice(color_list), line_name])

    # 绘制折线图
    mat_Line(lines_list, 'CPU利用率', '时间', '%')
