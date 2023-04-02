from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class ForgotPass(Browser):

    FORGOTPASS_BUTTON = (By.XPATH, '//a[normalize-space()="Forgot password?"]')
    BACKTOLOGIN_BUTTON = (By.XPATH, '//a[normalize-space()="Back to login"]')
    INPUT_EMAIL = (By.XPATH, '//input[@placeholder="Enter your email"]')
    INVALIDEMAIL_ERROR = (By.CSS_SELECTOR, 'p')
    SENDEMAIL_BUTTON = (By.XPATH, '//button[@type="button"]')
    EMAILSENTNOTIFICATION = (By.XPATH, '//span[contains(text(),"If you have an account registered with this email ")]')

    def click_forgotPass(self):
        self.driver.find_element(*self.FORGOTPASS_BUTTON).click()
        sleep(2)

    def click_backToLogin(self):
        self.driver.find_element(*self.BACKTOLOGIN_BUTTON).click()
        sleep(2)

    def check_url(self, url):
        if url == 'https://jules.app/forgot-password':
            actual = self.driver.current_url
            expected = 'https://jules.app/forgot-password'
            assert actual == expected, f'The URL is incorrect, actual: {actual}, expected: {expected}'

        elif url == 'https://jules.app/sign-in':
            actual = self.driver.current_url
            expected = 'https://jules.app/sign-in'
            assert actual == expected, f'The URL is incorreect, actual: {actual}, expected: {expected}'

    def input_email(self, email):
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)
        sleep(1.5)

    def email_error(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.INVALIDEMAIL_ERROR).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, \
            f'Error message is incorrect, expected: {expected_message}, actual: {actual_message}'
        sleep(2)

    def send_email_enabled(self):
        actual = self.driver.find_element(*self.SENDEMAIL_BUTTON).is_enabled()
        expected = True
        assert expected == actual, f'Send email button is disabled, expected: {expected}, actual: {actual}'

    def click_sendEmailButton(self):
        self.driver.find_element(*self.SENDEMAIL_BUTTON).click()

    def email_sentNotification(self):
        actual = self.driver.find_element(*self.EMAILSENTNOTIFICATION).is_displayed()
        expected = True
        assert expected == actual, f'Notification is not displayed, expected: {expected}, actual: {actual}'
        sleep(2)