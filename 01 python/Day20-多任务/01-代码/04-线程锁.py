import threading
import time

ticket = 20

# 创建一把锁
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        print('呵呵呵')
        print('哈哈哈')
        print('ddd')
        print('ppp')
        print('sss')
        print('ttt')
        print('xxx')
        lock.acquire()  # 加同步锁
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            lock.release()
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name, ticket))
        else:
            lock.release()
            print('票卖完了')
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
