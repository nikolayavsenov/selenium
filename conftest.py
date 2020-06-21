import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Remote(command_executor="http://192.168.88.238:4444/wd/hub",
                              desired_capabilities={"browserName": "firefox", "javascriptEnabled": True})
    yield driver
    driver.quit()
