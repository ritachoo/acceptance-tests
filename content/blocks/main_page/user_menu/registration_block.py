import logging

from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock
from testing_projects_common.blocks.link import Link


class RegistrationBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "registration"

    def get_registration_link(self) -> Link:
        return Link(self.me)

    def click_registration_link(self):
        logging.info("Click on registration link block")
        link = self.get_registration_link()
        link.wait_for_ready()
        link.click()
