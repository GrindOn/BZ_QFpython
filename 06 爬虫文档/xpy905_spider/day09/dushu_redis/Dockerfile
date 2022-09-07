FROM 119.3.170.97:5000/ubuntu:latest
MAINTAINER disen 610039018@qq.com
ADD . /usr/src
VOLUME /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh