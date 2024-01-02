import socket
import time
def is_port_open(ip, port, protocol):
    """Check if the specified port on a given IP is open for the specified protocol (TCP or UDP)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM) as s:
        if protocol == "tcp":
            s.settimeout(1)  # Timeout for TCP connection
            try:
                # Attempt to connect to the TCP port
                return s.connect_ex((ip, port)) == 0
            except socket.error:
                return False
        else:
            # UDP is connectionless; this method is less reliable for UDP
            try:
                s.sendto(b'', (ip, port))  # Sending empty byte
                s.settimeout(1)
                s.recvfrom(1024)
                return True
            except socket.error:
                return False
def monitor_tcp_ports(ip, ports):
    """Monitor multiple TCP ports and stop alerting when any of the ports is open."""
    while True:
        open_ports = [port for port in ports if is_port_open(ip, port, "tcp")]
        if open_ports:
            print(f"http(tcp/80)服务已经被打开  TCP port(s) {', '.join(map(str, open_ports))} on {ip} is/are open. Stopping alerts.")
            break
        else:
            for port in ports:
                print(f"等待一秒重新开始监控Alert: TCP port {port} on {ip} is not open!")
            time.sleep(1)  # Wait for 1 second before rechecking all ports

# Monitor both TCP ports 80 and 8000 on localhost
monitor_tcp_ports("127.0.0.1", [80,8000])
