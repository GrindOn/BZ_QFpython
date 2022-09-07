"""
初次使用日志
研究日志记录器、处理器和格式化之间的关系
"""

import logging
from logging import StreamHandler, FileHandler
from logging import Formatter

# StreamHandler 是控制输出的处理器


def new_logger(name):
    # 创建日志记录器
    logger = logging.getLogger(name)  # root
    logger.setLevel(logging.DEBUG)

    # 创建日志处理器
    handler = StreamHandler()
    handler.setLevel(logging.INFO)

    # 创建日志格式化对象
    formatter = Formatter(fmt='[ %(asctime)s of %(name)s - %(levelname)s ] %(message)s',
                          datefmt='%Y-%m-%d %H:%M:%S')  # time/datetime

    # 设置处理器的日志格式化
    handler.setFormatter(formatter)

    # 添加记录器的处理器
    logger.addHandler(handler)

    fileHandler = FileHandler('access.log', encoding='utf-8')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(Formatter(
        '<%(asctime)s> at %(lineno)s of %(name)s: %(message)s',
        '%m-%d %H:%M:%S'
    ))

    logger.addHandler(fileHandler)

    return logger


if __name__ == '__main__':
    logger = new_logger('spider')
    logger.info('hi, disen, 我正在认真的听课!')
    logger.debug('Disen, 我今天有点小意外，不能如时去听您课了!')