# Created by Sarah at 2/22/2023
Feature: 1 item in cart HW 4


  Scenario: Check one item in cart
    Given Amazon.com is open
    When input table into search field
    And Click on search icon
    And price is clicked
    And add to cart is clicked
    Then Verify 1 item in cart
