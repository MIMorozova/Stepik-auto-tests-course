from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x =  browser.find_element_by_id("input_value").text
    input1 =  browser.find_element_by_id("answer").send_keys(calc(x))
    button2 =  browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
