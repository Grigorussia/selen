import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import re
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")  #  проверка в течение 15 секунд каждые 500 мс + когда цена станет $100
    )
book = browser.find_element(By.ID, "book")
book.click()
x_element = browser.find_element(By.ID, 'input_value')  # нахождение селектора элемента, который содержит X
x = x_element.text  # получаем текстовое значение этого элемента
z = calc(x)  # подставляем значение x в функцию calc()
input = browser.find_element(By.ID, 'answer')
input.send_keys(z)
button = browser.find_element(By.ID, "solve")
button.click()

alert = browser.switch_to.alert
alert_text = alert.text
text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
print(text)
time.sleep(11)
browser.quit
# dfdf




