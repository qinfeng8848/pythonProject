#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Integer, DateTime, BigInteger, Boolean
import datetime
import os

tzutc_8 = datetime.timezone(datetime.timedelta(hours=8))

db_file_name = f'{os.path.dirname(os.path.realpath(__file__))}/sqlAlchemy_sysLog_sqlite3.db'

engine = create_engine(f'sqlite:///{db_file_name}?check_same_thread=False')

Base = declarative_base()

class InterfaceMonitor(Base):
    __tablename__ = 'interface_monitor'

    id = Column(Integer, primary_key=True)
    device_ip = Column(String(64), nullable=False)
    interface_name = Column(String(64), nullable=False)
    in_bytes = Column(Integer, nullable=False)
    out_bytes = Column(Integer, nullable=False)
    record_datetime = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)
    def __repr__(self):
        return f"{self.__class__.__name__}(路由器IP:{self.device_ip}" \
               f"|时间：{self.record_datetime}" \
               f"|接口名称：{self.interface_name}" \
               f"|入向字节数:{self.in_bytes}" \
               f"|出向字节数:{self.out_bytes}）"

Base.metadata.create_all(engine, checkfirst=True)

if __name__ == '__main__':
    # 如果存在老数据库就删除
    if os.path.exists(db_file_name):
        os.remove(db_file_name)
