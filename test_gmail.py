from pages.pages_gmail import GmailLogin, MailboxActions
import allure
from settings import LOGIN, PASSWORD, RECEIVER_EMAIL, EMAIL_SUBJECT, EMAIL_TEXT


@allure.feature('Test gmail')
@allure.story('Test for gmail')
def test_google_mail(browser):
    gmail_login = GmailLogin(browser)
    gmail_login.to_site()
    gmail_login.enter_login(LOGIN)
    gmail_login.enter_password(PASSWORD)
    inbox_actions = MailboxActions(browser)
    total_emails = inbox_actions.get_total_emails()
    inbox_actions.send_email(
        RECEIVER_EMAIL,
        EMAIL_SUBJECT,
        EMAIL_TEXT.format(total_emails)
    )
    assert True

