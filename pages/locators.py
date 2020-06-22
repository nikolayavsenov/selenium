from selenium.webdriver.common.by import By


class LoginLocators:
    """Login locators"""
    LOCATOR_LOGIN_FIELD = (By.ID, 'identifierId')
    LOCATOR_PASSWORD_FIELD = (By.NAME, 'password')
    LOCATOR_LOGIN_BUTTON = (By.ID, 'identifierNext')
    LOCATOR_PASSWORD_BUTTON = (By.XPATH, '//*[@id="passwordNext"]/div')


class InboxLocators:
    """Inbox locators"""
    LOCATOR_TOTAL_EMAILS = (By.CSS_SELECTOR, r'#\:je > span > span.ts')
    LOCATOR_NEW_MAIL_BUTTON = (By.CSS_SELECTOR, r'#\:jl > div > div')
    LOCATOR_RECEIVER_FIELD = (By.ID, ':14a')
    LOCATOR_MAIL_SUBJECT = (By.ID, ':r1')
    LOCATOR_TEXT_AREA = (By.ID, ':sy')
    LOCATOR_SEND_EMAIL_BUTTON = (By.ID, ':mb')