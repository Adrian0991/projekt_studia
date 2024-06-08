class BasePage:
    """
    Base class for every pages
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return