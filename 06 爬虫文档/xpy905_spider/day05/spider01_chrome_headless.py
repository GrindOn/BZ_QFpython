"""
配置Chrome的无头选项
爬取百度贴吧-Python
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def parse_data(flag=False):
    # 向下滚动 1000
    chrome.execute_script('var q = document.documentElement.scrollTop=5000')
    # 查找搜索结果
    posts = chrome.find_elements(By.CLASS_NAME, "s_post")
    if flag:
        posts = posts[1:]
    for post in posts:
        a = post.find_element(By.CSS_SELECTOR, '.p_title a')
        url = a.get_attribute('href')
        title = a.text

        print(url, title)

    time.sleep(3)
    # 查找下一页
    # 网页中的大于号 > 使用 &gt;
    chrome.find_element(By.LINK_TEXT, '下一页>').click()
    parse_data()


if __name__ == '__main__':

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # options.binary_location=r'/Users/apple/PycharmProjects/xpy905_spider/day04/chromedriver'

    chrome = Chrome(options=options)

    chrome.get('https://tieba.baidu.com/index.html')

    # 查询搜索框的元素
    chrome.find_element(By.ID, 'wd1').send_keys('Python')

    chrome.execute_script('var q = document.documentElement.scrollLeft=800')

    # 点击搜索按钮 search_btn_wrap
    chrome.find_element(By.XPATH, '//form[@id="tb_header_search_form"]/span[2]').click()

    time.sleep(1)

    parse_data(True) # True 第一次对搜索的数据去除第一项（user 信息）

    # 截取窗口的屏幕，保存图片
    chrome.save_screenshot('tiba.png')
    chrome.quit()  # chrome.close()