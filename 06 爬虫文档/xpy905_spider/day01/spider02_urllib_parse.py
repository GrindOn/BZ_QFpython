"""
应用： 百度翻译
- urllib.request.Request
- urllib.request.urlopen()
- urllib.parse.urlencode()
- 发起post请求
"""
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/sug'  # 请求的API接口

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Cookie': 'BIDUPSID=16CECBB89822E3A2F26ECB8FC695AFE0; PSTM=1572182457; BAIDUID=16CECBB89822E3A2C554637A8C5F6E91:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1573184257; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=1435_21084_30211_30283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; APPGUIDE_8_2_2=1; yjs_js_security_passport=0927713bf2c240ca607108086d07729426db4dbb_1577084843_js; __yjsv5_shitong=1.0_7_c3620451e4363f4aed30cbe954abf8942810_300_1577084847314_223.255.14.197_2d7151e0; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'x-requested-with': 'XMLHttpRequest'
}

def fanyi(kw):
    data = {
        'kw': kw
    }

    # Request() 中的data参数是byte类型
    # data不为空时，是post请求
    req = Request(url,
                  data=urlencode(data).encode('utf-8'),
                  headers=headers)

    resp = urlopen(req)
    assert resp.code == 200

    json_data = resp.read()  # byte

    content_encode = resp.getheader('Content-Type')
    content_encode = 'utf-8' if content_encode is None else content_encode.split('=')[-1]

    return json.loads(json_data.decode(content_encode))


if __name__ == '__main__':
    print(fanyi('orange'))




