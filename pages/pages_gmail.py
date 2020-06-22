from pages.base_gmail import BasePage
from pages.locators import LoginLocators, InboxLocators


class GmailLogin(BasePage):
    """Login into Gmail"""
    def enter_login(self, login):
        login_field = self.find_element(LoginLocators.LOCATOR_LOGIN_FIELD)
        login_field.send_keys(login)
        self.find_element(LoginLocators.LOCATOR_LOGIN_BUTTON).click()

    def enter_password(self, password):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        self.find_element(LoginLocators.LOCATOR_PASSWORD_BUTTON).click()


class MailboxActions(BasePage):
    """Actions in mailbox:getting total email, send email, etc"""
    def get_total_emails(self):
        total_emails = self.find_element(InboxLocators.LOCATOR_TOTAL_EMAILS)
        return total_emails

    def send_email(self, receiver, subject, text):
        self.find_element(InboxLocators.LOCATOR_NEW_MAIL_BUTTON).click()
        self.find_element(InboxLocators.LOCATOR_RECEIVER_FIELD).send_keys(receiver)
        self.find_element(InboxLocators.LOCATOR_MAIL_SUBJECT).send_keys(subject)
        self.find_element(InboxLocators.LOCATOR_TEXT_AREA).send_keys(text)
        self.find_element(InboxLocators.LOCATOR_SEND_EMAIL_BUTTON).click()
