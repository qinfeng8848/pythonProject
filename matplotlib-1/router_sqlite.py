#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import datetime
import os

tzutc_8 = datetime.timezone(datetime.timedelta(hours=8))  # 设置时区为东八区

# os.path.dirname(os.path.realpath(__file__)) 当前文件目录
# 当前数据库文件的位置，与当前文件同目录下
db_file_name = f'{os.path.dirname(os.path.realpath(__file__))}/sqlAlchemy_sysLog_sqlite3.db'

engine = create_engine(f'sqlite:///{db_file_name}?check_same_thread=False')

Base = declarative_base()

# 路由器监控数据表格，记录CPU、内存
class RouterMonitor(Base):
    __tablename__ = 'router_monitor'

    id = Column(Integer, primary_key=True)  # 唯一ID，自增
    device_ip = Column(String(64), nullable=False)  # 设备IP地址
    cpu_usage_percent = Column(Integer, nullable=False)  # CPU利用率
    mem_use = Column(Integer, nullable=False)  # 使用内存字节数
    mem_free = Column(Integer, nullable=False)  # 剩余内存字节数
    record_datetime = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return f"<{self.__class__.__name__}(Router: {self.device_ip} " \
               f" Datetime: {self.record_datetime} " \
               f" CPU_Usage_Percent: {self.cpu_usage_percent} " \
               f" MEM Use: {self.mem_use} " \
               f" MEM Free: {self.mem_free})>"

if __name__ == '__main__':
    # checkfirst=True, 表示在创建表格前会检查这个表格是否存在，如果不存在则创建新的表格，此参数默认就是True
    Base.metadata.create_all(engine, checkfirst=True)
