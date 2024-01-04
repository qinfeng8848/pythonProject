import os
import re
import paramiko

def ssh_get_route(hostname, username, password, command='route -n'):
    """
    连接到SSH服务器并执行命令。

    :param hostname: SSH服务器的主机名或IP地址
    :param username: SSH用户名
    :param password: SSH密码
    :param command: 要在远程服务器上执行的命令
    :param port: ssh默认端口
    :return: 命令输出的字符串
    """
    # 创建SSH客户端实例
    client = paramiko.SSHClient()

    # 自动接受未知的SSH密钥（注意安全风险）
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到服务器
        client.connect(hostname, username=username, password=password,port=22)

        # 执行命令并获取输出
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        # Regular expression to match the lines containing gateways
        gateway_regex = re.compile(r'^\S+\s+(\S+)\s+\S+\s+UG', re.MULTILINE)
        gateways = gateway_regex.findall(output)
        return gateways[0]

    finally:
        # 无论是否出错都要关闭连接
        client.close()

def ssh_execute(hostname, username, password, command='ls /tmp',port=22):
    """
    连接到SSH服务器并执行命令。

    :param hostname: SSH服务器的主机名或IP地址
    :param username: SSH用户名
    :param password: SSH密码
    :param command: 要在远程服务器上执行的命令
    :param port: ssh默认端口
    :return: 命令输出的字符串
    """
    # 创建SSH客户端实例
    client = paramiko.SSHClient()

    # 自动接受未知的SSH密钥（注意安全风险）
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到服务器
        client.connect(hostname, username=username, password=password,port=22)

        # 执行命令并获取输出
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        return output

    finally:
        # 无论是否出错都要关闭连接
        client.close()

if __name__ == '__main__':
  # 设置SSH连接的参数
  hostname = '113.31.116.157'
  username = 'root'
  password = 'WBk-0TZ-vhK'
  command = 'pwd'

  # 调用函数并打印结果
  output = ssh_execute(hostname, username, password, command)
  print(output)
  output = ssh_execute(hostname, username, password)
  print(output)
  gateway = ssh_get_route(hostname, username, password)
  print('本机的网关为：')
  print(gateway)
