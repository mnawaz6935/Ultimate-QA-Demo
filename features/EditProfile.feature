@editprofile
Feature: Validate the edit profile feature
  Background:
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in

  Scenario: TC_01_Verify that editing use profile save the company name correctly
    Then Login with valid email and password
    Then Verify that the home page is displayed
    Then Click on the profile dropdown
    Then Click on My Account menu
    Then Generate a random string
    Then Enter the '<RandomString>' in the company field
    When Click on the Save Changes button
    Then Verify company field have same '<RandomString>' value
    Then Close the browser


    Scenario: TC_02_Verify that editing use profile save the Professional Title correctly
    Then Login with valid email and password
    Then Verify that the home page is displayed
    Then Click on the profile dropdown
    Then Click on My Account menu
    Then Generate a random professional title
    Then Enter the '<RandomString>' in the professional title field
    When Click on the Save Changes button
    Then Verify professional title field have same '<RandomString>' value
    Then Close the browser
