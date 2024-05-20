from testing_projects_common.blocks.base_block import BaseBlock
from acceptance_core.core.actions import driver_actions, waiting_actions


class Button(BaseBlock):
    """Любая кнопка"""

    def click(self):
        driver_actions.click(self.me)

    def click_by_html(self):
        driver_actions.click_by_html(self.me)

    def wait_for_element_visible(self):
        waiting_actions.wait_for_element_visible(self.me)
