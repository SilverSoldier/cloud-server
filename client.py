import requests
import time
import sys
import random
from multiprocessing import Process, Value

# url = 'http://34.95.72.238:8080/'
url = 'http://localhost:3000/'

N_REQUESTS = int(sys.argv[1])

def send_request():
    while 1:
        try:
            resp = requests.get(url + str(random.randint(20, 60)))
            break
        except requests.exceptions.ConnectionError:
            continue

threads = []

start = time.time()
for i in range(N_REQUESTS):
    t = Process(target=send_request)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

end = time.time()

print("{0} {1}".format(N_REQUESTS, (end-start)))
