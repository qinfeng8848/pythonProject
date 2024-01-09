import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    """
    Function to execute multiple commands on a router using SSH, with handling of enable mode and full output capture.
    Args:
    - ip (str): IP address of the router.
    - username (str): Username for SSH login.
    - password (str): Password for SSH login.
    - cmd_list (list): List of commands to execute on the router.
    - enable (str): Enable password, if required. Default is ''.
    - wait_time (int): Time to wait for router response. Default is 2 seconds.
    - verbose (bool): If True, print the output of the commands. Default is True.
    """
    # Initialize SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the router
        ssh_client.connect(hostname=ip, username=username, password=password)

        # Get the shell
        remote_connection = ssh_client.invoke_shell()
        time.sleep(wait_time)

        # Disable paging
        remote_connection.send('terminal length 0\n')
        time.sleep(wait_time)

        # Check the initial prompt and switch to enable mode if necessary
        remote_connection.send('\n')
        time.sleep(wait_time)
        output = remote_connection.recv(65535).decode('ascii')
        if '>' in output:
            remote_connection.send('enable\n')
            if enable:
                remote_connection.send(f'{enable}\n')
            time.sleep(wait_time)

        # Execute each command and capture the output
        full_output = ""
        for cmd in cmd_list:
            remote_connection.send(cmd + '\r\n')
            time.sleep(wait_time)
            output = remote_connection.recv(65535).decode('ascii')
            full_output += output

        # If verbose is True, print the full output
        if verbose:
            print(full_output)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        if ssh_client is not None:
            ssh_client.close()

if __name__ == '__main__':
    cmd_list=['show version', 'configure terminal','router ospf 1','network 192.168.123.0 0.0.0.255 area 0','end','wr']
    qytang_multicmd('192.168.123.1', 'admin', 'Cisc0123', cmd_list, enable='')
