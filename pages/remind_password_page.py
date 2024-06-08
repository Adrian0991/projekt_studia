from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class RemindPasswordPageLocators:
    EMAIL_PASSWORD_INPUT = (By.NAME, "pass_email")
    REMIND_PASSWORD_PAGE_INFO_MESSAGE = (By.XPATH, '//div[@class="infos"]')
    SEND_BUTTON = (By.CSS_SELECTOR, 'input[value="wyślij"]')
    REMIND_PASSWORD_INFO_MESSAGE = (By.XPATH, '//div[@class ="tick"]')
    USER_ERROR_MESSAGES = (By.XPATH, '//div[@class="warn"]')
class RemindPasswordPage(BasePage):
    def enter_password_email(self, email):
        """
        Enter email
        """
        # Odszukać to pole
        el = self.driver.find_element(*RemindPasswordPageLocators.EMAIL_PASSWORD_INPUT)
        el.send_keys(email)

    def click_send_btn(self):
        self.driver.find_element(*RemindPasswordPageLocators.SEND_BUTTON).click()

    def get_user_info_messages(self):
        """
        Returns list of user info messages
        """
        infos = self.driver.find_elements(*RemindPasswordPageLocators.REMIND_PASSWORD_PAGE_INFO_MESSAGE)
        infos_texts = []
        for i in infos:
            # Dodaję zawartość tekstową do listy
            infos_texts.append(i.text)
        return infos_texts

    def get_user_tick_messages(self):
        """
        Returns list of user info messages
        """
        ticks = self.driver.find_elements(*RemindPasswordPageLocators.REMIND_PASSWORD_INFO_MESSAGE)
        ticks_texts = []
        for t in ticks:
            # Dodaję zawartość tekstową do listy
            ticks_texts.append(t.text)
        return ticks_texts

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*RemindPasswordPageLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts