from testing_projects_common.url_builders.base_url_builder import BaseUrlBuilder
from acceptance_core.helpers import env


class RegistrationPageUrlBuilder(BaseUrlBuilder):
    def get_url_to_open(self) -> str:
        registration_page_url = env.get_testing_project_url_data().url_with_basic_auth + "/registration/?next=/"
        return registration_page_url
