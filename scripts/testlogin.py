import sys
import os
sys.path.append(os.getcwd())
from tools.read_data import read_yaml
from page.page_in import PageIn
import pytest

def get_data():
    arr = []
    for data in read_yaml('data.yaml').values():
         arr.append(tuple(data.values()))
    return arr



class TestLogin():
    def setup_class(self):
        self.login = PageIn().get_page_login()
        # 获取弹窗
        self.login.page_close_alert()
        # 点击我
        self.login.page_click_me()
        # 点击已有帐户
        self.login.page_click_username_exists()

    def teardown_class(self):
        # 关闭driver
        self.login.driver.quit()

    @pytest.mark.parametrize("username,pwd", get_data())
    def test_login(self, username, pwd):
        self.login.page_login(username, pwd)
