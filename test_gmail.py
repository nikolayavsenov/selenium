from allure_commons.types import AttachmentType
from pages_gmail import GmailLogin, MailboxActions
from conftest import browser
import time
import allure

RECEIVER_EMAIL = 'valiahmetov.farit@gmail.com'
EMAIL_SUBJECT = 'Тестовое задание. Долгоаршинных.'
EMAIL_TEXT = 'Найдено {} писем'
LOGIN = 'avsenov.nikolay@gmail.com'
PASSWORD = '123456'


@allure.feature('Test gmail')
@allure.story('Test for gmail')
def test_google_mail(browser):
    gmail_login = GmailLogin(browser)
    gmail_login.to_site()
    with allure.step('Screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='login_page', attachment_type=AttachmentType.PNG)
    gmail_login.enter_login(LOGIN)
    time.sleep(1)
    gmail_login.enter_password(PASSWORD)
    inbox_actions = MailboxActions(browser)
    total_emails = inbox_actions.get_total_emails()
    send_mail = inbox_actions.send_email(
        RECEIVER_EMAIL,
        EMAIL_SUBJECT,
        EMAIL_TEXT.format(total_emails)
    )
    assert True
