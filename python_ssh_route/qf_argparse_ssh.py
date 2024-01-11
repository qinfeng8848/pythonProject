import argparse
import paramiko


def create_ssh_client(ipaddr, username, password, command):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=ipaddr, username=username, password=password)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    # 获取命令结果
    output = stdout.read().decode()
    # 关闭连接
    ssh.close()
    return output


def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description='Simple SSH Client')
    # 添加参数
    parser.add_argument('-i', '--ipaddr', type=str, help='SSH Server IP Address', required=True)
    parser.add_argument('-u', '--username', type=str, help='SSH Username', required=True)
    parser.add_argument('-p', '--password', type=str, help='SSH Password', required=True)
    parser.add_argument('-c', '--command', type=str, help='Shell Command', required=True)

    # 解析参数
    args = parser.parse_args()

    # 使用提供的参数创建SSH客户端并执行命令
    output = create_ssh_client(args.ipaddr, args.username, args.password, args.command)

    # 打印输出
    print(output)


if __name__ == '__main__':
    main()
