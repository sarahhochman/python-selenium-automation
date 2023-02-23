from selenium.webdriver.common.by import By
from behave import when, then


PRODUCT_PRICE = (By.CSS_SELECTOR, "span.a-price-whole")
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART_COUNT =(By.ID, 'add-to-cart-button')
GO_TO_CHECKOUT = (By.CSS_SELECTOR, "input[name=proceedToRetailCheckout]")


@when('price is clicked')
def price_clicked(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('add to cart is clicked')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()


@then('Verify {number} item in cart')
def verify_number_in_cart(context, number):
    actual_result=context.driver.find_element(*CART_COUNT).text
    assert number == actual_result, f'(expect {number} got {actual_result})'


@then('proceed to checkout')
def checkout(context):
    assert context.driver.find_element(*GO_TO_CHECKOUT).is_displayed(), f'checkout button does not appear'
    print('Test passed!')