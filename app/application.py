#from pages.main_page import MainPage
#from pages.header import Header
#from pages.search_results_page import SearchResultsPage

from pages.base_page import BasePage
from pages.drop_down_choices_page import DropDownChoices


class Application:

    def __init__(self, driver):
        self.driver = driver
        #self.main_page = MainPage(self.driver)
        #self.header = Header(self.driver)
        #self.search_results_page = SearchResultsPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.drop_down_choices_page = DropDownChoices(self.driver)