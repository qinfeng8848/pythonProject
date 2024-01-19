#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# pip3 install matplotlib==3.5.3
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置黑体
plt.rcParams['font.family'] = 'sans-serif'

def mat_bar(name_list, count_list, title, x_label, y_label, color_list):
    # 柱状图美化, 参数说明
    plt.figure(figsize=(6, 6))

    # 柱状图绘制
    # plt.barh(name_list, count_list, height=0.5, color=color_list)

    # 柱状图绘制
    plt.bar(name_list, count_list, width=0.5, color=color_list)

    # 添加图形标签等
    plt.title(title)  # 标题
    plt.xlabel(x_label)  # X轴标签
    plt.ylabel(y_label)  # Y轴标签

    # 保存到图片
    # plt.savefig('result1.png')

    # 绘制图形
    plt.show()

if __name__ == "__main__":
    name_list = ['name1', 'name2', 'name3', 'name4']
    count_list = [123, 555, 354, 888]
    bar_name = '2023年销售额'
    x_label = '项目'
    y_label = '万元'
    colors = ['red', 'blue', 'green', 'yellow']
    mat_bar(name_list, count_list, bar_name, x_label, y_label, colors)
