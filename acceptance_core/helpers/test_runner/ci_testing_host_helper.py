import os

from acceptance_core.core.exception.uc_exception import UCException
from acceptance_core.core.testing_project_url_data import TestingProjectUrlData


def get_testing_project_url_data_from_ci_env() -> TestingProjectUrlData:
    ci_testing_host_env_var = "CI_TESTING_HOST_URL"
    ci_testing_host_url = os.environ.get(ci_testing_host_env_var, "")
    if not ci_testing_host_url:
        raise UCException(
            f"Error! Create '{ci_testing_host_env_var} in ENV'. Current is '{ci_testing_host_url=}'"
        )
    return TestingProjectUrlData(ci_testing_host_url)
