from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    #search = context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    #search.send_keys(search_word)
    #sleep(4)
    context.app.base_page.input_text(search_word, *SEARCH_INPUT)


@when('Click on search icon')
def click_search_icon(context):
    #context.driver.find_element(*SEARCH_SUBMIT).click()
    #sleep(1)
    context.app.base_page.click(*SEARCH_SUBMIT)

@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"