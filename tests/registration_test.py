from tests.base_test import BaseTest
from test_data.registration_data import RegistrationData
import test_data.registration_data
from ddt import data, unpack, ddt
from time import sleep

@ddt
class RegistrationTest(BaseTest):
    """
    Registration tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = RegistrationData()

    def test_go_to_webside_regulations_by_register(self):
        """
        TC 000: User want to go and read webside regulations and back to registration page
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # 3. KLiknij w "regulamin"
        self.create_customer_account_page.click_statute_link()
        sleep(1)
        # 4. Wróć do strony Rejestracji klikając "Rejestracja
        self.create_customer_account_page = self.home_page.click_sign_in()
        sleep(1)

    @data(*test_data.registration_data.get_csv_data("../test_data/registration.csv"))
    @unpack
    def test_exist_login_ddt(self, login, email, password):
        """
        TC 001: User enter exist login
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Wprowadź login
        self.create_customer_account_page.enter_login(login)
        # 3. Wprowadź email
        self.create_customer_account_page.enter_email(email)
        # 4. Wprowadź hasło
        self.create_customer_account_page.enter_password(password)
        # 5. Powtórz hasło
        self.create_customer_account_page.repeat_password(password)
        # 6. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.create_customer_account_page.mark_acceptance_of_checkbox_regulations()
        # 7. Kliknij "zarejestruj"
        self.create_customer_account_page.click_register_btn()
        # Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # Sprawdź poprawność komunikatów o wpisaniu istniejącego loginu
        self.assertEqual('podany login jest już zajęty!',
        self.create_customer_account_page.get_user_error_messages()[0])
        sleep(1)

    def test_no_login(self):
        """
        TC 002: User does not enter his login
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Wprowadź email
        self.create_customer_account_page.enter_email(self.test_data.registration_email)
        # 3. Wprowadź hasło
        self.create_customer_account_page.enter_password(self.test_data.first_password)
        # 4. Powtórz hasło
        self.create_customer_account_page.repeat_password(self.test_data.first_password)
        # 5. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.create_customer_account_page.mark_acceptance_of_checkbox_regulations()
        # 6. Kliknij "zarejestruj"
        self.create_customer_account_page.click_register_btn()
        # Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # Sprawdź poprawność komunikatów o nie wpisaniu loginu
        self.assertEqual('login jest nieprawidłowy, możesz używać tylko liter i cyfr!',
        self.create_customer_account_page.get_user_error_messages()[0])
        self.assertEqual('podany login jest już zajęty!',
        self.create_customer_account_page.get_user_error_messages()[1]) # komunikat ten można uznać jako błąd, ponieważ prawdopodobnie nie ma takiego użytkownika
        sleep(1)

    def test_no_email(self):
        """
        TC 003: User does not enter his email
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Wprowadź login
        self.create_customer_account_page.enter_login(self.test_data.registration_login)
        # 3. Wprowadź hasło
        self.create_customer_account_page.enter_password(self.test_data.first_password)
        # 4. Powtórz hasło
        self.create_customer_account_page.repeat_password(self.test_data.first_password)
        # 5. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.create_customer_account_page.mark_acceptance_of_checkbox_regulations()
        # 6. Kliknij "zarejestruj"
        self.create_customer_account_page.click_register_btn()
        # Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # Sprawdź poprawność komunikatów o nie wpisaniu loginu
        self.assertEqual('adres e-mail jest nieprawidłowy!',
        self.create_customer_account_page.get_user_error_messages()[0])
        sleep(1)

    def test_no_password(self):
        """
        TC 004: User does not enter his password
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Wprowadź login
        self.create_customer_account_page.enter_login(self.test_data.registration_login)
        # 3. Wprowadź email
        self.create_customer_account_page.enter_email(self.test_data.registration_email)
        # 5. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.create_customer_account_page.mark_acceptance_of_checkbox_regulations()
        # 6. Kliknij "zarejestruj"
        self.create_customer_account_page.click_register_btn()
        # Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # Sprawdź poprawność komunikatów o nie wpisaniu hasła
        self.assertEqual('hasło musi zawierać conajmniej 6 znaków i co najwyżej 20!',
        self.create_customer_account_page.get_user_error_messages()[0])
        self.assertEqual('podane hasła nie są identyczne!',
        self.create_customer_account_page.get_user_error_messages()[1]) # komunikat ten można uznać za błąd, ponieważ nie wpisując hasła w obu polach mamy tą samą wartość
        sleep(3)

    def test_no_equal_passwords(self):
        """
        TC 005: User does enter his correct password
        """
        # KROKI
        # 1. Kliknij "Rejestracja"
        self.create_customer_account_page = self.home_page.click_sign_in()
        # 2. Wprowadź login
        self.create_customer_account_page.enter_login(self.test_data.registration_login)
        # 3. Wprowadź email
        self.create_customer_account_page.enter_email(self.test_data.registration_email)
        # 4. Wprowadź hasło
        self.create_customer_account_page.enter_password(self.test_data.first_password)
        # 5. Powtórz hasło
        self.create_customer_account_page.repeat_password(self.test_data.second_password)
        # 5. Zaznacz checkbox dotyczący akceptacji regulaminu
        self.create_customer_account_page.mark_acceptance_of_checkbox_regulations()
        # 6. Kliknij "zarejestruj"
        self.create_customer_account_page.click_register_btn()
        # Sprawdz poprawność komunikatu na stronie rejestracji klienta
        self.assertEqual('Rejestracja jest całkowicie darmowa i zajmuje tylko kilka sekund.',
        self.create_customer_account_page.get_user_info_messages()[0])
        # Sprawdź poprawność komunikatów o wpisaniu niepoprawnego hasła
        self.assertEqual('podane hasła nie są identyczne!',
        self.create_customer_account_page.get_user_error_messages()[0])
        sleep(3)
