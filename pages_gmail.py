from base_gmail import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Locators:
    """Locators"""
    LOCATOR_LOGIN_FIELD = (By.ID, 'identifierId')
    LOCATOR_PASSWORD_FIELD = (By.CLASS_NAME, 'whsOnd')
    LOCATOR_TOTAL_EMAILS = (By.CSS_SELECTOR, '#\:je > span > span.ts')
    LOCATOR_NEW_MAIL_BUTTON = (By.CSS_SELECTOR, '#\:jl > div > div')
    LOCATOR_RECEIVER_FIELD = (By.ID, ':14a')
    LOCATOR_MAIL_SUBJECT = (By.ID, ':r1')
    LOCATOR_TEXT_AREA = (By.ID, ':sy')
    LOCATOR_SEND_EMAIL_BUTTON = (By.ID, ':mb')


class GmailLogin(BasePage):
    """Login into Gmail"""
    def enter_login(self, login):
        login_field = self.find_element(Locators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(login+Keys.ENTER)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(Locators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password+Keys.ENTER)
        return password_field


class MailboxActions(BasePage):
    """Actions in mailbox:getting total email, send email, etc"""
    def get_total_emails(self):
        total_emails = self.find_element(Locators.LOCATOR_TOTAL_EMAILS)
        return total_emails

    def send_email(self, receiver, subject, text):
        self.find_element(Locators.LOCATOR_NEW_MAIL_BUTTON).click()
        email_receiver = self.find_element(Locators.LOCATOR_RECEIVER_FIELD).send_keys(receiver)
        email_subject = self.find_element(Locators.LOCATOR_MAIL_SUBJECT).send_keys(subject)
        email_text = self.find_element(Locators.LOCATOR_TEXT_AREA).send_keys(text)
        self.find_element(Locators.LOCATOR_SEND_EMAIL_BUTTON).click()
        return email_receiver, email_subject, email_text
