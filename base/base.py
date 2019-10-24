from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        # 不能为空，可以随便写
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.yunmall.lc'
        # 启动名
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
        # 声明⼿机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(loc[0], loc[1]))

    # 点击
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入
    def base_input(self, loc, value):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)
