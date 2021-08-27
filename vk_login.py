import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#  автологин на VK написанный мной в учебных целях 05.12.2019

def test_login_VK(driver):
    driver.get("https://vk.com/") #переход на страницу VK

    login = driver.find_element_by_id("index_email")                    # поиск поля логина
    login.send_keys("8**********")                                      # ввод логина в соответствующее поле

    password = driver.find_element_by_id("index_pass")                  # поиск поля пароля
    password.send_keys("******")                                        # ввод пароля в соответствующее поле

    login_button = driver.find_element_by_id("index_login_button")      # поиск кнопки логина
    login_button.click()                                                # клик на кнопку логина
    wait = WebDriverWait(driver, 10)                                    # ожидание выполения
    wait.until(expected_conditions.url_to_be("https://vk.com/feed"))    # ожидание редиректа на vk.com/feed

    msg_button = driver.find_element_by_xpath("//*[@id='l_msg']")       # поиск кнопки Сообщения
    msg_button.click()                                                  # клик на кнопку Сообщения
    wait = WebDriverWait(driver, 10)                                    # ожидание выполения
    wait.until(expected_conditions.url_to_be("https://vk.com/im"))      # ожидание редиректа на vk.com/im

    search_dialog = driver.find_element_by_id("im_dialogs_search")      # поиск поля Поиска по диалогам
    search_dialog.send_keys("***************", Keys.ENTER)              # Поиск имени пользователя в диалогах

    message = driver.find_element_by_id("im_editable0")                 # поиск поля ввода тестового сообщения
    message.send_keys("*****привет! Я наконец-то допилил программу которая способна сама написать тебе вот это сообщение по нажатию всего одной кнопки!)", Keys.ENTER)
    time.sleep(100)

