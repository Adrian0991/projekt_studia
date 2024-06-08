from tests.base_test import BaseTest
from test_data.login_data import LogInData
from pages.log_in_page import LogInPage
import pages.log_in_page
import test_data.login_data
from ddt import data, unpack, ddt
from time import sleep

@ddt
class LogInTest(BaseTest):
    """
    Registration tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = LogInData()
        self.log_in_page = LogInPage(self.driver)

    @data(*test_data.login_data.get_csv_data("../test_data/login_and_password_to_log_in.csv"))
    @unpack
    def test_login_with_exist_login_and_password_ddt(self, login, password):
        """
        TC 001: User enter exist login and password
        """
        # KROKI
        # 2. Wprowadź login
        self.log_in_page.enter_login(login)
        # 5. Wprowadź hasło
        self.log_in_page.enter_password(password)
        # 6. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.log_in_page.click_on_checkbox_auto_log_in()
        # 7. Kliknij "zaloguj"
        self.log_in_page.click_log_in_btn()
        # 8. Kliknij "wyloguj"
        self.log_in_page.click_log_out_link()
        sleep(1)

    def test_no_login(self):
        """
        TC 002: User enter no exist login and password
        """
        # KROKI
        # 2. Wprowadź email
        self.log_in_page.enter_login(self.test_data.login)
        # 3. Wprowadź hasło
        self.log_in_page.enter_password(self.test_data.password)
        # 7. Kliknij "zaloguj"
        self.log_in_page.click_log_in_btn()
        # Sprawdź poprawność komunikatów o wpisaniu istniejącego loginu lub/i hasła
        self.assertEqual('Podany login bądź hasło jest błędne, spróbuj ponownie lub skorzystaj z funkcji', self.log_in_page.get_user_error_messages()[0])
        sleep(1)