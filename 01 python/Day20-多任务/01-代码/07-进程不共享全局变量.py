import os, multiprocessing, threading

n = 100


def test():
    global n
    n += 1
    print('test==={}里n的值是{}'.format(os.getpid(), hex(id(n))))


def demo():
    global n
    n += 1
    print('demo===={}里n的值是{}'.format(os.getpid(), hex(id(n))))


print(threading.current_thread().name)
test()  # 101
demo()  # 102

# 同一个主进程里的两个子线程。线程之间可以共享同一进程的全局变量

# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=demo)
# t1.start()
# t2.start()

# if __name__ == '__main__':
# 不同进程各自保存一份全局变量，不会共享全局变量
# p1 = multiprocessing.Process(target=test)
# p2 = multiprocessing.Process(target=demo)
# p1.start()  # 101
# p2.start()  # 101
