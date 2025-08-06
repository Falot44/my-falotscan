import socket

common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

def scan_ports(ip, ports):
    open_ports = []
    closed_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()
    return open_ports, closed_ports

def main():
    ip = input("🎯 Enter Target IP: ")
    print(f"\n🔎 Scanning common ports on {ip}...\n")
    open_ports, closed_ports = scan_ports(ip, common_ports)
    if open_ports:
        print("🟢 Open Ports:")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("❌ No common ports are open.")
    if closed_ports:
        print("\n🔴 Closed Ports:")
        for port in closed_ports:
            print(f" - {port}")

if __name__ == "__main__":
    main()