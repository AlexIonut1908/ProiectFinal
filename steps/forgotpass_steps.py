from behave import *

@when('forgotpass: I click the "Forgot password?" button')
def step_impl(context):
    context.forgotpass_page.click_forgotPass()

@when('forgotpass: I click the "Back to login" button')
def step_impl(context):
    context.forgotpass_page.click_backToLogin()

@when('forgotpass: I click the "SEND EMAIL" button')
def step_impl(context):
    context.forgotpass_page.click_sendEmailButton()

@when('forgotpass: I fill the email slot with value: "{email}"')
def step_implt(context, email):
    context.forgotpass_page.input_email(email)

@then('forgotpass: The URL is: "{url}"')
def step_impl(context, url):
    context.forgotpass_page.check_url(url)

@then('forgotpass: Error message is displayed with the error message "{expected_message}"')
def step_impl(context, expected_message):
    context.forgotpass_page.email_error(expected_message)

@then('forgotpass: Send email button is enabled')
def step_impl(context):
    context.forgotpass_page.send_email_enabled()

@then('forgotpass: Email sent notification is displayed')
def step_impl(context):
    context.forgotpass_page.email_sentNotification()