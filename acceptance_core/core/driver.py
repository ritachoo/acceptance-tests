from __future__ import annotations

import logging

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from acceptance_core.core.exception.ut_exception import UTException
from acceptance_core.helpers import env
from webdriver_manager.chrome import ChromeDriverManager

instance: WebDriver


def initialize() -> WebDriver:
    global instance

    logging.info("Creating WebDriver Chrome instance")

    test_name_for_show = env.get_test_file_name() + "::" + env.get_test_name()

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["name"] = test_name_for_show

    chrome_options = Options()

    chrome_prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    chrome_options.add_experimental_option("prefs", chrome_prefs)

    if env.is_headless_mode():
        logging.info("Enabling 'headless mode' for browser instance")
        chrome_options.headless = True
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")

    chrome_options.page_load_strategy = 'normal'

    try:
        logging.info("Trying get instance")
        instance = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        instance.implicitly_wait(5)
        logging.info(f"Get instance={instance}")
    except Exception:
        raise UTException(
            "Could not create WebDriver Chrome instance. Test cannot start"
        )

    return instance


def close_driver():
    global instance
    logging.info("Quit WebDriver instance. Bye-bye!")
    instance.quit()
