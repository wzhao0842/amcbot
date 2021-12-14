import threading
import datetime

def print_num():
    print(datetime.datetime.now())

# print_num()
for i in range(20):
    t = threading.Thread(target=print_num)
    t.start()
