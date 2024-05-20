from testing_projects_common.url_builders.base_url_builder import BaseUrlBuilder
from acceptance_core.helpers import env


class MainPageUrlBuilder(BaseUrlBuilder):
    def get_url_to_open(self) -> str:
        main_page_url = env.get_testing_project_url_data().url_with_basic_auth
        return main_page_url
