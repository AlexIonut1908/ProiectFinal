Feature: Check the login functionality

  Background:
    Given login: I am an user on the login page
  @test1
  Scenario: Try to login with email only
    When login: I fill the email slot with value "ionut.alexandru1908@gmail.com"
    When login: I leave the password slot empty
    Then login: Error message is displayed with the message: "Please enter your password!"
    Then login: Login button is disabled

  @test2
  Scenario: Try to login with password only
    When login: I fill the password slot with value "1908"
    When login: I leave the email slot empty
    Then login: Error message is displayed with the message: "Please enter a valid email address!"
    Then login: Login button is disabled

  @test3
  Scenario: Login without filling the email or password slot
    When login: I leave the email slot empty
    When login: I leave the password slot empty
    Then login: Error message is displayed with the message: "Please enter a valid email address!"
    Then login: Error message is displayed with the message: "Please enter your password!"
    Then login: Login button is disabled

  @test4
  Scenario: Login with correct credentials, but unregistered on the website
    When login: I fill the email slot with value "ionut.alexandru1908@gmail.com"
    When login: I fill the password slot with value "1908"
    Then login: Login button is enabled
