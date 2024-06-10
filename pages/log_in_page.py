from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LogInLocators:
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button[name='ok']")
    AUTO_LOGIN_CHECKBOX = (By.XPATH, "//input[@id='autolog']")
    USER_LOGIN = (By.CSS_SELECTOR, "input[placeholder='użytkownik']")
    USER_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='hasło']")
    USER_ERROR_MESSAGES = (By.XPATH, "//div[@class='warn']")
    LOG_OUT_LINK = (By.XPATH, "//a[normalize-space()='Wyloguj']")

class LogInPage(BasePage):
    def enter_login(self, login):
        """
        Enters login
        """
        el = self.driver.find_element(*LogInLocators.USER_LOGIN)
        el.send_keys(login)

    def enter_password(self, password):
        el = self.driver.find_element(*LogInLocators.USER_PASSWORD)
        el.send_keys(password)

    def click_on_checkbox_auto_log_in(self):
        self.driver.find_element(*LogInLocators.AUTO_LOGIN_CHECKBOX).click()

    def click_log_in_btn(self):
        self.driver.find_element(*LogInLocators.LOG_IN_BUTTON).click()

    def click_log_out_link(self):
        self.driver.find_element(*LogInLocators.LOG_OUT_LINK).click()

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*LogInLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts