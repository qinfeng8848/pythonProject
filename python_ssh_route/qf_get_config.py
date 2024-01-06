from qf_ssh import qyt_ssh
import re
import hashlib
import time

def qf_get_config(ip,username,password,comm):
        ssh_output=qyt_ssh(hostname=ip, username=username, password=password,comm=comm)
        return ssh_output

if __name__ == '__main__':
    config=qf_get_config('192.168.123.1',username='admin',password='Cisc0123',comm="show running-config")
    print(config)