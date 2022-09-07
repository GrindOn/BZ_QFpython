#!/usr/bin/python3
# coding: utf-8
import re
import json
import time

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions

from utils.header import get_ua

headers = {
    'User-Agent': get_ua()
}


chrome = Chrome(executable_path='chromedriver')

def get_allcity():
    url = 'https://www.zhaopin.com/citymap'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        html = resp.text
        s = re.search(r'<script>__INITIAL_STATE__=(.*?)</script>', html)
        json_data = s.groups()[0]
        data = json.loads(json_data)
        cityMapList = data['cityList']['cityMapList']  # dict
        for letter, citys in cityMapList.items():
            print(f'----{letter}----')
            for city in citys:
                """
                {
                    "name": "鞍山",
                    "url": "//www.zhaopin.com/anshan/",
                    "code": "601",
                    "pinyin": "anshan"
			    }
                """
                yield city


def get_city_jobs(url):
    chrome.get(url)  # 打开城市

    # 查找警告信息的button
    btn = chrome.find_element_by_css_selector('.risk-warning__content>button')
    btn.click()

    # 根据class_name查询WebElement
    input_search: WebElement = chrome.find_element_by_class_name('zp-search__input')
    input_search.send_keys('Python')

    # 开始搜索
    chrome.find_element_by_class_name('zp-search__btn--blue').click()
    time.sleep(1)

    # 当前浏览器打开第二个窗口
    chrome.switch_to.window(chrome.window_handles[1])

    chrome.execute_script('var q=window.document.documentElement.scrollTop=1000')
    time.sleep(5)
    chrome.execute_script('var q=window.document.documentElement.scrollTop=2000')
    time.sleep(0.2)

    # 等待 class_name 为 "contentpile__content" div元素的出现
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                'contentpile__content')),
        '查找的元素一直没有出现'
    )

    # 判断当前查询的结果是否不存在
    nocontent = chrome.find_element_by_class_name('contentpile__jobcontent__notext')
    if not nocontent:
        print('当前城市未查找到Python岗位')
    else:
        # 提取查询结果
        divs = chrome.find_elements_by_class_name('contentpile__content__wrapper')
        for div in divs:
            # 每一个岗位
            job_info_url = div.find_element(By.XPATH, './/a/@href')
            print(job_info_url)


def get_city_jobs2(url):
    chrome.get(url)
    chrome.find_element_by_css_selector('.risk-warning__content>button').click()

    chrome.execute_script('var q=window.document.documentElement.scrollTop=3000')
    time.sleep(0.2)
    chrome.execute_script('var q=window.document.documentElement.scrollTop=5000')
    time.sleep(0.2)

    # 等待 class_name 为 "contentpile__content" div元素的出现
    ui.WebDriverWait(chrome, 120).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,
                                                                'contentpile__content')),
        '查找的元素一直没有出现'
    )

    # 判断当前查询的结果是否不存在
    nocontent = chrome.find_element_by_class_name('contentpile__jobcontent__notext')
    if not nocontent:
        print('当前城市未查找到Python岗位')
    else:
        # 提取查询结果
        divs = chrome.find_elements_by_class_name('contentpile__content__wrapper')
        for div in divs:
            # 每一个岗位
            job_info_url = div.find_element(By.XPATH, './/a/@href')
            print(job_info_url)


        chrome.save_screenshot('a.png')
        chrome.get_cookies()
        chrome.get_window_rect() # left/top/right,bottom
        chrome.get_window_size() # width, height
        chrome.get_window_position()




if __name__ == '__main__':

    query_citys = ('北京',
                   '西安',
                   '上海')
    for city in get_allcity():
        # 保存city城市信息
        # 请求城市下的所有Python岗位
        if city['name'] in query_citys:
            print(city)
            # https://sou.zhaopin.com/?jl=854&kw=Python&kt=3
            get_city_jobs('https:'+city['url'])
            # get_city_jobs2(f'https://sou.zhaopin.com/?jl={city["code"]}&kw=Python&kt=3')
            time.sleep(5)
