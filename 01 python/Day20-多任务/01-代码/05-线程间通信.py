import threading, queue
import time


def produce():
    for i in range(10):
        time.sleep(0.5)
        print('生产++++++面包{} {}'.format(threading.current_thread().name, i))
        q.put('{}{}'.format(threading.current_thread().name, i))


def consumer():
    while True:
        time.sleep(1)
        # q.get()方法时一个阻塞的方法
        print('{}买到------面包{}'.format(threading.current_thread().name, q.get()))


q = queue.Queue()  # 创建一个q

# 一条生产线
pa = threading.Thread(target=produce, name='pa')
pb = threading.Thread(target=produce, name='pb')
pc = threading.Thread(target=produce, name='pc')

# 一条消费线
ca = threading.Thread(target=consumer, name='ca')
cb = threading.Thread(target=consumer, name='cb')
cc = threading.Thread(target=consumer, name='cc')

pa.start()
pb.start()
pc.start()

ca.start()
cb.start()
cc.start()
