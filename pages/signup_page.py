from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from browser import Browser

class SignupPage(Browser):

    SIGNUP_BUTTON = (By.CSS_SELECTOR, '.jss17.jss49')
    PERSONAL_BUTTON = (By.XPATH, '//input[@value="personal"]')
    BUSINESS_BUTTON = (By.CSS_SELECTOR, 'input[value="business"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.jss15.jss39')
    INPUT_NAME = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.MuiFormHelperText-root.MuiFormHelperText-contained.MuiFormHelperText-filled')
    BETWEEN_8AND72_CHARACTERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Between 8 and 72 characters"]')
    UPPERCASE_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Uppercase characters"]')
    LOWERCASE_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Lowercase characters"]')
    NUMBERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Numbers"]')
    SPECIAL_CHARACTERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Special characters"]')

    def click_signup_btn(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def click_personal_btn(self):
        self.driver.find_element(*self.PERSONAL_BUTTON).click()

    def clic_business(self):
        self.driver.find_element(*self.BUSINESS_BUTTON).click()


    def click_continue_btn(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(2)

    def input_first_name(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    def display_error_message(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_message == actual_message,\
            f'Error message is incorrect, expected: {expected_message}, actual: {actual_message}'

    def clear_name_input(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(Keys.BACKSPACE*len(name))
        sleep(2)

    def error_message_not_displayed(self):
        sleep(2)
        try:
            actual = self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()
            expected = False
        except NoSuchElementException:
            actual = False
            expected = False

        assert actual == expected, \
            f'Error message is displayed, actual: {actual}, expected: {expected}'

    def between_notification(self):
        sleep(2)
        expected_msg = 'Between 8 and 72 characters'
        try:
            actual_message = self.driver.find_element(*self.BETWEEN_8AND72_CHARACTERS_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message,\
            f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def uppercase_notification(self):
        sleep(2)
        expected_msg = 'Uppercase characters'
        try:
            actual_message = self.driver.find_element(*self.UPPERCASE_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message,\
            f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def lowercase_notification(self):
        sleep(2)
        expected_msg = 'Lowercase characters'
        try:
            actual_message = self.driver.find_element(*self.LOWERCASE_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message,\
            f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def numbers_notification(self):
        sleep(2)
        expected_msg = 'Numbers'
        try:
            actual_message = self.driver.find_element(*self.NUMBERS_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message,\
            f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def special_characters_notification(self):
        sleep(2)
        expected_msg = 'Special characters'
        try:
            actual_message = self.driver.find_element(*self.SPECIAL_CHARACTERS_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message,\
            f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'
