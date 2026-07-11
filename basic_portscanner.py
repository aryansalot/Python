import socket
import threading

domain = input("Enter the Domain: ")
ip = socket.gethostbyname(domain)

print(f"Target {ip} is scanning...")

def port_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

def thread_scan():
    threads = []

    for port in range(1,1025):
        t = threading.Thread(target=port_scan, args=(ip, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

thread_scan()