from pages.base_page import BasePage
from pages.create_customer_acccount_page import CreateCustomerAccountPage
from pages.remind_login_page import RemindLoginPage
from pages.remind_password_page import RemindPasswordPage
from pages.log_in_page import LogInPage
from pages.search_result_page import SearchResultPage
from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_LINK = (By.ID, "rej12")
    REMIND_LOGIN = (By.LINK_TEXT, "Zapomniałem loginu")
    REMIND_PASSWORD = (By.LINK_TEXT, "Zapomniałem hasła")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button[name='ok']")
    AUTO_LOGIN_CHECKBOX = (By.XPATH, "input[@id='autolog']")
    USER_LOGIN = (By.CSS_SELECTOR, "input[placeholder='użytkownik']")
    USER_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='hasło']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='inp_search']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Szukaj']")

class HomePage(BasePage):
    """
    Landing Page object
    """
    def click_sign_in(self):
        """
        Click SignIn link and returns CreateCustomerAccountPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # Kliknąć w ten element
        el.click()
        # Zwróć nową stronę
        return CreateCustomerAccountPage(self.driver)

    def remind_login(self):
        """
        Click Remind Login link and returns RemindLoginPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.REMIND_LOGIN)
        # Kliknąć element
        el.click()
        # Zwróć nową stronę
        return  RemindLoginPage(self.driver)

    def remind_password(self):
        """
        Click Remind Password link and returns RemindLoginPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.REMIND_PASSWORD)
        # Kliknąć element
        el.click()
        # Zwróć nową stronę
        return RemindPasswordPage(self.driver)

    def click_log_in(self):
        """
        Click Log In button and returns LogInPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.LOG_IN_BUTTON)
        # Kliknąć element
        el.click()
        # Zwróć nową stronę
        return LogInPage(self.driver)

    def click_search_button(self):
        """
        Click Search button and returns SearchResultsPage instance
        """
        # Odszukaj element
        el = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        # Kliknąć element
        el.click()
        # Zwróć nową stronę
        return SearchResultPage(self.driver)