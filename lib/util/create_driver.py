import pytest
from selenium.webdriver import Chrome, Firefox


def get_driver_instance():
    browser = pytest.config.option.type.lower()
    if browser == 'chrome':
        driver = Chrome("./browser_server/chromedriver.exe")
    elif browser == 'firefox':
        driver = Firefox("./browser_server/geckodriver.exe")
    else:
        print("Invalid browser option.")
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://actitime.jmr.co.za/actitime/login.jsp")
    return driver
