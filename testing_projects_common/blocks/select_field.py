from testing_projects_common.blocks.base_block import BaseBlock
from acceptance_core.core.actions import driver_actions


class SelectField(BaseBlock):
    """Любое поле с выбором какого-то значения в нем"""

    def select_by_value(self, value_to_select: str):
        driver_actions.select_by_value(self.me, value_to_select, True)

    def select_by_visible_text(self, text_to_select: str):
        driver_actions.select_by_visible_text(self.me, text_to_select, True)


# todo
# дописать селектов
