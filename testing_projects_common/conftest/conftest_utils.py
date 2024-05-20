import logging

from _pytest.fixtures import FixtureRequest
from acceptance_core.core.actions.screenshot_actions import ScreenshotActions
from acceptance_core.helpers import env


def send_finished_capture_screenshot(request: FixtureRequest):
    if is_test_failed(request) and env.is_need_capture_screenshot():
        capture_screenshot_on_fail()


def capture_screenshot_on_fail() -> str:
    screenshot_path = ScreenshotActions.get_instance().capture_full_page_screenshot(
        "FAILING"
    )
    logging.warning(f"--- Screenshot on Failing: {screenshot_path} ---")
    return screenshot_path


def is_test_failed(request: FixtureRequest) -> bool:
    # For good test exit by CTRL+C check attr 'rep_call' exists in request.node
    return hasattr(request.node, "rep_call") and request.node.rep_call.failed
