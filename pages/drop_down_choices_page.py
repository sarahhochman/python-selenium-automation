from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


one_medical_expected = " Get primary care in person of via video "
one_medical_item = (By.XPATH, 'p[text()="Get primary care in perso or via video"]')
amazon_health_tab = (By.XPATH, "//a[@id='nav_link_allhealthingress']")

new_arrivals_expected = "5 classes found"
new_arrivals_actual = (By.XPATH, "//div[@class='mega-menu']")


class DropDownChoices(BasePage):

    def mouse_over_amazon_health(self):
        actions = ActionChains(self.driver)

        actions.move_to_element(amazon_health_tab)
        actions.perform()

    def verify_one_medical_displayed(self):
        self.verify_item_displayed(one_medical_expected, one_medical_item)

    def open_product_page(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_over_new_arrivals(self):
        new_arrivals_tab = self.driver.find_element(By.XPATH, "//a[@aria-label='New Arrivals']")
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_tab)
        actions.perform()

    def verify_new_arrivals_appear(self):
        self.verify_items_displayed(new_arrivals_expected, new_arrivals_actual)
