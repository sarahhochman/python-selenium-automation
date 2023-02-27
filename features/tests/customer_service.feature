Feature: Customer Service Page

  Scenario: Welcome line
    Given Amazon Customer page is open
    Then Welcome heading appears


  Scenario: Icon Table
    Given Amazon Customer page is open
    Then 9 links present in table


  Scenario: Search Library
    Given Amazon Customer page is open
    Then Search Library Header

  Scenario: Search Library Field
    Given Amazon Customer page is open
    Then Search Field exists

  Scenario: All Help Topics Header
    Given Amazon Customer page is open
    Then Help header exists

  Scenario: All Help Topics list
    Given Amazon Customer page is open
    Then 11 links in help topics