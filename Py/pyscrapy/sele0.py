from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import time
# chrome_driver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' 
# dr = webdriver.Chrome(executable_path=chrome_driver)
# dr.get('http://exercise.kingname.info/exercise_ajax_3.html')
# time.sleep(3)
# hetml = dr.page_source
# print(hetml)

# import requests
# html = requests.get('http://exercise.kingname.info/exercise_ajax_3.html')
# print(html.text)
dr = webdriver.Chrome()
dr.get('http://exercise.kingname.info/exercise_ajax_3.html')
try:
    WebDriverWait(dr,30).until(EC.text_to_be_present_in_element((By.CLASS_NAME,'content'),'不错'))
except Exception as _:
    print('It is too late')
print(dr.page_source)
dr.quit()