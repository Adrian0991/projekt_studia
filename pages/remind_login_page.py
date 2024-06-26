from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RemindLoginPageLocators:
    EMAIL_LOGIN_INPUT = (By.NAME, "mail_login")
    REMIND_LOGIN_PAGE_INFO_MESSAGE = (By.XPATH, '//div[@class="infos"]')
    SEND_BUTTON = (By.CSS_SELECTOR, 'input[value="wyślij"]')
    REMIND_LOGIN_INFO_MESSAGE = (By.XPATH, '//div[@class ="tick"]')
    USER_ERROR_MESSAGES = (By.XPATH, '//div[@class="warn"]')
class RemindLoginPage(BasePage):
    def enter_login_email(self, email):
        """
        Enter email
        """
        # Odszukać to pole
        el = self.driver.find_element(*RemindLoginPageLocators.EMAIL_LOGIN_INPUT)
        el.send_keys(email)

    def click_send_btn(self):
        """
        Send email with login
        """
        self.driver.find_element(*RemindLoginPageLocators.SEND_BUTTON).click()

    def get_user_info_messages(self):
        """
        Returns list of user info messages
        """
        infos = self.driver.find_elements(*RemindLoginPageLocators.REMIND_LOGIN_PAGE_INFO_MESSAGE)
        infos_texts = []
        for i in infos:
            # Dodaję zawartość tekstową do listy
            infos_texts.append(i.text)
        return infos_texts

    def get_user_tick_messages(self):
        """
        Returns list of confirmation messages
        """
        ticks = self.driver.find_elements(*RemindLoginPageLocators.REMIND_LOGIN_INFO_MESSAGE)
        ticks_texts = []
        for t in ticks:
            # Dodaję zawartość tekstową do listy
            ticks_texts.append(t.text)
        return ticks_texts

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*RemindLoginPageLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts