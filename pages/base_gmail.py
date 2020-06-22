from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import LOGIN_URL


class BasePage:
    """Base class"""
    def __init__(self, driver):
        self.driver = driver
        self.login_url = LOGIN_URL

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def to_site(self):
        return self.driver.get(self.login_url)
