from content import content_vars
from testing_projects_common.blocks.base_block import BaseBlock


class LogoutBlock(BaseBlock):
    block_attribute_name = content_vars.test_attr_name
    block_attribute_value = "logout"
