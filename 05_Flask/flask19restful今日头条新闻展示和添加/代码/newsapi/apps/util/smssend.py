import hashlib
import json
import random
import ssl
import time
import urllib


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
            request = urllib.request.Request(self.API_URL, params)
            response = urllib.request.urlopen(request, timeout=1, context=context)
            content = response.read()

            return json.loads(content)
        except Exception as ex:
            print("调用API接口失败:", str(ex))
