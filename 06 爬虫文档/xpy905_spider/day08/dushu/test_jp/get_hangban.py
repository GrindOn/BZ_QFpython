#!/usr/bin/python3
# coding: utf-8

import requests
import re

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, ui

from lxml import etree

session = requests.session()

headers = {
    'referer': 'https://www.koreanair.com/global/zh_cn.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


def cookies():
    cookie_text = 'TLTSID=8B729FF02D53102D6B239BE804E20908; TLTUID=8B729FF02D53102D6B239BE804E20908; NULL=!9CXKKwV1p+JZ5KWvAHTlf2z3ytcFAg/Gqpinoa/j65bnRv84Syj/CA+vokiYreUruofTMDpyO65uS9E=; AKA_A2=A; bm_sz=EEEF4CF9D1F5903AF5E52CC0F7F175A7~YAAQxJ7C3V+J6BlvAQAA6SoHZgaTe2mt3v3FvFXJBmuw5FpwMlpligmoOq66VOa5lAS4fJKm2aDF2BpPxR7SoN/JYwjg2ezyst2HemL80i5O8P7N9yZj6IAbRNd07rtuUTnYG95khpctZ7sQZ9i6NJ3GIUazXwcoIcSV1We7lqJDcQPupJ9x2HLs2UZcfhlCTG+P; isBrowserInfo=true; JSESSIONID=0001hzgdiEhUgag_oy-OJboYTdP:18kit8m7o; lang=zh-cn; country=cn; AMCVS_3131246452DDAE2D0A490D45%40AdobeOrg=1; psn_adapter_s=0001wOWt0mH7xI-QrpTLEc0zi4O:-8K4LFK; AMCV_3131246452DDAE2D0A490D45%40AdobeOrg=1687686476%7CMCIDTS%7C18264%7CMCMID%7C42186091414444443494257870232739777451%7CMCAAMLH-1578569545%7C11%7CMCAAMB-1578569545%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1577971945s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; _abck=942EEA2A2001DBF56DA518E26D826772~0~YAAQxJ7C3eKK6BlvAQAAp0QHZgOVsmlGz9kT0GlOD17nhjkWWFZc2k1w8D38el6HOwGPpVoisxiAHjeiXY7a3u2oyXheXJtP6Mxi/BHb2ih1ni6rK+KJ6zUvxW+V7hdUboFtfetyc6uF6Fs7Gy21MDGvb4cOsSpGvv9eiaW0GQzosyb4yidZe0LU4c/CZNIGGc3yxV/WaNoZcJemxD2TlAxVHnwDwVD+vAube1k88RH/DPPAYIcUU/AIbplI0zh0VIhteDLtzYjpVeVnzjejcDhCNqz7TW2bk9Okf5QpKGH91m6TquT3HozhN90pNjIPe9MqIowAPiS8bA==~-1~-1~-1; ak_bmsc=3393DFF5EAC14F8345B20D056264F327DDC29EC48B380000C7D40D5EBDA3C851~pl91AYoi5dW0vhVJbFPCymDew0zTQ/ZE5PLlBEOvbUOGBMS9iQx1bvh7QunLLOr3v9irZkMkguTtE8zV4N2UEfnIcq0RedD4fx1N3Rd0hYCV11ePoC/+MhHF3S1AxAcyoCgedUl3D4sMTkNvynKpo9KWbnt3AyeW0HeaFElMCmwyozYsvgWBKntxlV45fOT41xjTniXQTpbfcRonbYSw/Ik4EgchCtYw2KTjdgmGzNLuSxt7TuxHtQhx0nSL5WRJgY; _sdsat_member_info_gender=false; _sdsat_member_info_ages=false; _sdsat_member_info_skypass_tier=false; _sdsat_member_info_remaining_miles=false; _sdsat_member_info_encrypt_id=false; s_vmonthnum=1580486400318%26vn%3D1; s_cc=true; px_dsp_s_cnt_k=1; physicalCountry=cn; br_ss=y; s_getNewRepeat=1577964812938-New; s_bghstr=100010CFA5251F632F8C4D8F6DDA4C82E90883F00ABB5924B248FAA55F5D419C7D005EEDEE3E2CFB5B5FD2C655A56CFFA0CEF082FBAA54A2A153306261A6AD34B130AA; s_sq=kal-pc-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddow_book2%2526link%253D%2525E7%2525A1%2525AE%2525E8%2525AE%2525A4%2526region%253Dmodal-contents-2%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Ddow_book2%2526pidt%253D1%2526oid%253D%2525E7%2525A1%2525AE%2525E8%2525AE%2525A4%2526oidt%253D3%2526ot%253DSUBMIT; S_CT=EAAQiz4cutSIy3Yog0YVtVe9duGGjXlOUMQvVy9aRu0PLJI%3D; S_RID=E0F1446BCFEB4782ADF6B26D3732B4D5; bm_sv=75845A7AD0DC48E38527F5C4698975C2~ybIGGMu1nmmKms5GIKm0jPOS8SbtlvkA9v2tx3Yo+3EjRQ6Su8TCDHxZiLX/BCuwKKHvbCa8hmy/qYX/vfthrwKZqW7Yv0gf/tTqZHjfdsaLAGuGetJ0vK7CXyZwltabYolKYG0UXxIp/yLaQLocUWSzk+/YtzBusjXJCQpApGs=; adcloud={%22_les_v%22:%22y%2Ckoreanair.com%2C1577968484%22}'

    ret = {}
    for item in cookie_text.split(';'):
        k, v = re.search(r'(.+?)=(.+)', item).groups()
        ret[k.strip()] = v

    return ret

def request(url, method="get"):
    if method == "get":
        resp = session.get(url, headers=headers, cookies=cookies())
    else:
        resp = session.post(url, headers=headers)

    return resp


def get_token():
    resp = request('https://www.koreanair.com/libs/granite/csrf/token.json')
    print(resp.status_code)
    print(resp.cookies)


def get_user():

    resp = request('https://www.koreanair.com/api/min/user?_=%s' % time_)
    print(resp.status_code)

    resp = request(
        'https://www.koreanair.com/content/koreanair-mobile-admin/cross-region/all-languages/korean-issued-credit-cards/_jcr_content/par/list.cardList.json/kr.json')
    print(resp.status_code)

    resp = session.post('https://www.koreanair.com/interactService/',
                        headers=headers,
                        cookies=cookies(),
                        json={"login":"N","mileage":"0","tier":"","lang":"zh-cn","country":"cn","category":"default","device":"W","firstname":"","lastname":"","age":"0","resegFlag":"Y","source":"web","go_ip_name":"Main_QuickBooking_Prefill_W","command":"SERVICE"})
    print(resp.status_code)
    print(resp.text)

    resp = request('https://c.go-mpulse.net/api/config.json?key=JKBJR-D4E3F-X43RV-K89VT-9ZMRT&d=www.koreanair.com&t=5259889&v=1.632.0&if=&sl=0&si=v191dtfgfj-q3havu&plugins=AK,ConfigOverride,Continuity,PageParams,IFrameDelay,AutoXHR,SPA,Angular,Backbone,Ember,History,RT,CrossDomain,BW,PaintTiming,NavigationTiming,ResourceTiming,Memory,CACHE_RELOAD,Errors,TPAnalytics,UserTiming,Akamai,LOGN&acao=&ak.ai=193669')
    print(resp.status_code)
    print(resp.text)


def get_info():
    resp = request(
        'https://www.koreanair.com/api/fly/revenue/from/SEL/to/PUS/on/01-30-2020-0000?flexDays=2&scheduleDriven=false&purchaseThirdPerson=&domestic=true&isUpgradeableCabin=false&currency=&bonusType=SKYPASS&countryCode=&adults=1&children=0&infants=0&cabinClass=ECONOMY&adultDiscounts=&adultInboundDiscounts=&childDiscounts=&childInboundDiscounts=&infantDiscounts=&infantInboundDiscounts=&_=%s' % time_)
    print(resp.status_code)
    print(resp.text)


def wait(by, value):
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_all_elements_located((by, value)),
        f'没有发现 {value}'
    )

def from_chrome(chrome):
    chrome.get('https://www.koreanair.com/global/zh_cn.html')

    wait(By.CLASS_NAME, 'airports-single')
    chrome.execute_script('var q=document.documentElement.scrollTop=1000')
    chrome.find_element(By.ID, 'oneway').click()
    inputs = chrome.find_elements(By.CSS_SELECTOR, '.airports-single input')
    inputs[0].send_keys('釜山(PUS)')
    inputs[1].send_keys('济州(CJU)')
    time.sleep(1)
    inputs[2].send_keys('20200122')
    time.sleep(1)

    chrome.find_element(By.ID, 'submit').click()
    chrome.find_element(By.ID, 'submit').click()

    wait(By.CLASS_NAME, 'flight-select-table')

    return chrome.page_source

def parse():
    with open('a.html', encoding='utf-8') as f:
        html = f.read()

    root = etree.HTML(html)
    trs = root.xpath('//tr[starts-with(@class,"scroll-flight")]')
    for tr in trs:
        item = {}
        item['no'] = tr.xpath('./th/span[1]/text()')[0]
        item['type_'] = tr.xpath('./th/span[2]/a/text()')[0]
        item['start_end_time'] = tr.xpath('./th/strong/text()')[0]
        item['price'] = [ item.strip() for item in tr.xpath('./td/div[1]/div[2]//label/text()') if item.strip()]
        item['ws'] = [item.strip() for item in tr.xpath('./td/div[1]/div[2]/span[2]/text()') if item.strip()]

        print(item)


if __name__ == '__main__':
    # chrome = Chrome()
    # html = from_chrome(chrome)
    # with open('a.html', 'w', encoding='utf-8') as f:
    #     f.write(html)
    #
    # print('---ok---')
    # chrome.quit()
    parse()