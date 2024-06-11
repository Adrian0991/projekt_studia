from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='inp_search']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Szukaj']")
    SEARCH_RESULTS = (By.XPATH, "//div[@class='holder']")
    USER_ERROR_MESSAGES = (By.XPATH, '//div[@class="warn"]')
class SearchResultPage(BasePage):
    def enter_words(self, word):
        """
        Enters login
        """
        el = self.driver.find_element(*SearchPageLocators.SEARCH_FIELD)
        el.send_keys(word)

    def click_search_btn(self):
        """
        Click search button and go to search results page
        """
        self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON).click()

    def get_search_results(self):
        """
        Checking return image attributes form search result page
        """
        results = self.driver.find_elements(*SearchPageLocators.SEARCH_RESULTS)
        img_attributes = []

        for result in results:
            img_src = result.get_attribute('src')
            img_alt = result.get_attribute('alt')
            img_attributes.append({'src': img_src, 'alt': img_alt})
        return img_attributes

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*SearchPageLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts