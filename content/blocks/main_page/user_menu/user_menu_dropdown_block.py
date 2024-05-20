import logging

from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock
from testing_projects_common.blocks.link import Link


class UserMenuDropdownBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "user-menu-dropdown-toggle"

    def get_user_menu_dropdown_link(self):
        return Link(self.me)

    def click_user_menu_dropdown_link(self):
        logging.info("Click on user menu link")
        link = self.get_user_menu_dropdown_link()
        link.wait_for_ready()
        link.click()
