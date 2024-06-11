from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CreateCustomerAccountPageLocators:
    LOGIN_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "mail")
    FIRST_PASSWORD_INPUT = (By.NAME, "_pass")
    SECOND_PASSWORD_INPUT = (By.NAME, "pass_")
    ACCEPTANCE_OF_CHECKBOX_REGULATIONS = (By.ID, "license_box")
    STATUTE_LINK = (By.LINK_TEXT, 'regulamin')
    REGISTER_BTN = (By.ID, "next_box")
    USER_ERROR_MESSAGES = (By.XPATH, '//div[@class="warn"]')
    USER_INFO_MESSAGES = (By.XPATH, '//div[@class="infos"]')
class CreateCustomerAccountPage(BasePage):

    def enter_login(self, login):
        """
        Enters login
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.LOGIN_INPUT)
        el.send_keys(login)

    def enter_email(self, email):
        """
        Enter email
        """
        # Odszukać to pole
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.EMAIL_INPUT)
        el.send_keys(email)

    def enter_password(self, first_password):
        """
        Enter password
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.FIRST_PASSWORD_INPUT)
        el.send_keys(first_password)

    def repeat_password(self, second_password):
        """
        Repeat password
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.SECOND_PASSWORD_INPUT)
        el.send_keys(second_password)

    def mark_checkbox_acceptance_of_regulations(self):
        """
        Acceptance of regulations
        """
        self.driver.find_element(*CreateCustomerAccountPageLocators.ACCEPTANCE_OF_CHECKBOX_REGULATIONS).click()

    def click_statute_link(self):
        """
        Go to Statute Page
        """
        self.driver.find_element(*CreateCustomerAccountPageLocators.STATUTE_LINK).click()

    def click_register_btn(self):
        """
        Creating user
        """
        self.driver.find_element(*CreateCustomerAccountPageLocators.REGISTER_BTN).click()

    def get_user_info_messages(self):
        """
        Returns list of user info messages
        """
        infos = self.driver.find_elements(*CreateCustomerAccountPageLocators.USER_INFO_MESSAGES)
        infos_texts = []
        for i in infos:
            # Dodaję zawartość tekstową do listy
            infos_texts.append(i.text)
        return infos_texts

    def get_user_error_messages(self):
        """
        Returns list of user error messages
        """
        errors = self.driver.find_elements(*CreateCustomerAccountPageLocators.USER_ERROR_MESSAGES)
        errors_texts = []
        for e in errors:
            # Dodaję zawartość tekstową do listy
                errors_texts.append(e.text)
        return  errors_texts