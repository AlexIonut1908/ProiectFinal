from behave import *

@when('signup: I click on "PERSONAL" button')
def step_impl(context):
    context.signup_page.click_personal_btn()

@when('signup: I click on "Continue" button')
def step_impl(context):
    context.signup_page.click_continue_btn()

@when('signup: I fill the name input with value "{name}"')
def step_impl(context, name):
    context.signup_page.input_first_name(name)

@then('signup: Error message is displayed with the error message: {error_message}')
def step_impl(context, error_message):
    context.signup_page.display_error_message(error_message)

@when('signup: I clear the name input which was "{name}"')
def step_impl(context, name):
    context.signup_page.clear_name_input(name)

@when('signup: I click on "BUSINESS" button')
def step_impl(context):
    context.signup_page.click_business_button()

@then('signup: Error message is not displayed anymore')
def step_impl(context):
    context.signup_page.error_message_not_displayed()

@then('signup: Continue button is disabled')
def step_impl(context):
    context.signup_page.cotinue_button_enabled()

@then('signup: Between 8 and 72 characters notification is displayed')
def step_impl(context):
    context.signup_page.between_notification()

@then('signup: Uppercase characters notification is displayed')
def step_impl(context):
    context.signup_page.uppercase_notification()

@then('signup: Lowercase characters notification is displayed')
def step_impl(context):
    context.signup_page.lowercase_notification()

@then('signup: Numbers notification is displayed')
def step_impl(context):
    context.signup_page.numbers_notification()

@then('signup: Special characters notification is displayed')
def step_impl(context):
    context.signup_page.special_notification()