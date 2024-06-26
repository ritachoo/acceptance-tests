import logging
import pathlib
from pathlib import Path

from acceptance_core.core import driver
from acceptance_core.core.actions import driver_actions
from acceptance_core.core.actions.screenshot_local_storage_data import (
    ScreenshotLocalStorageData,
)
from acceptance_core.helpers import env
from acceptance_core.helpers.utils import date_utils


def create_and_save_screenshot_in_local(
    screenshot_local_storage_data: ScreenshotLocalStorageData,
):
    """Make and save screenshot in local dir. Return origin screenshot_path_data if success"""
    dir_path_for_screenshot = screenshot_local_storage_data.local_dir_path
    screenshot_path_with_file: Path = (
        screenshot_local_storage_data.full_local_screenshot_path
    )

    pathlib.Path(dir_path_for_screenshot).mkdir(parents=True, exist_ok=True)

    # Resize to full page for making screenshot
    driver_actions.resize_window_to_full_page()

    logging.info(f"Saving screenshot in path: '{screenshot_path_with_file}'")
    status = driver.instance.save_screenshot(str(screenshot_path_with_file.absolute()))
    if status:
        logging.info(
            f"Successfully saved screenshot in local storage: '{screenshot_path_with_file=}'"
        )
        return screenshot_path_with_file

    logging.warning(f"Failed on saving screenshot in '{screenshot_path_with_file=}'")
    return ""


class ScreenshotActions:
    """Attention: Singleton object, use by ScreenshotActions.get_instance()"""

    __instance = None
    # Screenshots from one test should be saved in one folder
    screenshots_dir_name_postfix = ""

    def __init__(self):
        if not ScreenshotActions.__instance:
            self.screenshots_dir_name_postfix = date_utils.generate_date(
                format_date="%Y-%m-%d-%H-%M-%S"
            )

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            logging.debug("Creating ScreenshotActions instance")
            cls.__instance = ScreenshotActions()
        return cls.__instance

    def capture_full_page_screenshot(self, screenshot_name_postfix: str = "") -> str:
        """Return uploaded screenshot path"""

        screenshot_local_storage_data = self.create_screenshot_local_storage_data(
            screenshot_name_postfix
        )
        local_screenshot = create_and_save_screenshot_in_local(screenshot_local_storage_data)
        return local_screenshot

    def create_screenshot_local_storage_data(
        self, screenshot_name_postfix: str = ""
    ) -> ScreenshotLocalStorageData:
        """Return local storage data for in future saved screenshot"""
        screenshot_local_storage_data = ScreenshotLocalStorageData()

        append_to_screenshot_file_name = ""
        if screenshot_name_postfix:
            append_to_screenshot_file_name = "_" + screenshot_name_postfix

        # Example: test_screenshots-2020-01-22-20-03-53
        screenshots_dir_name = (
            env.get_test_name() + "-" + self.screenshots_dir_name_postfix
        )

        project_name = env.get_project_name()
        # Example: /acceptance-tests/output/screenshots/test_screenshots-2020-01-22-20-03-53/
        screenshots_dir_path = Path(
            f"output/screenshots/{project_name}/{screenshots_dir_name}/"
        )

        test_file_name = env.get_test_file_name().replace("/", "_").replace(".", "_")
        date_for_test = "_" + date_utils.generate_date(format_date="%H_%M_%S_%f")
        # Example: test_correctly_opening_page_py_test_screenshots_20_03_54_889506.png
        screenshot_file_name = (f"{test_file_name}_{env.get_test_name()}"
                                f"{append_to_screenshot_file_name}{date_for_test}.png")
        # Example:
        # /acceptance-tests/output/screenshots/test_screenshots-2020-01-22-20-03-53/test_correctly_opening_pages_py_test_screenshots_20_03_54_889506.png
        screenshot_path = screenshots_dir_path / screenshot_file_name

        screenshot_local_storage_data.set_screenshots_dir_name(screenshots_dir_name)
        screenshot_local_storage_data.set_local_dir_path(screenshots_dir_path)
        screenshot_local_storage_data.set_screenshot_file_name(screenshot_file_name)
        screenshot_local_storage_data.set_full_local_screenshot_path(screenshot_path)
        return screenshot_local_storage_data
