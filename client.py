import os
from time import sleep

minimum_lag = 10
receive_count = 0
while True:
    banner = '-'*36+'Update #%d' % receive_count + '-'*36
    print(banner)
    os.system("git pull") 
    print('-'*len(banner))
    sleep(minimum_lag)
