#!/bin/bash

path=~/venv/xiaohua
echo "验证爬虫环境是否已存在"  >> run.log
if [ -d $path ]; then
    echo "正在激活环境" >> run.log
    source $path/bin/activate
else
    echo "正在初始安装爬虫环境" >> run.log
    apt update
    apt install virtualenv -y
    virtualenv ~/venv/xiaohua -p python3
    source ~/venv/xiaohua/bin/activate
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
    echo "爬虫环境已就绪"  >> run.log

fi

if [ ${#} == 1 ] ;then
    echo "正在定量爬取数据..." >> run.log
    nohup scrapy crawl ertong -s CLOSESPIDER_ITEMCOUNT=$1  &
else
    echo "初次开启爬虫..." >> run.log
    nohup scrapy crawl ertong &
fi