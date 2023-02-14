# Created by morah at 2/14/2023
Feature: When I open Amazon my cart is empty


  Scenario:
    Given Amazon.com is open
    When Click on Cart icon
    Then Text says Cart is Empty