import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, ui
from acceptance_core.core import driver
from acceptance_core.core.actions import driver_actions
from acceptance_core.core.selector import Selector
from acceptance_core.helpers import env


def wait_for_load() -> bool:
    try_count = 0
    max_try_count = env.get_waiting_default_timeout()
    get_page_state_js = "return document.readyState"
    state = str(driver_actions.execute_js(get_page_state_js))

    while state != "complete":
        if try_count > max_try_count:
            logging.warning(f"Could not waiting for page load for {max_try_count} seconds")
            return False

        try_count += 1
        state = str(driver_actions.execute_js(get_page_state_js))
        logging.info(f"Current page {state=}, try = {try_count} of {max_try_count}")
        time.sleep(1)

    logging.info(f"Successfully loading page with '{state=}' for {try_count} seconds")
    return True


def wait_for_element_exists(selector: Selector, message: str = None, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    if message is None:
        message = f"Element with selector='{str(selector)}' did not exists for {timeout} seconds"

    logging.info(f"Waiting for existing element with selector='{str(selector)}' for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, str(selector))),
        message,
    )


def wait_for_element_clickable(selector: Selector, message: str = None, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    if message is None:
        message = f"Element with selector='{str(selector)}' did not become clickable for {timeout} seconds"

    logging.info(f"Waiting element with selector='{str(selector)}' being clickable for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, str(selector))),
        message,
    )


def wait_for_element_visible(selector: Selector, message: str = None, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    if message is None:
        message = f"Element with selector='{str(selector)}' did not become visible for {timeout} seconds"

    logging.info(f"Waiting for visibility element with selector='{str(selector)}' for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, str(selector))),
        message,
    )


def wait_for_element_visible_xpath(selector: Selector, message: str = None, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    if message is None:
        message = f"Element with selector='{str(selector)}' did not become visible for {timeout} seconds"

    logging.info(f"Waiting for visibility element with selector='{str(selector)}' for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(
        expected_conditions.visibility_of_element_located((By.XPATH, str(selector))),
        message,
    )


def wait_for_element_not_visible(selector: Selector, message: str = None, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    if message is None:
        message = f"Element with selector='{str(selector)}' did not become invisible for {timeout} seconds"

    logging.info(f"Waiting for invisibility element with selector='{str(selector)}' for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(
        expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, str(selector))),
        message,
    )


def wait_for_ajax(timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)
    try:
        logging.info(f"Waiting for complete all ajax-requests for {timeout} seconds")
        wait_for_js("return $.active == 0;", timeout)
    except Exception as e:
        logging.warning(
            f"Could not wait for completion of all AJAX requests during timeout of {timeout} seconds. "
            f"With Exception {e}"
        )


def wait_for_js(js: str, timeout: int = None):
    timeout = get_waiting_timeout_from_env_if_necessary(timeout)

    logging.info(f"Waiting for JS-script '{js}' for {timeout} seconds")
    ui.WebDriverWait(driver.instance, timeout).until(lambda x: x.execute_script(js))


def get_waiting_timeout_from_env_if_necessary(timeout: int = None):
    if timeout is None:
        timeout = env.get_waiting_default_timeout()
        logging.debug(f"Set timeout from ENV-config in {timeout} seconds")
        return timeout

    logging.debug(f"Set timeout NOT from ENV-config in {timeout} seconds, probably from method's argument")
    return timeout
