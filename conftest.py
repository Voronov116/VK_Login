import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """
    Инициализация веб-драйвера
    """
    remote_host = os.getenv("SELENIUM_HOST", None)
    if remote_host:
        chrome_options = webdriver.ChromeOptions()
        #   Запуск хрома без GUI
        chrome_options.add_argument("--headless")
        #
        chrome_options.add_argument("--no-sandbox")
        # Хром запускаеться одним процессом
        chrome_options.add_argument("--single-process")
        # отключить SHM
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--windows-size=1920,1080")
        driver = webdriver.Remote(remote_host, desired_capabilities=chrome_options.to_capabilities())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield driver  #  Возвращаем веб драйвер для работы в тестах
    driver.quit()   #  Завершаем работу веб драйвера