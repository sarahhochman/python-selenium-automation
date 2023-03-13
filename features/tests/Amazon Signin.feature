# Created by morah at 2/14/2023
Feature: Amazon Sign in page opens

  Scenario: When click on Sign in, under accounts, Sign in page opens
    Given Amazon.com is open
    When Account clicked
    Then Sign in displayed
    Then email field appears

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Amazon.com is open
    When Click Amazon Orders link
    Then Verify Sign In page is opened