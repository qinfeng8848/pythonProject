#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 安装matplotlib库的特定版本
from matplotlib import pyplot as plt

# 定义一个函数，用于生成饼图
def mat_bing(name_list, count_list, bing_name):
    # 设置中文字体，以便饼图可以显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建一个图表对象，并设置图表的大小
    plt.figure(figsize=(6, 6))

    # 调用plt.pie()函数生成饼图，输入参数为计数列表和名称列表
    # 并设置标签的距离、自动百分比显示格式、阴影效果、起始角度和占比数字的距离
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=name_list,
                                      labeldistance=1.2,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)

    # 自定义饼图的样式设置，包括标签距离、自动百分比、阴影、起始角度和占比数字的距离
    for t in l_text:
        t.set_size(30)
    for t in p_text:
        t.set_size(30)

    # 设置坐标轴比例相等，确保饼图为圆形
    plt.axis('equal')
    # 设置图表标题
    plt.title(bing_name)
    # 显示图例
    plt.legend()

    # 显示图表
    plt.show()

# 这是主程序入口，如果直接运行这个文件，会调用mat_bing函数生成饼图
if __name__ == '__main__':
    # 调用函数，传入名称列表、计数列表和饼图的名称
    mat_bing(['名称1', '名称2', '名称3'], [1000, 123, 444], '我的测试饼图')
