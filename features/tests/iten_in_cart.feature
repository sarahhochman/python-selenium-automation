# Created by morah at 2/14/2023
Feature: purchasing an item

  Scenario: when item in chosen it appears in cart
    Given Amazon.com is open
    When Input bear into search field
    And Click on search icon
    And price is clicked
    And add to cart is clicked
    And Click on Cart icon
    Then proceed to checkout