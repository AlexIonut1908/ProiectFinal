from browser import Browser
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.signup_page = SignupPage()

def after_all(context):
    context.browser.close()