from behave import *

@given('login: I am an user on the login page')
def step_impl(context):
    context.login_page.go_to_login_page()

@when('login: I fill the email slot with value "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I fill the password slot with value "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('login: I leave the password slot empty')
def step_impl(context):
    context.login_page.empty_password()

@when('login: I leave the email slot empty')
def step_impl(context):
    context.login_page.empty_email()

@then('login: Error message is displayed with the message: {error_message}')
def step_impl(context, error_message):
    if error_message == 'Please enter a valid email address!':
        context.login_page.display_error_message_username(error_message)
    elif error_message == 'Please enter your password!':
        context.login_page.display_error_message_password(error_message)

@then('login: Login button is disabled')
def step_impl(context):
    context.login_page.login_button_disabled()

@then('login: Login button is enabled')
def step_impl(context):
    context.login_page.login_button_enabled()
