from selenium.webdriver.common.by import By
from behave import given, when, then


WELCOMECS = (By.CSS_SELECTOR, "h1.fs-heading.bolded")
CUSTOMER_SERVICE_TABLE_LINKS = (By.CSS_SELECTOR, 'div.issue-card-wrapper')
LIBRARY_HEADER = (By.CSS_SELECTOR, "label h2.fs-heading.bolded")
LIBRARY_SEARCH_FIELD = (By.ID, "hubHelpSearchInput")
HELP_TOPICS = (By.CSS_SELECTOR, "div#hub-gateway-app-unauth>div>div>h2.fs-heading")
HELP_TOPICS_LIST = (By.CSS_SELECTOR, "li.help-topics")

@given ('Amazon Customer page is open')
def open_cus_page(context):
    context.driver.get("https://www.amazon.com/hz/contact-us?ref_=nav_AccountFlyout_CS")


@then ('9 links present in table')
def table_links(context):
    table_links = context.driver.find_elements(*CUSTOMER_SERVICE_TABLE_LINKS)
    expected_amount = 9
    actual_amount = len(table_links)
    assert expected_amount == actual_amount, f'expected {expected_amount} but got {actual_amount}'


@then ('Search Library Header')
def library_header(context):
    expected_result = 'Search our help library'
    actual_result = context.driver.find_element(*LIBRARY_HEADER).text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then ('Search Field exists')
def lib_search_field(context):
    assert context.driver.find_element(*LIBRARY_SEARCH_FIELD).is_displayed(), f'library search field not displayed'


@then ('Help header exists')
def help_header(context):
    expected_result = 'All help topics'
    actual_result = context.driver.find_element(*HELP_TOPICS).text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then ('11 links in help topics')
def links_in_help_topics(context):
    list_of_links = context.driver.find_elements(*HELP_TOPICS_LIST)
    expected_amount = 11
    actual_amount = len(list_of_links)
    assert expected_amount == actual_amount, f'expected {expected_amount} but got {actual_amount}'


@then("Welcome heading appears")
def welcome_heading(context):
    expected_result = 'Welcome to Amazon Customer Service'
    actual_result = context.driver.find_element(*WELCOMECS).text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
