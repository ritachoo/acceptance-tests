from testing_projects_common.blocks.base_block import BaseBlock
from acceptance_core.core.actions import driver_actions


class Checkbox(BaseBlock):
    """Чекбокс. Квадратик с галочкой такой :)"""

    def click(self):
        driver_actions.click(self.me)

    def click_by_html(self):
        driver_actions.click_by_html(self.me)
