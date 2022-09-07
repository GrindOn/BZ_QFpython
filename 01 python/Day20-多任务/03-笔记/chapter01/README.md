# 线程

python的thread模块是比较底层的模块，python的threading模块是对thread做了一些包装的，可以更加方便的被使用。

## 单线程

```python
import time

def saySorry():
    print("hello world")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        saySorry()
```

## 多线程

```python
import threading
import time


def saySorry():
    print("hello world")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t1 = threading.Thread(target=saySorry)
        t1.start()
```

### 说明

1. 可以明显看出使用了多线程并发的操作，花费时间要短很多
2. 当调用`start()`时，才会真正的创建线程，并且开始执行