from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Amazon.com is open')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Account clicked')
def click_account(context):
    context.driver.find_element(By.ID, 'nav-link-accountList').click()


@then('Sign in displayed')
def verify_signin(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('email field appears')
def verify_email_field(context):
    assert context.driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed(), f'email input not displayed'