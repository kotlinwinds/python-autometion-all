import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'NFIVFYAEVWPVFM4D'
        self.dc['appPackage'] = 'com.winds.karyakarta'
        self.dc['appActivity'] = '.ui.authentication.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        time.sleep(3)
        self.driver.swipe(796, 269, -930, 357, 5033)
        self.driver.swipe(107, 284, 1580, 257, 6337)
        self.driver.swipe(657, 1938, 561, 696, 7337)
        self.driver.swipe(461, 553, 557, 1757, 7825)

        self.driver.find_element_by_xpath("xpath=//*[@id='iv_supports']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='iv_call_support']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CANCEL']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='iv_supports']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='tv_mtd']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='iv_supports']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='iv_supports']").click()

    # self.driver.find_element_by_xpath("xpath=//*[@text='English' and @id='lng_name1']").click()
        # self.driver.find_element_by_xpath("xpath=//*[@text='CONTINUE']").click()
        #
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="edt_mobile_number"]')))
        # self.driver.find_element_by_xpath("xpath=//*[@id='edt_mobile_number']").send_keys('9448309290')
        #
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="edt_password"]')))
        # self.driver.find_element_by_xpath("xpath=//*[@id='edt_password']").send_keys('pgcaptain')
        #
        # self.driver.find_element_by_xpath("xpath=//*[@text='LOGIN']").click()
        #
        # self.driver.find_element_by_xpath("xpath=//*[@text='ALLOW']").click()
        #
        #

        #self.driver.find_element_by_xpath("xpath=//*[@text='Settings']").click()
        #self.driver.find_element_by_xpath("xpath=//*[@id='iv_back']").click()




    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
     unittest.main()