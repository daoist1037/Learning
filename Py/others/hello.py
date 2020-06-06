""" a = 3
a+1
print(a)
print('hello', end='')
print('\b'*5, end='', flush=True)
print('HELLO') """

# hello world
# hello world


from selenium import webdriver
import time
# driver = webdriver.PhantomJS(executable_path=r'D:\portable program\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
# print(driver.find_element_by_id('content').text)
driver.get_screenshot_as_file('a.png')
driver.close()
