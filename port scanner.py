import socket
from tqdm import tqdm

# Port dictionary
port_names = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

target = input("Enter target IP: ")

print(f"\nScanning target: {target}\n")

for port in tqdm(range(1, 1025), desc="Scanning Ports"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        service = port_names.get(port, "Unknown")
        print(f"Port {port} is open ({service})")

    sock.close()
