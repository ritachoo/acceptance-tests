from __future__ import annotations

from content.blocks.destinations_page.all_cities_block import AllCitiesBlock
from testing_projects_common.pages.base_page import BasePage
from acceptance_core.core.actions import waiting_actions


class DestinationsPage(BasePage):
    __all_cities_block = None

    @property
    def all_cities_block(self) -> AllCitiesBlock:
        if self.__all_cities_block is None:
            self.__all_cities_block = AllCitiesBlock()
        return self.__all_cities_block

    def wait_for_ready(self):
        waiting_actions.wait_for_load()
        waiting_actions.wait_for_element_visible(
            self.all_cities_block.me, "Could not waiting for visibility All cities block"
        )
