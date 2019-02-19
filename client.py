import requests
import time
import sys
import random
from multiprocessing import Process, Value, Pool

# url = 'http://35.185.208.66:3000/'
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

pool = Pool()
start = time.time()
for i in range(N_REQUESTS):
    pool.apply_async(send_request)

pool.close()
pool.join()

end = time.time()

print("{0} {1}".format(N_REQUESTS, (end-start)))
