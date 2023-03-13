from selenium.webdriver.common.by import By
from behave import given, when, then


ACCOUNT = (By.ID, 'nav-link-accountList')
SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')
ORDERS = (By.ID, "nav-orders")

@given('Amazon.com is open')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.base_page.open_url('https://www.amazon.com/')


@given('Open Amazon T&C page')
def open_amazon_TC(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Account clicked')
def click_account(context):
    context.driver.find_element(*ACCOUNT).click()


@when('Click Amazon Orders link')
def amazon_orders_link_click(context):
    context.app.base_page.click(*ORDERS)


@then('Sign in displayed')
def verify_signin(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(*SIGN_IN_TEXT).text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('email field appears')
def verify_email_field(context):
    assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f'email input not displayed'


@then('Verify Sign In page is opened')
def sign_in_page_open(context):
    context.app.base_page.verify_url_contains_query('signin')
