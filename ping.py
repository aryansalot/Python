import threading 
import os

target_ip = ["8.8.8.8", "10.10.10.10", "192.168.20.6"]

def ping(ip):
    output = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if output == 0:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is not reachable")
        
threads = []

for ips in target_ip:
    t = threading.Thread(target=ping, args=(ips,))
    t.start()
    threads.append(t) 
    
for t in threads:
    t.join()

print("All pings completed.")
    