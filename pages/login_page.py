from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from browser import Browser



class LoginPage(Browser):

    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained"]')
    ERROR_MESSAGE_EMAIL = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')


    def go_to_login_page(self):
        self.driver.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def empty_password(self):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('5')
        sleep(1)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(Keys.BACKSPACE)
        sleep(2)

    def empty_email(self):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys('a')
        sleep(1)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(Keys.BACKSPACE)
        sleep(2)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def error_message_password(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_PASSWORD).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_message == actual_message, \
            f' Error message is incorrect, expected {expected_message}, actual {actual_message}'

    def error_message_email(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_EMAIL).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, \
            f' Error message is incorrect, expected {expected_message}, actual {actual_message}'

    def login_button_disabled(self):
        sleep(2)
        actual = self.driver.find_element(*self.LOGIN_BUTTON).is_enabled()
        expected = False
        assert expected == actual, \
            f'Login button is working, expected {expected}, actual {actual}'

    def login_button_enabled(self):
        sleep(2)
        actual = self.driver.find_element(*self.LOGIN_BUTTON).is_enabled()
        expected = True
        assert expected == actual, \
            f'Login button is not working, expected {expected}, actual {actual}'