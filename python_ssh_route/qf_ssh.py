
import paramiko

def qyt_ssh(hostname,username,password,comm):
    # 创建SSH客户端实例
    client = paramiko.SSHClient()
    # 自动接受未知的SSH密钥（注意安全风险）
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 连接到服务器
        client.connect(hostname=hostname, username=username, password=password)
        # 执行命令并获取输出
        stdin, stdout, stderr = client.exec_command(comm)
        output = stdout.read().decode()
        return output
    finally:
        # 无论是否出错都要关闭连接
        client.close()

if __name__ == '__main__':
    # hostname = '113.31.116.157'
    # username = 'root'
    # password = 'WBk-0TZ-vhK'
    # command = 'pwd'
    hostname = '192.168.123.1'
    username = 'admin'
    password = 'Cisc0123'
    comm = 'show ip int bri'
    output = qyt_ssh(hostname,username,password,comm)
    print(output)
