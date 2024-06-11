from tests.base_test import BaseTest
from test_data.search_data import SearchData
import test_data.search_data
from pages.search_result_page import SearchResultPage
from ddt import data, unpack, ddt
from time import sleep

@ddt
class SearchResultTest(BaseTest):
    """
    Registration tests
    """
    def setUp(self):
        super().setUp()
        self.test_data = SearchData()
        self.search_result_page = SearchResultPage(self.driver)

    @data(*test_data.search_data.get_csv_data("../test_data/words_to_search.csv"))
    @unpack
    def test_search_movie_ddt(self, word):
        """
        TC 012: User enter word to find movie
        """
        # KROKI
        # 1. Wprowadź login
        self.search_result_page.enter_words(word)
        # 2. Kliknij "szukaj"
        self.search_result_page.click_search_btn()
        # Sprawdź wyniki wyszukiwania
        self.search_result_page.get_search_results()
        sleep(1)

    def test_search_no_movie(self):
        """
        TC 013: User enter word to find movie
        """
        # KROKI
        # 1. Wprowadź login
        self.search_result_page.enter_words(self.test_data.word)
        # 2. Kliknij "szukaj"
        self.search_result_page.click_search_btn()
        # Sprawdź poprawność komunikatów o wpisaniu nieistniejącego filmu na tej stronie
        self.assertEqual('Nic nie znaleziono...',
        self.search_result_page.get_user_error_messages()[0])
        sleep(1)