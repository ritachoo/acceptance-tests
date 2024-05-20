from content.pages.destinations.destinations_page import DestinationsPage
from content.pages.main.main_page import MainPage
from content.url_builders.main.main_page_url_builder import MainPageUrlBuilder
from acceptance_core.core.asserts import assert_selector_visible


class TestClickAllCities:
    def test_click_all_cities(self):
        main_page = MainPage().open_me(MainPageUrlBuilder())

        destinations_block = main_page.destinations_block
        destinations_block.click_destinations_link()

        destinations_page = DestinationsPage()
        all_cities_block = destinations_page.all_cities_block
        assert_selector_visible(all_cities_block.me, "All cities block is not visible")
