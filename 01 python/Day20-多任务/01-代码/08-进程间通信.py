import os, multiprocessing, time


def producer(x):
    for i in range(10):
        time.sleep(0.5)
        print('生产了+++++++pid{} {}'.format(os.getpid(), i))
        x.put('pid{} {}'.format(os.getpid(), i))


def consumer(x):
    for i in range(10):
        time.sleep(0.3)
        print('消费了-------{}'.format(x.get()))


if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=producer, args=(q,))
    p3 = multiprocessing.Process(target=producer, args=(q,))
    p1.start()
    p2.start()
    p3.start()

    c2 = multiprocessing.Process(target=consumer, args=(q,))
    c2.start()
