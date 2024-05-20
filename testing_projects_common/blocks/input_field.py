from testing_projects_common.blocks.base_block import BaseBlock
from acceptance_core.core.actions import driver_actions


class InputField(BaseBlock):
    """Любое поле для ввода, например, текста"""

    def input_with_check(self, string_to_input: str, need_click_by_html: bool = False):
        driver_actions.input_in_field(
            self.me,
            string_to_input,
            need_check_for_correctly_input=True,
            need_click_by_html=need_click_by_html,
        )

    def input(self, string_to_input: str):
        driver_actions.input_in_field(self.me, string_to_input, need_check_for_correctly_input=False)

    def input_by_char(self, string_to_input: str, need_click_by_html: bool = False):
        driver_actions.input_in_field_by_char(self.me, string_to_input, need_click_by_html)

    def input_with_keyboard_clear(self, string_to_input: str):
        driver_actions.input_in_field(
            self.me,
            string_to_input,
            need_clear_field_with_keyboard=True,
            need_check_for_correctly_input=False,
        )

    def send_keys(self, string_to_input: str):
        driver_actions.send_keys(self.me, string_to_input)

    def grab_value_from_input_field(self) -> str:
        return driver_actions.get_attr_value_from_element(self.me, "value")

    def clear(self):
        driver_actions.clear_field(self.me)

    def click(self):
        driver_actions.click(self.me)
