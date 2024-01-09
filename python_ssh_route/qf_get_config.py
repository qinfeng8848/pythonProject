from qf_ssh import qyt_ssh
import re
import hashlib
import time

def qf_get_config(ip,username,password,comm):
    try:
        ssh_output=qyt_ssh(hostname=ip, username=username, password=password,comm=comm)
        extracted_config = re.search(r'hostname.*end', ssh_output, re.DOTALL)
        extracted_config.group(0) if extracted_config else "No match found"
        return extracted_config.group(0)
    except Exception:
        return


def qf_check_diff(ip, username, password, comm):
    before_md5 = None
    while True:
        ssh_output = qyt_ssh(hostname=ip, username=username, password=password, comm=comm)
        extracted_config = re.search(r'hostname.*end', ssh_output, re.DOTALL)

        if not extracted_config:
            print("No configuration found.")
            break

        m = hashlib.md5()
        m.update(extracted_config.group().encode())
        current_md5 = m.hexdigest()

        if before_md5 is not None:
            if current_md5 == before_md5:
                print(current_md5)
            else:
                print(f"Configuration changed! New MD5: {current_md5}")
                break
        else:
            before_md5 = current_md5
            print(f"Initial MD5: {current_md5}")

        time.sleep(5)


if __name__ == '__main__':
    # config=qf_get_config('192.168.123.1',username='admin',password='Cisc0123',comm="show running-config")
    config=qf_check_diff('192.168.123.1',username='admin',password='Cisc0123',comm="show running-config")

