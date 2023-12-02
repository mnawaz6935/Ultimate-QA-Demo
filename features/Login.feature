@login
Feature: Validate the login feature
  Background:
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in

  Scenario: TC_01 able to enter email in field
      Then Enter email in text field
      Then Verify that the email field is displaying a value
      Then Close the browser

  Scenario: TC_02_Verify email text field is not accepting double dots consecutively
      Then Enter email "123a..bc@yopmail.com" in text field
      Then Verify that the email field is displaying a value
      Then Close the browser

   Scenario: TC_03 Verify that user is able to able to enter password in field
      Then Enter password "45dasfasf" in password text field
      Then Verify that the password field is displaying a value
      Then Close the browser

  Scenario: TC_04 Verify that the Remember me checkbox is checked on mouse click
      Then click on remember me checkbox and verify remember me checkbox is checked
      Then Close the browser

  Scenario: TC_05 Verify that the Remember me checkbox is unchecked on mouse click
      Then click on remember me checkbox and verify remember me checkbox is unchecked
      Then Close the browser

  Scenario: TC_06 Verify that the Forgot password button is working
      Then click on forgot password button
      Then Verify that the forgot page is displayed
      Then Close the browser

  Scenario: TC_07 Verify that Create an Account link is working
      Then click on create an account link
      Then Verify that the create an account page is displayed
      Then Close the browser

  Scenario: TC_08 Verify that user is not able to login with valid credentials
      Then Login with invalid email and password
      Then Verify that the home page is displayed
      Then Close the browser

  Scenario: TC_09 Verify that user is able to login with valid credentials
    Then Login with valid email and password
    Then Verify that the home page is displayed
    Then Close the browser