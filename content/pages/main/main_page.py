from __future__ import annotations

from content.blocks.main_page.destinations_block import DestinationsBlock
from content.blocks.main_page.login_block import LoginBlock
from content.blocks.main_page.logo_block import LogoBlock
from content.blocks.main_page.user_menu.add_experience_block import AddExperienceBlock
from content.blocks.main_page.user_menu.logout_block import LogoutBlock
from content.blocks.main_page.user_menu.registration_block import RegistrationBlock
from content.blocks.main_page.user_menu.user_menu_block import UserMenuBlock
from content.blocks.main_page.user_menu.user_menu_dropdown_block import UserMenuDropdownBlock
from testing_projects_common.pages.base_page import BasePage
from acceptance_core.core.actions import waiting_actions


class MainPage(BasePage):
    __login_block = None
    __logo_block = None
    __registration_block = None
    __user_menu_dropdown_block = None
    __user_menu_block = None
    __add_experience_block = None
    __logout_block = None
    __destinations_block = None

    @property
    def login_block(self) -> LoginBlock:
        if self.__login_block is None:
            self.__login_block = LoginBlock()
        return self.__login_block

    @property
    def logo_block(self) -> LogoBlock:
        if self.__logo_block is None:
            self.__logo_block = LogoBlock()
        return self.__logo_block

    @property
    def registration_block(self) -> RegistrationBlock:
        if self.__registration_block is None:
            self.__registration_block = RegistrationBlock()
        return self.__registration_block

    @property
    def user_menu_dropdown_block(self) -> UserMenuDropdownBlock:
        if self.__user_menu_dropdown_block is None:
            self.__user_menu_dropdown_block = UserMenuDropdownBlock()
        return self.__user_menu_dropdown_block

    @property
    def user_menu_block(self) -> UserMenuBlock:
        if self.__user_menu_block is None:
            self.__user_menu_block = UserMenuBlock()
        return self.__user_menu_block

    @property
    def add_experience_block(self) -> AddExperienceBlock:
        if self.__add_experience_block is None:
            self.__add_experience_block = AddExperienceBlock()
        return self.__add_experience_block

    @property
    def logout_block(self) -> LogoutBlock:
        if self.__logout_block is None:
            self.__logout_block = LogoutBlock()
        return self.__logout_block

    @property
    def destinations_block(self) -> DestinationsBlock:
        if self.__destinations_block is None:
            self.__destinations_block = DestinationsBlock()
        return self.__destinations_block

    def wait_for_ready(self):
        waiting_actions.wait_for_load()
        waiting_actions.wait_for_element_visible(
            self.logo_block.me,
            "Could not waiting for visibility Logo block"
        )
        waiting_actions.wait_for_element_visible(
            self.destinations_block.me,
            "Could not waiting for visibility Destinations block"
        )
