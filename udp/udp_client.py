import socket
import struct
import hashlib
import pickle


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    version = 1
    pkt_type = 1
    seq_id = 1  # 这个序列号在发送多个数据包时应该递增

    for x in data_list:
        # 序列化数据
        send_data = pickle.dumps(x)
        # 数据长度
        length = len(send_data)
        # 构造协议头部
        header = struct.pack('!HHIQ', version, pkt_type, seq_id, length)
        # 计算数据的MD5值
        md5_value = hashlib.md5(send_data).digest()
        # 构造完整的数据包
        packet = header + send_data + md5_value
        # 发送数据包
        s.sendto(packet, address)
        # 序列号递增
        seq_id += 1

    # 关闭套接字
    s.close()


if __name__ == "__main__":
    from datetime import datetime

    # 测试数据
    user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}, {'datetime': datetime.now()}]
    udp_send_data('192.168.123.219', 6666, user_data)
