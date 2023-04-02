from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from browser import Browser

class SignupPage(Browser):

    SIGNUP_BUTTON = (By.XPATH, '//a[normalize-space()="Sign up."]')
    PERSONAL_BUTTON = (By.XPATH, '//input[@value="personal"]')
    BUSINESS_BUTTON = (By.XPATH, '//input[@value="business"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[normalize-space()="CONTINUE"]')
    INPUT_NAME = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'p')
    BETWEEN_8AND72_CHARACTERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Between 8 and 72 characters"]')
    UPPERCASE_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Uppercase characters"]')
    LOWERCASE_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Lowercase characters"]')
    NUMBERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Numbers"]')
    SPECIAL_CHARACTERS_NOTIFICATION = (By.XPATH, '//span[normalize-space()="Special characters"]')

    def click_signup(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def click_personal(self):
        self.driver.find_element(*self.PERSONAL_BUTTON).click()

    def click_business(self):
        self.driver.find_element(*self.BUSINESS_BUTTON).click()


    def click_continue1(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(2)

    def set_firstName(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    def display_error(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, \
            f'Error message is incorrect, expected: {expected_message}, actual: {actual_message}'
        sleep(2)

    def clear_nameInput(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(Keys.BACKSPACE*len(name))
        sleep(2)

    def error_notDisplayed(self):
        sleep(1)
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
