import requests
import threading
import queue

subdomains = ["www", "mail", "ftp", "blog", "dev", "test", "api", "shop", "support", "admin"]

q = queue.Queue()

def check_subdomain(domain):
    while not q.empty():
        sub = q.get()
        url = f"https://{sub}.{domain}"
        try: 
            res = requests.get(url, timeout=3)
            if res.status_code < 400:
                print(f"[+] Found subdomain: {url}")
        except requests.ConnectionError:
            pass
        q.task_done()

def main():
    
    domain = input("Enter the domain to enumerate subdomains for: ")
    
    for sub in subdomains:
        q.put(sub)
    
    threads=[]
    for t in range(10):
       t = threading.Thread(target=check_subdomain, args=(domain,))
       t.start()
       t.deamon = True # kill background threads when main thread exits
       threads.append(t)
       
       for t in threads:
           t.join() 

    print("Subdomain enumeration completed.")

if __name__ == "__main__":
    main()