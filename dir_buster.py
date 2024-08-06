import requests, queue, threading, sys

host = sys.argv[1]
threads = int(sys.argv[2])
try:
    ext = sys.argv[3]
except IndexError:
    ext = False

try:
    requests.get(host)
except Exception as e:
    print(e)
    exit(0)

print("[+] Scanning for directories!")
directory_list = open('file_name')

q = queue.Queue()

def dirbuster(thread_no, q):
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url, allow_redirects=False, timeout=2)
            if response.status_code == 200:
                print(f"[+] Directory found: {url}")
        except requests.RequestException:
            pass
        q.task_done()

for directory in directory_list.read().splitlines():
    if not ext:
        url = host.rstrip('/') + '/' + directory
    else:
        url = host.rstrip('/') + '/' + directory + ext
    q.put(url)

for i in range(threads):
    t = threading.Thread(target=dirbuster, args=(i, q))
    t.daemon = True
    t.start()

q.join()
