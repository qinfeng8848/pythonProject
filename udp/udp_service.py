import socket
import sys
import struct
import hashlib
import pickle

# 绑定到本机的6666端口
address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器端开始监听！')

try:
    while True:
        # 接收客户端的数据
        recv_source_data = s.recvfrom(512)
        rdata, addr = recv_source_data

        # 解析头部信息，头部信息包括版本号、类型、序列号和长度
        header = rdata[:16]  # 根据图片中的展示，头部长度为14字节
        version, pkt_type, seq_id, length = struct.unpack('!HHIQ', header)

        # 分离数据和MD5校验值
        data = rdata[16:16+length]
        md5_recv = rdata[16+length:]

        # 计算数据的MD5值
        md5_value = hashlib.md5(data).digest()

        # 对比接收到的MD5值和计算的MD5值
        if md5_recv == md5_value:
            # 如果MD5匹配，打印出数据内容
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据源自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))
        else:
            # 如果MD5不匹配，打印错误信息
            print('MD5校验错误！')

except KeyboardInterrupt:
    # 如果运行时按下Ctrl+C，则退出程序
    print('服务器关闭。')
    sys.exit()
finally:
    # 最后关闭套接字
    s.close()
