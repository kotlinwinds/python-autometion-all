import time
from selenium import webdriver

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/karun/Downloads/chromedriver/chromedriver")
driver.get(url)

driver.find_element_by_id('email').send_keys('karunkumar2525@gmail.com')
driver.find_element_by_id('pass').send_keys('nh@12345')
driver.find_element_by_id('loginbutton').click()






# driver = webdriver.Chrome("/Users/karun/Downloads/chromedriver/chromedriver")  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml')
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
#
#



# from selenium import webdriver
#

