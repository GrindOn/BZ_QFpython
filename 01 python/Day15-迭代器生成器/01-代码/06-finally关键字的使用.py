file = open('../02-视频/03-练习3.mp4', 'rb')

try:
    while True:
        content = file.read(1024)
        if not content:
            break
        print(content)
finally:  # 最终都会被执行的代码
    print('文件被关闭了')
    file.close()
