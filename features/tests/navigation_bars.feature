# Created by Sarah at 2/23/2023
Feature: navigation bars


  Scenario: Five links pn top pf bestsellers page
    Given Amazon.com is open
    When Best sellers is clicked
    Then There are 5 sub links on the page
