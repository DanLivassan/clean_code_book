from multiprocessing import Process
import threading
import os
import time


def func(sec, number):
    time.sleep(sec/10)
    for i in range(100000):
        a=1**1/6
        b = a**7
        c = zip([a],[b])
    print(f"process {number}")
processes = []
threads = []
num_of_processers = os.cpu_count()

# MULTIPROCESS
for i in range(num_of_processers):
    process = Process(target=func, args=(i,i,))
    processes.append(process)

t1 = time.time()
for process in processes:
    process.start()
for process in processes:
    process.join()
t2 = time.time()
print(f"{t2-t1:.2f} seconds elapsed")

#MULTITHREADING
for i in range(num_of_processers):
    threads.append(threading.Thread(target=func, args=(i, i)))
t1 = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
t2 = time.time()
print(f"{t2-t1:.2f} seconds elapsed")
#REGULAR WAY
t1 = time.time()
for i in range(num_of_processers):
    func(i,i)
t2 = time.time()
print(f"{t2-t1:.2f} seconds elapsed")