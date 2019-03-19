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


        # search_button = self.driver.find_element_by_id('com.winds.karyakarta:id/search_view')
        # search_button.click()
        #
        # name_serach_box = self.driver.find_element_by_id('com.winds.karyakarta:id/search_view')
        # name_serach_box.send_keys('Hindi')
        #
        # time.sleep(2)
        #
        # msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("हिंदी")')
        # msg.click()
        # self.driver.hide_keyboard()
        # time.sleep(2)
        #
        # send_button = self.driver.find_element_by_id('com.winds.karyakarta:id/btn_continue')
        # send_button.click()
        #
        # # Login page
        # name_serach_box = self.driver.find_element_by_id('com.winds.karyakarta:id/edt_mobile_number')
        # name_serach_box.send_keys('8920828585')
        #
        # name_serach_box = self.driver.find_element_by_id('com.winds.karyakarta:id/edt_password')
        # name_serach_box.send_keys('22222222')
        #
        # login_button = self.driver.find_element_by_id('com.winds.karyakarta:id/btn_login')
        # login_button.click()
        # time.sleep(1)

        # permission_allow_button = self.driver.find_element_by_id( 'com.android.packageinstaller:id/permission_allow_button')
        # permission_allow_button.click()

        # profile_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_Profile1')
        # profile_button.click()
        #
        # time.sleep(2)
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable('
        #                                                         'true).instance(0))''.getChildByText(new UiSelector('
        #                                                         ').className("android.widget.TextView"), '
        #                                                         '"' + 'कार्यकर्ता क्रमांक' + '")')
        #
        # time.sleep(2)
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable('
        #                                                         'true).instance(0)).getChildByText(new UiSelector('
        #                                                         ').className("android.widget.TextView"), '
        #                                                         '"' + '8920828585' + '")')
        #
        # time.sleep(2)
        # edit_profile_button = self.driver.find_element_by_id('com.winds.karyakarta:id/ib_edit_btn')
        # edit_profile_button.click()
        # time.sleep(2)
        # self.driver.back()
        # time.sleep(2)
        # self.driver.back()

        time.sleep(5)
        mypartner_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_tab2')
        mypartner_button.click()

        time.sleep(5)
        nearby_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_tab3')
        nearby_button.click()

        time.sleep(5)
        noti_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_tab4')
        noti_button.click()

        time.sleep(5)
        noti_button = self.driver.find_element_by_id('com.winds.karyakarta:id/tv_tab1')
        noti_button.click()
        time.sleep(8)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WindsCaptainTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
