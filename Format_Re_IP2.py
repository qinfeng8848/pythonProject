import os
import re

def run_command(command):
    return os.popen(command).read()

def find_pattern(pattern, text, default=''):
    match = re.findall(pattern, text)
    return match[0] if match else default

def hex_to_dot_decimal(hex_str):
    if hex_str.startswith("0x"):
        hex_str = hex_str[2:]
    binary_str = bin(int(hex_str, 16))[2:].zfill(32)
    return '.'.join(str(int(binary_str[i:i+8], 2)) for i in range(0, 32, 8))

def main():
    ifconfig_result = run_command("ifconfig en0")

    ipv4_add = find_pattern(r"inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifconfig_result)
    netmask_hex = find_pattern(r"netmask\s+(0x[0-9a-fA-F]{8})", ifconfig_result)
    broadcast = find_pattern(r"broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifconfig_result)
    mac = find_pattern(r"ether\s+([0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2}\:[0-9A-Fa-f]{2})", ifconfig_result)

    dot_decimal_netmask = hex_to_dot_decimal(netmask_hex) if netmask_hex else 'Unknown'
    ipv4_gw = '.'.join(broadcast.split('.')[:-1]) + '.254' if broadcast else 'Unknown'

    print(f'IPv4 Address: {ipv4_add}')
    print(f'Netmask: {dot_decimal_netmask}')
    print(f'Broadcast: {broadcast}')
    print(f'MAC Address: {mac}')
    print(f'Assumed Gateway IP: {ipv4_gw}')

    if ipv4_gw != 'Unknown':
        ping_result = run_command(f"ping {ipv4_gw} -c 1")
        if 'bytes from' in ping_result:
            print("Gateway is reachable.")
        else:
            print("Gateway is not reachable.")

if __name__ == "__main__":
    main()
