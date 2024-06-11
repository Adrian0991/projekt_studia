from tests.base_test import BaseTest
from test_data.remind_login_data import RemindLoginData
import test_data.remind_login_data
from pages.remind_login_page import RemindLoginPage
from ddt import data, unpack, ddt
from time import sleep
import os

@ddt
class RemindLoginTest(BaseTest):
    """
    Remind Login tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = RemindLoginData()
        self.remind_login_page = RemindLoginPage(self.driver)

    def test_remind_login_email_no_exist(self):
        """
        TC 008: User enter no exist email
        """
        # KROKI
        # 1. Kliknij "Zapomniałem loginu"
        self.remind_login_page = self.home_page.remind_login()
        # 2. Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Aby odzyskać login wpisz poniżej adres eMail, login zostanie natychmiastowo wysłany na twoją skrzynkę pocztową!',
        self.remind_login_page.get_user_info_messages()[0])
        # 3. Wprowadź email
        self.remind_login_page.enter_login_email(self.test_data.remind_login_email)
        # 4. Kliknij "wyślij"
        self.remind_login_page.click_send_btn()
        # Sprawdź poprawność komunikatów o nie wpisaniu loginu
        self.assertEqual('Użytkownik o podanym mailu nie istnieje!',
        self.remind_login_page.get_user_error_messages()[0])
        sleep(1)

    @data(*test_data.remind_login_data.get_csv_data("../test_data/login_or_password_remind.csv"))
    @unpack
    def test_remind_login_email_exist(self, email):
        """
        TC 009: User enter exist email
        """
        # KROKI
        # 1. Kliknij "Zapomniałem loginu"
        self.remind_login_page = self.home_page.remind_login()
        # 2. Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Aby odzyskać login wpisz poniżej adres eMail, login zostanie natychmiastowo wysłany na twoją skrzynkę pocztową!',
        self.remind_login_page.get_user_info_messages()[0])
        # 3. Wprowadź email
        self.remind_login_page.enter_login_email(email)
        # 4. Kliknij "wyślij"
        self.remind_login_page.click_send_btn()
        # Sprawdź poprawność komunikatów o nie wpisaniu loginu
        self.assertEqual('Login został pomyślnie wysłany na twoją skrzynkę pocztową!',
        self.remind_login_page.get_user_tick_messages()[0])
        sleep(1)