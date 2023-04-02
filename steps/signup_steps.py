from behave import *

@when('base: I click the "Sign up." button')
def step_impl(context):
    context.signup_page.click_signup()
@when('signup: I click on "PERSONAL" button')
def step_impl(context):
    context.signup_page.click_personal()

@when('signup: I click on "Continue" button')
def step_impl(context):
    context.signup_page.click_continue1()

@when('signup: I fill the name input with value "{name}"')
def step_impl(context, name):
    context.signup_page.set_firstName(name)

@then('signup: Error message is displayed with the error message "{expected_message}"')
def step_impl(context, expected_message):
    context.signup_page.display_error(expected_message)

@when('signup: I clear the name input which was "{name}"')
def step_impl(context, name):
    context.signup_page.clear_nameInput(name)

@when('signup: I click on "BUSINESS" button')
def step_impl(context):
    context.signup_page.click_business()

@then('signup: Error message is not displayed anymore')
def step_impl(context):
    context.signup_page.error_notDisplayed()

@then('signup: Continue button is disabled')
def step_impl(context):
    context.signup_page.continue_buttonEnabled()

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
    context.signup_page.special_characters_notification()
