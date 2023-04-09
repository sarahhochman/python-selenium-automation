from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Product Page')
def open_product_page(context):
    context.app.drop_down_choices_page.open_product_page()


@when('Mouse over Amazon Health')
def mouse_over_amazon_health(context):
    context.app.drop_down_choices_page.mouse_over_amazon_health()

@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.drop_down_choices_page.hover_over_new_arrivals()

@then('Verify New Arrivals Appear')
def verify_new_arrivals_appear(context):
    context.app.drop_down_choices_page.verify_new_arrivals_appear()

@then('Verify One Medical Displayed')
def verify_one_medical_displayed(context):
    context.app.verify_one_medical_displayed()