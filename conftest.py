import pytest
from selenium import webdriver
from settings import HUB


@pytest.fixture
def browser():
    driver = webdriver.Remote(command_executor=HUB,
                              desired_capabilities={"browserName": "firefox", "javascriptEnabled": True})
    yield driver
    driver.quit()
