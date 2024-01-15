import time

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sql_routers import Base, RouterConfig  # 假设sql_routers.py包含ORM定义
from ssh_routers import get_show_run  # 假设ssh_routers.py包含连接网络设备的函数

# 数据库配置
DATABASE_URI = 'sqlite:///sqlalchemy_sqlite3.db'
engine = create_engine(DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
# 确保数据库表存在
Base.metadata.create_all(engine)

def main():
    last_hash = None
    session = Session()

    while True:
        # 获取网络设备的配置和HASH值
        config, hash_val = get_show_run("192.168.123.1", "admin", "Cisc0123")
        # 将获取的配置和HASH值写入数据库
        new_config = RouterConfig(router_ip="192.168.123.1", router_config=config, config_hash=hash_val)
        session.add(new_config)
        session.commit()

        # 比较最近两次的HASH值
        if last_hash is not None:
            if last_hash == hash_val:
                print(f'本次采集的HASH值: {hash_val}')
            else:
                print('配置发生变化')
                print(f'上一次HASH值: {last_hash}')
                print(f'本次HASH值: {hash_val}')
        else:
            print(f'首次采集的HASH值: {hash_val}')

        # 更新上一次的HASH值
        last_hash = hash_val

        # 等待5秒
        time.sleep(5)


if __name__ == "__main__":
    main()
