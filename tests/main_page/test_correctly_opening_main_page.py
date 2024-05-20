from content.pages.main.main_page import MainPage
from content.url_builders.main.main_page_url_builder import MainPageUrlBuilder
from acceptance_core.core.asserts import assert_selector_visible


class TestsForCorrectlyOpeningMainPages:
    def test_for_correctly_opening_main_page(self):
        """Example test"""
        main_page = MainPage().open_me(MainPageUrlBuilder())
        login_block = main_page.login_block
        logo_block = main_page.logo_block
        assert_selector_visible(login_block.me, "Login block is not visible")
        assert_selector_visible(logo_block.me, "Logo block is not visible")
