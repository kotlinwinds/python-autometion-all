import os
import unittest
from appium import webdriver
from time import sleep
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WindsCaptainTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'oppo'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.winds.karyakarta'
        desired_caps['appActivity'] = 'com.winds.karyakarta.ui.authentication.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_text_friend(self):
        time.sleep(3)

        # forgot password
        login_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_forgot_password')
        login_button.click()

        # permission_allow_button = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
        # permission_allow_button.click()

        otp_mobile = self.driver.find_element_by_id('com.winds.karyakarta:id/edt_mob')
        otp_mobile.send_keys('8920828585')

        time.sleep(2)

        login_button = self.driver.find_element_by_id('com.winds.karyakarta:id/btn_btnSendOtp')
        login_button.click()

        # OTP Page

        time.sleep(5)

        otp_new_password = self.driver.find_element_by_id('com.winds.karyakarta:id/edt_new_password')
        otp_new_password.send_keys('22222222')

        self.driver.hide_keyboard()
        time.sleep(2)

        otp_retry_password = self.driver.find_element_by_id('com.winds.karyakarta:id/edt_retry_password')
        otp_retry_password.send_keys('22222222')

        self.driver.hide_keyboard()
        time.sleep(2)

        otp_submit_button = self.driver.find_element_by_id('com.winds.karyakarta:id/btn_btnOK')
        otp_submit_button.click()

        time.sleep(5)
        otp_alert_submit_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_ok')
        otp_alert_submit_button.click()

        time.sleep(10)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WindsCaptainTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
