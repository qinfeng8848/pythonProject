from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import os
# 数据库设置
db_file_path = f'{os.path.dirname(os.path.realpath(__file__))}/sqlAlchemy_sysLog_sqlite3.db'
engine = create_engine(f'sqlite:///{db_file_path}')
Base = automap_base()
Base.prepare(engine, reflect=True)

# 反射RouterMonitor表
RouterMonitor = Base.classes.router_monitor

# 查询特定路由器的数据
def query_router_data(device_ip):
    with Session(engine) as session:
        stmt = select(RouterMonitor).where(RouterMonitor.device_ip == device_ip)
        results = session.execute(stmt).all()
        return results
import datetime

# 过滤出最近60分钟的数据
def filter_last_60_minutes_data(timestamps, data):
    now = datetime.datetime.now()
    start_time = now - datetime.timedelta(minutes=60)

    filtered_timestamps = []
    filtered_data = []

    for i in range(len(timestamps)):
        if start_time <= timestamps[i] <= now:
            filtered_timestamps.append(timestamps[i])
            filtered_data.append(data[i])

    return filtered_timestamps, filtered_data

# 准备数据的函数
def query_and_prepare_data(device_ip):
    router_data = query_router_data(device_ip)
    cpu_usage = [data[0].cpu_usage_percent for data in router_data]
    mem_usage = [(data[0].mem_use / (data[0].mem_use + data[0].mem_free)) * 100 for data in router_data]
    timestamps = [data[0].record_datetime for data in router_data]
    return timestamps, cpu_usage, mem_usage

import datetime

# 绘制两条线的折线图，设置Y轴范围和间隔
def plot_two_lines_chart_with_fixed_y_axis(x_data1, y_data1, label1, x_data2, y_data2, label2, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(x_data1, y_data1, label=label1)
    plt.plot(x_data2, y_data2, label=label2)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))
    plt.gca().set_ylim([0, 100])  # 设置Y轴的范围从0到100
    plt.gca().set_yticks(range(0, 101, 10))  # 设置Y轴的间隔为10
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

# 查询并过滤数据
timestamps1, cpu_usage1, mem_usage1 = query_and_prepare_data('192.168.124.100')
timestamps2, cpu_usage2, mem_usage2 = query_and_prepare_data('192.168.124.200')

filtered_timestamps1, filtered_cpu_usage1 = filter_last_60_minutes_data(timestamps1, cpu_usage1)
filtered_timestamps2, filtered_cpu_usage2 = filter_last_60_minutes_data(timestamps2, cpu_usage2)
filtered_mem_usage1 = filter_last_60_minutes_data(timestamps1, mem_usage1)[1]
filtered_mem_usage2 = filter_last_60_minutes_data(timestamps2, mem_usage2)[1]

# 绘制CPU使用率图表
plot_two_lines_chart_with_fixed_y_axis(filtered_timestamps1, filtered_cpu_usage1, 'CPU Usage - 192.168.124.100',
                                   filtered_timestamps2, filtered_cpu_usage2, 'CPU Usage - 192.168.124.200',
                                   'CPU Usage Over Time (Last 60 minutes)', 'Time', 'CPU Usage (%)')

# 绘制内存使用率图表
plot_two_lines_chart_with_fixed_y_axis(filtered_timestamps1, filtered_mem_usage1, 'Memory Usage - 192.168.124.100',
                                   filtered_timestamps2, filtered_mem_usage2, 'Memory Usage - 192.168.124.200',
                                   'Memory Usage Over Time (Last 60 minutes)', 'Time', 'Memory Usage (%)')



