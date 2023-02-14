from selenium.webdriver.common.by import By
from behave import given, when, then



@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon').click()


@then('Text says Cart is Empty')
def check_text(context):
    expected_result = 'Your Amazon Cart is empty'

    actual_result = context.actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
