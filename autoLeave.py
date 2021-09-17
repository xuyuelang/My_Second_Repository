# import sys
# sys.path.append('E:\\Desktop\\Python\\venv\\Lib\\site-packages')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

usr = "202011225588"
psd = "********"
tel="17888888888"
url="https://auth.bupt.edu.cn/authserver/login?service=https%3A%2F%2Fservice.bupt.edu.cn%2Fsite%2Flogin%2Fcas-login%3Fredirect_url%3Dhttps%253A%252F%252Fservice.bupt.edu.cn%252Fv2%252Fmatter%252Fdetail%253Fid%253D578"

class TestCase6():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) # seconds
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_case6(self):
        self.driver.get(url)
        self.driver.set_window_size(1550, 832)
        self.driver.find_element(By.ID, "username").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "username").send_keys(usr)
        self.driver.find_element(By.ID, "password").send_keys(psd)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btnsubmit").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".header_bot .zl-button").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__footer:nth-child(3) .zl-button-line").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(4) .doneplugin-value").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(4) .doneplugin-value").send_keys(tel)
        self.driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-select__input").send_keys("西土城")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".el-select-dropdown__item > span").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".dplugin-userSearchInput").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "UserSearch_60").send_keys("谷")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".li-style:nth-child(1) > .span-style").click()
        #时间空间的输入##########
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .el-date-editor > .el-input__inner").click()
        time.sleep(1)

        d = self.driver.find_element_by_css_selector("td:nth-child(2) .el-date-editor > .el-input__inner")
        self.driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)
        # js = "$('input:eq(0)').removeAttr('readonly')"  # jQuery，移除属性
        # self.driver.execute_script(js)
        input_time = self.driver.find_element(By.CSS_SELECTOR,"td:nth-child(2) .el-date-editor > .el-input__inner")
        time.sleep(2)
        input_time.click()
        input_time.send_keys(Keys.CONTROL,'a')
        time.sleep(1)
        input_time.send_keys(Keys.SPACE,"07:07:41")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
        time.sleep(2)
        ##########结束时间##########
        self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(4) .el-input__inner").click()
        time.sleep(1)
        d = self.driver.find_element_by_css_selector("td:nth-child(4) .el-input__inner")
        self.driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)
        stop_time = self.driver.find_element(By.CSS_SELECTOR,"td:nth-child(4) .el-input__inner")
        time.sleep(2)
        stop_time.click()

        stop_time.send_keys(Keys.CONTROL,'a')
        time.sleep(1)
        stop_time.send_keys(Keys.SPACE,"23:07:41")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(12) > div.el-time-panel__footer > button.el-time-panel__btn.confirm").send_keys(Keys.ENTER)
        time.sleep(2)
        ######################
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[10]").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".el-popover__reference:nth-child(2) > input").send_keys("实习")
        self.driver.find_element(By.CSS_SELECTOR, ".dplugin-boxBorder").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".dplugin-boxBorder").send_keys("实习")
        self.driver.find_element(By.ID, "1716_Radio_52_0").click()
        time.sleep(2)
        # eles = self.driver.find_elements_by_css_selector('.zl-button:nth-child(4)')
        # ele = eles[0]
        # self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # 向上滚动500个像素
        self.driver.execute_script('window.scrollBy(0,-500)')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".zl-button:nth-child(4)").click()
        time.sleep(1)
