import logging

from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock
from testing_projects_common.blocks.link import Link


class DestinationsBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "destinations"

    def get_destinations_link(self) -> Link:
        return Link(self.me)

    def click_destinations_link(self):
        logging.info("Click on destinations block on main page")
        destinations_link = self.get_destinations_link()
        destinations_link.wait_for_ready()
        destinations_link.click_by_html()
