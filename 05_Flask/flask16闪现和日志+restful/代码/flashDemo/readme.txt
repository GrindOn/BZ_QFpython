1. 闪现：
    记住：
    1。在一个请求结束的时候添加flash
        flash('恭喜！验证成功啦！','info')
        flash('哈哈哈','error')
        flash(username,'warning')
    2。在当前请求中渲染获取或者仅仅下一个请求中可以获取。

    添加闪现：（后面的类型是可选择的）
    flash('恭喜！验证成功啦！','info')
    flash('哈哈哈','error')
    flash(username,'warning')

    获取闪现内容：
    get_flash_messages(with_categories=[True/False])
    get_flashed_messages(category_filter=["error"])  可选的
    有针对性的获取对应类型的闪现消息

2.日志
    uwsgi ----》 uwsgi.log

    1.使用app自带，
      app.logger.info('')
      app.logger.debug('A value for debugging')
      app.logger.warning('A warning occurred (%d apples)', 42)
      app.logger.error('An error occurred')

    2.通过logging进行创建：
    import logging

    logger = logging.getLogger('name')  # 默认flask的名字叫：app
    logger = logging.getLogger('app')

    保存到文件：
    1。logging.basicConfig(filename='log.txt', filemode='a', level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    2。logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log1.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    3。使用logger.info('message')
