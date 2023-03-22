Feature: Check URL changing functionality

  Background:
    Given login: I am an user on the login page

  @test5
  Scenario: I click the "Sign up" button, then I click the "Sign in" button
    When base: I click the "Sign up." button
    Then base: The url is: "https://jules.app/sign-up"
    When base: I click the "Log in." button
    Then base: The url is: "https://jules.app/sign-in"
