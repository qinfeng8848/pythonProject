#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# pip3 install matplotlib==3.5.3
from matplotlib import pyplot as plt

def mat_bing(name_list, count_list, bing_name):
    # 饼状图参数
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置黑体
    plt.rcParams['font.family'] = 'sans-serif'
    plt.figure(figsize=(6, 6))

    # 如果count_list的和小于100%，会自动加一个'空'部分
    # 如果name_list为空，可以自动标注为'空'
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=name_list,
                                      labeldistance=1.1,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)

    # labeldistance, 文字的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct, 饼里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow, 饼是否有阴影
    # startangle, 起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始
    # pctdistance, 与labeldistance相似，但是引出的线的长度

    # 改变文本的大小
    # 方法是把每一个文本遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 30
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title(bing_name)  # 标题
    plt.legend()

    # 保存到图片
    # plt.savefig('result1.png')

    # 显示图形
    plt.show()

if __name__ == "__main__":
    mat_bing(['项目1', '项目2', '项目3', '项目4'], [1000, 123, 444, 888], '项目统计')
