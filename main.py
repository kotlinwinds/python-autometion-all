import os
import unittest
from appium import webdriver
from time import sleep
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WhatappAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'oppo'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.whatsapp'
        desired_caps['appActivity'] = 'com.whatsapp.HomeActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        search_button=self.driver.find_element_by_id('com.whatsapp:id/menuitem_search')
        search_button.click()

        name_serach_box=self.driver.find_element_by_id('com.whatsapp:id/search_src_text')
        name_serach_box.send_keys('An')

        msg=self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("An")')
        msg.click()

        txt_box=self.driver.find_element_by_id('com.whatsapp:id/entry')
        txt_box.send_keys('hii h r u ?')

        send_button=self.driver.find_element_by_id('com.whatsapp:id/send')
        send_button.click()

        time.sleep(10)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatappAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
