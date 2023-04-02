Feature: Check the forgot password functionality

  Background:
    Given login: I am an user on the login page

  @test8
  Scenario: I click the "Forgot password?" button, then I click "Back to login" button
    When forgotpass: I click the "Forgot password?" button
    Then forgotpass: The URL is: "{url}"
    When forgotpass: I click the "Back to login" button
    Then forgotpass: The URL is: "{url}"

  @test9
  Scenario: I click the "Forgot password?" button, then I input an invalid email address
    When forgotpass: I click the "Forgot password?" button
    When forgotpass: I fill the email slot with value: "Ionut"
    Then forgotpass: Error message is displayed with the error message "Please enter a valid email address!"

  @test10
  Scenario: I click the "Forgot password?" button, then I input an valid email address and click "SEND EMAIL" button
    When forgotpass: I click the "Forgot password?" button
    When forgotpass: I fill the email slot with value: "ionut.alexandru1908@gmail.com"
    Then forgotpass: Send email button is enabled
    When forgotpass: I click the "Send email" button
    Then forgotpass: Email sent notification is displayed