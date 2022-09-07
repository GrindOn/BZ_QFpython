import threading
import time

# 多个线程可以同时操作一个全局变量(多个线程共享全局变量)
# 线程安全问题
ticket = 20


def sell_ticket():
    global ticket
    while True:  # ticket = 1  线程1:1  线程2: 1
        if ticket > 0:
            time.sleep(1)  # 线程1: ticket=1  线程2:ticket=1
            ticket -= 1  # 线程1: ticket = 0  线程2:ticket=-1
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
