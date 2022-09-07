"""
日志格式化中的扩展字段
- %(扩展字段名)s
- logger.info(msg, extra)
"""

import logging


def init_logger():

    """
    filename  Specifies that a FileHandler be created, using the specified
              filename, rather than a StreamHandler.
    filemode  Specifies the mode to open the file, if filename is specified
              (if filemode is unspecified, it defaults to 'a').
    format    Use the specified format string for the handler.
    datefmt   Use the specified date/time format.
    style     If a format string is specified, use this to specify the
              type of format string (possible values '%', '{', '$', for
              %-formatting, :meth:`str.format` and :class:`string.Template`
              - defaults to '%').
    level     Set the root logger level to the specified level.
    stream    Use the specified stream to initialize the StreamHandler. Note
              that this argument is incompatible with 'filename' - if both
              are present, 'stream' is ignored.
    handlers  If specified, this should be an iterable of already created
              handlers, which will be added to the root handler. Any handler
              in the list which does not have a formatter assigned will be
              assigned the formatter created in this function.
    """
    # 配置 root 记录器的基本信息（格式化、处理器）
    logging.basicConfig(format='<%(asctime)s>  of %(user_id)s at %(pathname)s %(lineno)s line : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)


if __name__ == '__main__':
    init_logger()

    # 以root logger 记录信息
    # logger = logging.getLogger()
    # extra 指定日志格式中的扩展变量名的值， 是dict类型
    logging.info('hi, Disen info !',
                 extra={'user_id': '10009'})
    logging.warning('warn Disen 准时下课!',
                    extra={'user_id': '10009'})