from selenium.webdriver.common.by import By
"""以下为登录模块 配置数据 """
# 关闭弹窗
login_close_alert = By.ID, "com.yunmall.lc:id/img_close"
# 点击我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击 已有账号，去登录
login_username_exists = By.ID, "com.yunmall.lc:id/textView1"
# 用户名
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"