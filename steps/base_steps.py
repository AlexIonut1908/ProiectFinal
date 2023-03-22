from behave import *

@when('base: I click the "{button}"')
def step_impl(context, button):
    context.base_page.click_button(button)

@then('base: The url is: "{url}"')
def step_impl(context, url):
    context.base_page.check_url(url)