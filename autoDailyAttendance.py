
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestCase1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_case1(self):
        self.driver.get(
            "https:*****")
        self.driver.set_window_size(1550, 832)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input").send_keys("学号")
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input").send_keys("密码")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .radio div:nth-child(1) i").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) input").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) div:nth-child(2) > span > i").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,3349.512451171875)")
        self.driver.find_element(By.LINK_TEXT, "提交信息(Submit)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".wapat-btn").click()

