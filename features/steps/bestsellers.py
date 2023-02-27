from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLER = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
BEST_SELLER_SUB_LINKS = (By.CSS_SELECTOR, "div[class*='nav-tab-all_style_zg-tabs-li']")

@when('Best sellers is clicked')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLER).click()


@then('There are 5 sub links on the page')
def five_links(context):
    sub_links = context.driver.find_elements(*BEST_SELLER_SUB_LINKS)
    print(sub_links)
    print(len(sub_links))
    expected_amount=5
    actual_amount = len(sub_links)
    assert expected_amount == actual_amount, f'expected {expected_amount} but got {actual_amount}'
