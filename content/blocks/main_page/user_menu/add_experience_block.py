import logging

from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock
from testing_projects_common.blocks.link import Link


class AddExperienceBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "experience-edit"

    def get_add_experience_link(self):
        return Link(self.me)

    def click_add_experience_link(self):
        logging.info("Click add experience link")
        link = self.get_add_experience_link()
        link.wait_for_ready()
        link.click()
