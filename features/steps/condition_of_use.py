from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRIVACY_NOTICE = (By.PARTIAL_LINK_TEXT, 'Notice')
PRIVACY_NOTICE_PAGE = (By.XPATH, "//h1[contains(text(),'Privacy')]")


@when('Store original windows')
def opening_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def amazon_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.tabs = context.driver.window_handles
    context.second_window = context.tabs[1]
    context.driver.switch_to.window(context.second_window)

@then('Verify Amazon Privacy Notice page is opened')
def privacy_notice_open(context):
    expected_result = 'Amazon.com Privacy Notice'
    actual_result = context.driver.find_element(*PRIVACY_NOTICE_PAGE).text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('User can close new window and switch back to original')
def close_window(context):
    context.driver.switch_to.window(context.second_window)
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
