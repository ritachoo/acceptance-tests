import logging
import os

from acceptance_core.core.testing_project_url_data import TestingProjectUrlData
from acceptance_core.helpers.test_runner.ci_testing_host_helper import (
    get_testing_project_url_data_from_ci_env,
)


def get_testing_project_url_data() -> TestingProjectUrlData:
    testing_host_url_from_config = os.environ.get("TESTING_HOST_URL", "")
    if testing_host_url_from_config:
        return TestingProjectUrlData(testing_host_url_from_config)

    return get_testing_project_url_data_from_ci_env()


def get_waiting_default_timeout() -> int:
    return int(os.environ.get("WAITING_DEFAULT_TIMEOUT", 35))


def get_test_name() -> str:
    """Пример возвращаемого значения: test_correctly_opening_some_page"""
    test_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
    logging.debug(f"Got current test name: '{test_name}'")
    return test_name


def get_test_file_name() -> str:
    """Пример возвращаемого значения: tests/test_correctly_opening_pages.py"""
    test_file_name = os.environ.get("PYTEST_CURRENT_TEST").split(":")[0]
    logging.debug(f"Got current test file name: '{test_file_name}'")
    return test_file_name


def get_test_name_with_path() -> str:
    """Пример возвращаемого значения: 'tests.main_page.test_opening_pages.py.test_opening_main_page'"""
    result = get_test_file_name().replace("/", ".") + "." + get_test_name()
    logging.debug(f"Generated test name with path '{result}'")
    return result


def get_project_name() -> str:
    project_name = os.environ.get("PROJECT_NAME", "")
    logging.debug(f"Got '{project_name=}' from ENV")
    return project_name


def is_headless_mode() -> bool:
    """Возвращает True, если требуется selenium headless mode"""
    var = "HEADLESS_MODE"
    if os.environ.get(var):
        return os.environ.get(var) == "True"
    return False


def is_need_capture_screenshot() -> bool:
    return os.environ.get("CAPTURE_SCREENSHOT") == "True"


# Данные из окружения GitLab CI


def get_ci_commit_ref_name() -> str:
    """Возвращает branch name как есть из Gitlab-CI Runner Environment"""
    var = "CI_COMMIT_REF_NAME"
    if os.environ.get(var):
        return os.environ.get(var)
    return "no_ci_branch_name"


def get_ci_commit_ref_slug() -> str:
    """Возвращает немного отформатированное branch name из Gitlab-CI Runner Environment"""
    var = "CI_COMMIT_REF_SLUG"
    if os.environ.get(var):
        return os.environ.get(var)
    return "no_ci_branch_name"


def get_ci_project_id() -> str:
    var = "CI_PROJECT_ID"
    if os.environ.get(var):
        return os.environ.get(var)
    return ""


def get_ci_project_name() -> str:
    var = "CI_PROJECT_NAME"
    if os.environ.get(var):
        return os.environ.get(var)
    return ""


def get_ci_testing_host_url() -> str:
    var = "CI_TESTING_HOST_URL"
    if os.environ.get(var):
        return os.environ.get(var)
    return ""
