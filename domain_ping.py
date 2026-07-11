import threading, socket, os

websites = [
    "google.com",
    "github.com",
    "python.org",
    "example.com"
]

def domains(domain):
    try:
        socket.create_connection((domain,80), timeout=2)
        print(f"{domain} is reachable")
    except Exception as e:
        print(f"{domain} is not reachable")
        print(e)
        
thread=[]

for i in websites:
    t = threading.Thread(target=domains, args=(i,))
    t.start()
    thread.append(t)
    
for t in thread:
    t.join()
    
print("all done")