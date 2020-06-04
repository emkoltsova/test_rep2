from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_id("button")
    #Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()