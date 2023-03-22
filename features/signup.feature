Feature: Check the signup functionality

  Background:
    Given login: I am an user on the login page

  @test6
  Scenario: I am trying to create a "personal" account on the page with a wrong email, then a correct email.
    When base: I click the "Sign up." button
    When signup: I click on "PERSONAL"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Alexandru"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Gheorghe"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Ionut"
    Then signup: Error message is displayed with the error message: Please enter a valid email address.
    When signup: I clear the name input which was "Ionut"
    When signup: I fill the name input with value "ionut.alexandru1908@gmail.com"
    Then signup: Error message is not displayed anymore

  @test7
  Scenario: I am trying to create a "personal" account and verify the password requirements
    When base: I click the "Sign up." button
    When signup: I click on "PERSONAL" button
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "Alexandru"
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "Gheorghe"
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "ionut.alexandru1908@gmail.com"
    When signup: I click on "Continue" button
    Then signup: Between 8 and 72 characters notification is displayed
    Then signup: Uppercase characters notification is displayed
    Then signup: Lowercase characters notification is displayed
    Then signup: Numbers notification is displayed
    Then signup: Special characters notification is displayed

  @test8
  Scenario: I am trying to create a "business" account and verify the password requirements
    When base: I click the "Sign up." button
    When signup: I click on "BUSINESS" button
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "AlexIonut"
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "Alexandru"
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "Gheorghe"
    When signup: I click on "Continue" button
    When signup: I fill the name input with value "ionut.alexandru1908@gmail.com"
    When signup: I click on "Continue" button
    Then signup: Between 8 and 72 characters notification is displayed
    Then signup: Uppercase characters notification is displayed
    Then signup: Lowercase characters notification is displayed
    Then signup: Numbers notification is displayed
    Then signup: Special characters notification is displayed