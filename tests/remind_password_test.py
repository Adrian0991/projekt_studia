from tests.base_test import BaseTest
from test_data.remind_password_data import RemindPasswordData
import test_data.remind_password_data
from pages.remind_password_page import RemindPasswordPage
from ddt import data, unpack, ddt
from time import sleep

@ddt
class RemindPasswordTest(BaseTest):
    """
    Remind Login tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = RemindPasswordData()
        self.remind_password_page = RemindPasswordPage(self.driver)

    def test_remind_password_email_no_exist(self):
        """
        TC 010: User enter no exist email
        """
        # KROKI
        # 1. Kliknij "Zapomniałem loginu"
        self.remind_password_page = self.home_page.remind_password()
        # 2. Sprawdz poprawność komunikatu na stronie zrestartowania hasła
        self.assertEqual('Aby odzyskać hasło wpisz poniżej swój adres email, instrukcja zresetowania hasła zostanie natychmiastowo wysłana na twoją skrzynkę pocztową!',
        self.remind_password_page.get_user_info_messages()[0])
        # 3. Wprowadź email
        self.remind_password_page.enter_password_email(self.test_data.remind_password_email)
        # 6. Kliknij "wyślij"
        self.remind_password_page.click_send_btn()
        # Sprawdź poprawność komunikatów o nie wpisaniu loginu
        #self.assertEqual('Login został pomyślnie wysłany na twoją skrzynkę pocztową!', self.remind_login_page.get_user_tick_messages()[0])
        self.assertEqual('Użytkownik o podanym emailu nie istnieje!',
        self.remind_password_page.get_user_error_messages()[0])
        sleep(1)

    @data(*test_data.remind_password_data.get_csv_data("../test_data/login_or_password_remind.csv"))
    @unpack
    def test_remind_password_email_exist(self, email):
        """
        TC 011: User enter email
        """
        # KROKI
        # 1. Kliknij "Zapomniałem loginu"
        self.remind_password_page = self.home_page.remind_password()
        # 2. Sprawdz poprawność komunikatu na stronie zrestartowania hasła
        self.assertEqual('Aby odzyskać hasło wpisz poniżej swój adres email, instrukcja zresetowania hasła zostanie natychmiastowo wysłana na twoją skrzynkę pocztową!',
        self.remind_password_page.get_user_info_messages()[0])
        # 3. Wprowadź email
        self.remind_password_page.enter_password_email(email)
        # 4. Kliknij "wyślij"
        self.remind_password_page.click_send_btn()
        # Sprawdź poprawność komunikatów o instrukcji resetowania hasla
        self.assertEqual('Instrukcje resetowania hasła zostały wysłane na twoja skrzynkę pocztową!',
        self.remind_password_page.get_user_tick_messages()[0])
        sleep(1)