# -*- coding: utf-8 -*-
import hashlib
import json
import random
import ssl
import time
import urllib
import urllib.parse
import urllib.request
import requests


class SecretPair(object):
    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key


class SmsSendAPIDemo(object):
    """易盾短信发送接口示例代码"""
    API_URL = "https://sms.dun.163yun.com/v2/sendsms"
    VERSION = "v2"

    def __init__(self, business_id, secret_pair):
        self.business_id = business_id
        self.secret_pair = secret_pair

    def gen_signature(self, params=None):
        """生成签名信息
        Args:
            params (object) 请求参数
        Returns:
            参数签名md5值
        """
        buff = ""
        for k in sorted(params.keys()):
            buff += str(k) + str(params[k])
        buff += self.secret_pair.secret_key
        buff = buff.encode('utf-8')
        return hashlib.md5(buff).hexdigest()

    def send(self, params):
        """请求易盾接口
        Args:
            params (object) 请求参数
        Returns:
            请求结果，json格式
        """
        params["secretId"] = self.secret_pair.secret_id
        params["businessId"] = self.business_id
        params["version"] = self.VERSION
        params["timestamp"] = int(time.time() * 1000)
        params["nonce"] = int(random.random() * 100000000)
        params["signature"] = self.gen_signature(params)

        try:
            params = urllib.parse.urlencode(params)
            params = params.encode('utf-8')
            context = ssl._create_unverified_context()  # 忽略安全
            request = urllib.request.Request(self.API_URL,params)
            response = urllib.request.urlopen(request,timeout=1,context=context)
            content = response.read()
            # request = urllib2.Request(self.API_URL, params)
            # content = urllib2.urlopen(request, timeout=1).read()
            # print(params)
            # headers = {
            #     "Content-Type": "application/x-www-form-urlencoded"
            # }
            #
            # response = requests.post(self.API_URL, data=params, headers=headers)

            return json.loads(content)
        except Exception as ex:
            print("调用API接口失败:", str(ex))


if __name__ == "__main__":
    """示例代码入口"""
    SECRET_ID = "dcc535cbfaefa2a24c1e6610035b6586"  # 产品密钥ID，产品标识
    SECRET_KEY = "d28f0ec3bf468baa7a16c16c9474889e"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "748c53c3a363412fa963ed3c1b795c65"  # 业务ID，易盾根据产品业务特点分配
    secret_pair = SecretPair(SECRET_ID,SECRET_KEY)
    api = SmsSendAPIDemo(BUSINESS_ID,secret_pair)

    params = {
        "mobile": "15010185644",
        "templateId": "11732",
        "paramType": "json",
        "params": {"code": "123"}
        # 国际短信对应的国际编码(非国际短信接入请注释掉该行代码)
        # "internationalCode": "对应的国家编码"
    }
    ret = api.send(params)
    print(ret)
    if ret is not None:
        if ret["code"] == 200:
            taskId = ret["data"]["requestId"]
            print("taskId = %s" % taskId)
        else:
            print("ERROR: ret.code=%s,msg=%s" % (ret['code'], ret['msg']))
