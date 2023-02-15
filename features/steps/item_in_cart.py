from selenium.webdriver.common.by import By
from behave import when, then


@when('Input bear into search field')
def input_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('bear')


@when('Click on search icon')
def search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()


@when('price is clicked')
def price_clicked(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").click()



@when('add to cart is clicked')
def add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@then('proceed to checkout')
def checkout(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '.a-button-input[name=proceedToRetailCheckout]').is_displayed(), f'checkout button does not appear'
    print('Test passed!')