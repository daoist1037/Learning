import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://pass.hust.edu.cn/cas/login?service=https%3A%2F%2Fyqtb.hust.edu.cn%2Finfoplus%2Flogin%3FretUrl%3Dhttps%253A%252F%252Fyqtb.hust.edu.cn%252Finfoplus%252Fform%252FBKS%252Fstart')

try:
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type ='text']")))
except Exception as _:
    print('zeor too late!')

text = browser.find_element_by_xpath("//input[@type ='text']")
text.send_keys(' ')
passwd = browser.find_element_by_xpath("//input[@type ='password']")
passwd.send_keys(' ')
button = browser.find_element_by_xpath("//input[@type ='button']")
button.click()

try:
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@class ='command_button_content']")))
except Exception as _:
    print('first too late!')

command_button_content = browser.find_element_by_xpath(
    "//a[@class ='command_button_content']")
time.sleep(1)
command_button_content.click()

""" try:
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//input[@name ='fieldXSZLB']")))
except Exception as _:
    print('second too late!') """
# 上一步失败的原因：页面源码已经获取，但是网页仍然没有加载到位；所以获得了元素，但是无法send_keys()
time.sleep(7)
text = browser.find_element_by_xpath("//input[@id ='V1_CTRL164']")

text.send_keys('36.9')
command_button_content = browser.find_element_by_xpath(
    "//ul/li/a/nobr[text()='提交 Submit']/..")
time.sleep(3)
command_button_content.click()
time.sleep(2)
dialog_button_default_fr = browser.find_element_by_xpath(
    "//button[@class='dialog_button default fr']")
dialog_button_default_fr.click()
time.sleep(2)
dialog_button_default_fr = browser.find_element_by_xpath(
    "//button[@class='dialog_button default fr']")
dialog_button_default_fr.click()
time.sleep(3)
