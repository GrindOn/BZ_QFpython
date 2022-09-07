"""
多个urllib的请求处理器
- Cookie
- Proxy
- Http
"""
import json
from urllib.request import Request, build_opener, HTTPHandler, HTTPCookieProcessor, ProxyHandler
from http.cookiejar import CookieJar
from urllib.parse import urlencode

opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor(CookieJar()),
                      ProxyHandler(proxies={
                          'http': 'http://180.113.189.147:9999'
                      })
                      )

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019111173190'

data = {
    'rkey': '349d874cb30075e222d45ba63074a793',
    'password': '38e75ac3f5210589f03e2cf6e258ac616de4e29997ffd35169d2c29162a507ea',
    'origURL': 'http://www.renren.com/home',
    'key_id': '1',
    'icode': '',
    'f': 'http://www.renren.com/224549540',
    'email': 'dqsygcz@126.com',
    'domain': 'renren.com',
    'captcha_type': 'web_login',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Referer': 'http://www.renren.com/SysHome.do'
}

request = Request(post_url,
                  urlencode(data).encode('utf-8'),
                  headers)

resp = opener.open(request)  # http.client.HTTPResponse
bytes_ = resp.read()
ret = json.loads(bytes_.decode('utf-8'))  # {"code":true,"homeUrl":"http://www.renren.com/home"}
if ret['code']:
    resp = opener.open(ret['homeUrl'])
    bs = resp.read()
    print(bs.decode('utf-8'))
