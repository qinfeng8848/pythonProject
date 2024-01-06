import re
import pprint
from qf_ping import qyt_ping
from qf_ssh import qyt_ssh

def qyt_get_if(*ips,username,password,comm):
    devices_if_dict = {}
    for ip in ips:
        if qyt_ping(ip):
            ssh_output=qyt_ssh(hostname=ip, username=username, password=password,comm=comm)
            pattern = r"(GigabitEthernet\d+)\s+([\d\.]+)"
            # Find all matches in the text
            matches = re.findall(pattern, ssh_output)
            # Creating a dictionary from the matches
            interfaces_dict = {match[0]: match[1] for match in matches}
            devices_if_dict.update({ip: interfaces_dict})
        else:
            devices_if_dict.update({ip:{}})
    return devices_if_dict

if __name__ == "__main__":
    devices_if_dict=qyt_get_if('192.168.123.1','192.168.123.2',username='admin',password='Cisc0123',comm="show ip int bri")
    pprint.pprint(devices_if_dict,indent=4)