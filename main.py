import stream.stream1 as stream1
import stream.stream2 as stream2
import stream.stream3 as stream3
import stream.stream4 as stream4
import threading
import time

timer = 0

thread1 = threading.Thread(target = stream1.getCount)
thread2 = threading.Thread(target = stream2.getCount)
thread3 = threading.Thread(target = stream3.getCount)
thread4 = threading.Thread(target = stream4.getCount)

lst = [0,0,0,0]
traffic = ["red","red","red","red"]

def read(ind):
    while True:
        f = open(f"stream/count{ind}",'r')
        data = f.read()
        if data != '': lst[ind-1] = int(data)
        f.close()

def Light():
    while True:
        mx = max(lst)
        max_ind = lst.index(mx)
        global traffic
        traffic = ["red","red","red","red"]
        traffic[max_ind] = "green"
        timer = mx
        time.sleep(timer//10)

def Print():
    while True:
        print(traffic)

read1 = threading.Thread(target = read, args = (1,))
read2 = threading.Thread(target = read, args = (2,))
read3 = threading.Thread(target = read, args = (3,))
read4 = threading.Thread(target = read, args = (4,))

printThread = threading.Thread(target = Print)
lightThread = threading.Thread(target = Light)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
read1.start()
read2.start()
read3.start()
read4.start()
printThread.start()
lightThread.start()

