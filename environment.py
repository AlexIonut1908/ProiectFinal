from browser import Browser
from pages.forgotpass_page import ForgotPass
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.signup_page = SignupPage()
    context.forgotpass_page = ForgotPass()

def after_all(context):
    context.browser.close()