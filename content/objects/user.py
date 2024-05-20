from __future__ import annotations

from content.helpers.user_data import generate_user_data
from content.pages.registration.registration_page import RegistrationPage
from content.url_builders.registration.registration_page_url_builder import RegistrationPageUrlBuilder


class User:
    def create_user(self) -> User:
        registration_page = RegistrationPage().open_me(RegistrationPageUrlBuilder())

        data = self.user_data
        registration_name_block = registration_page.registration_name_block
        registration_email_block = registration_page.registration_email_block
        registration_password_block = registration_page.registration_password_block
        registration_submit_block = registration_page.registration_submit_block

        registration_name_block.filling_registration_name_input(data.name)
        registration_email_block.filling_registration_email_input(data.email)
        registration_password_block.filling_registration_password_input(data.password)
        registration_submit_block.click_registration_submit_link()
        return self

    @property
    def user_data(self):
        generate_user_data()
        return generate_user_data()
