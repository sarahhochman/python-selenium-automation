# Created by Sarah at 2/23/2023
Feature: navigation bars


  Scenario: Five links on top of bestsellers page
    Given Amazon.com is open
    When Best sellers is clicked
    Then There are 5 sub links on the page


  Scenario:  Five links on top of bestsellers page work
    Given Best sellers page is open
    When Best sellers is clicked
    Then Link clicked correct page displayed
