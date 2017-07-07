import socket
from concurrent.futures import ThreadPoolExecutor

THREADS = 512
CONNECTION_TIMEOUT = 1

def ping(host, port, results = None):
    try:
        socket.socket().connect((host, port))
        if results is not None:
            results.append(port)
        print(str(port) + " Open")
        return True
    except:
        return False

def scan_ports(host):
    available_ports = []
    socket.setdefaulttimeout(CONNECTION_TIMEOUT)
    with ThreadPoolExecutor(max_workers = THREADS) as executor:
        print("\nScanning ports on " + host + " ...")
        for port in range(1, 65535):
            executor.submit(ping, host, port, available_ports)
    print("\nDone.")
    available_ports.sort()
    print(str(len(available_ports)) + " ports available.")
    print(available_ports)

def main():
    scan_ports("192.168.1.43")

if __name__ == "__main__":
    main()
