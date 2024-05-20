import os

import pytest
from content.fixtures.experience_fixtures import create_individual_experience_by_ui  # noqa
from content.fixtures.user_fixtures import create_user_by_ui  # noqa
from testing_projects_common.conftest.conftest_utils import send_finished_capture_screenshot
from acceptance_core.core import driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Hack https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
    setattr(item, "rep_" + rep.when, rep)
    # Create attribute request.node.exception for request.node if test failed
    if rep.when == "call" and rep.failed:
        setattr(item, "exception", call.excinfo.value)


@pytest.fixture(autouse=True)
def run_test(request):

    driver.initialize()

    # Запуск теста
    yield

    send_finished_capture_screenshot(request)

    driver.close_driver()


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://example.com", help="Testing host URL"
    )


def pytest_configure(config):
    os.environ["CI_TESTING_HOST_URL"] = config.getoption("url")
