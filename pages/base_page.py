from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep

class BasePage(Browser):
    SIGN_IN_URL = 'https://jules.app/sign-in'
    SIGN_UP_URL = 'https://jules.app/sign-up'
    SIGN_UP_BUTTON = (By.XPATH, '//a[normalize-space()="Sign up."]')
    LOG_IN_BUTTON = (By.XPATH, '//span[normalize-space()="Log In."]')

    def click_button(self, button):
        sleep(2)
        if button == "Sign up.":
            self.driver.find_element(*self.SIGN_UP_BUTTON).click()
        elif button == "Log in.":
            self.driver.find_element(*self.LOG_IN_BUTTON).click()

    def check_url(self, url):
        if url == self.SIGN_UP_URL:
            actual = self.driver.current_url
            expected = self.SIGN_UP_URL
            assert actual == expected, \
                f'The current URL is wrong, actual: {actual}, expected: {expected}'

        elif url == self.SIGN_IN_URL:
            actual = self.driver.current_url
            expected = self.SIGN_IN_URL
            assert actual == expected, \
                f'The current URL is wrong, actual: {actual}, expected: {expected}'