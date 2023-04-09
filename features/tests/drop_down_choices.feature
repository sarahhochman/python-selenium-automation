# Created by Sarah at 3/17/2023
Feature: how to use drop down menus

  Scenario: Find Health Options
    Given Amazon.com is open
    When Mouse over Amazon Health
    Then Verify One Medical Displayed


  Scenario: Find Deals
    Given Open Product Page
    When Hover over New Arrivals
    Then Verify New Arrivals Appear