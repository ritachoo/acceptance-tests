import logging

from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock
from testing_projects_common.blocks.link import Link


class AllCitiesBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "destinations"

    def get_all_cities_link(self) -> Link:
        return Link(self.me)

    def click_all_cities_link(self):
        logging.info("Click on all cities block")
        link = self.get_all_cities_link()
        link.wait_for_ready()
        link.click()
