# Created by morah at 2/14/2023
Feature: Working with the Shopping Cart


  Scenario: Your Shopping Cart is empty' shown if no product added
    Given Amazon.com is open
    When Click on Cart icon
    Then Text says Cart is Empty

