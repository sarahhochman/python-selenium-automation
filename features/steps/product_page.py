from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

IMAGE_ICONS = (By.CSS_SELECTOR, "button.a-button-text")
IMAGE_COLOR = (By.CSS_SELECTOR, "div#variation_color_name div.a-row span.selection")


@given('open umbrella product page')
def umbrella_page(context):
    context.driver.get('https://www.amazon.com/StrombergBrand-Spectrum-Umbrella-Most-Popular-Style-Automatic/dp/B016UZ7GGE/ref=sr_1_7?crid=1VQG7YH1L9RP2&keywords=umbrella&qid=1677549753&sprefix=um%2Caps%2C223&sr=8-7&th=1')


@when('images as clickable')
def image_clickable(context):
    context.link_images = context.driver.find_elements(*IMAGE_ICONS)


@then('clicked images are correct colors')
def check_image_colors(context):
    expected_image_colors = ['(Black)', '(Black/white)', '(Burgundy)', '(Burgundy/White)', '(Carolina Blue)']
    actual_image_colors = []
    for image in context.link_images[:5]:
        image.click()
        context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#variation_color_name div.a-row span.selection")),message="icons not clickable")
        current_color = context.driver.find_element(*IMAGE_COLOR).text
        actual_image_colors += [current_color]
    assert actual_image_colors == expected_image_colors, f'expected {expected_image_colors} but got {actual_image_colors}'