import logging
import time
from time import sleep
from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from acceptance_core.core import driver
from acceptance_core.core.actions import waiting_actions
from acceptance_core.core.exception.uc_exception import UCException
from acceptance_core.core.selector import Selector
from acceptance_core.core.testing_project_url_data import TestingProjectUrlData
from acceptance_core.helpers import env

# Click/tap methods


def click(selector: Selector):
    logging.info(f"Native click on element with selector '{selector}'")
    locate_element(selector).click()
    waiting_actions.wait_for_load()


def click_by_html(selector: Selector):
    logging.info(f"Click on element with selector '{selector}' by HTML")
    execute_js(get_dom_object(selector, "click()"))
    waiting_actions.wait_for_load()


def click_by_text(text: str):
    logging.info(f"Click on element '{text}'")
    locate_element_by_text(text).click()
    waiting_actions.wait_for_load()


def click_by_partial_text(text: str):
    logging.info(f"Click on element '{text}'")
    locate_element_by_partial_text(text).click()
    waiting_actions.wait_for_load()


def click_by_xpath(xpath: str):
    logging.info(f"Click on element '{xpath}'")
    locate_element_by_xpath(xpath).click()
    waiting_actions.wait_for_load()


def double_click(selector: Selector):
    element = locate_element(selector)
    logging.info(f"Double click on element with selector '{selector}'")
    ActionChains(driver.instance).double_click(element).perform()
    waiting_actions.wait_for_load()


# Select methods


def select_by_value(selector: Selector, value: str, clear_inline_css_display: bool):
    logging.info(f"Select option with value {value} for selector '{selector}'")
    element = locate_element(selector)

    if clear_inline_css_display:
        execute_js(f"document.querySelector('{selector}').style.display = '';")

    select_obj = Select(element)
    select_obj.select_by_value(value)
    waiting_actions.wait_for_load()


def select_by_visible_text(selector: Selector, text: str, clear_inline_css_display: bool):
    logging.info(f"Select option with value {text} for selector '{selector}'")
    element = locate_element(selector)

    if clear_inline_css_display:
        execute_js(f"document.querySelector('{selector}').style.display = '';")

    select_obj = Select(element)
    select_obj.select_by_visible_text(text)
    waiting_actions.wait_for_load()


# Openers methods


def open_direct_url(url: str):
    logging.info(f"Opening direct URL: '{url}'")
    driver.instance.get(url)
    waiting_actions.wait_for_load()


# Grabber methods


def grab_text_from_element(selector: Selector) -> str:
    if is_element_not_exists(selector):
        logging.info(f"Can't grab text from selector '{selector}': element do not exist.")
        return ""

    element = locate_element(selector)
    grabbed_text = element.text if element.is_displayed() else grab_text_from_hidden_element(selector)
    logging.info(f"Grabbed text '{grabbed_text}' from selector '{selector}'")
    return grabbed_text


def grab_text_from_hidden_element(selector: Selector) -> str:
    grabbed_text = execute_js("return " + get_dom_object(selector, "textContent"))
    logging.debug(f"Grabbed text '{grabbed_text}' from hidden selector '{selector}' by JS")
    return grabbed_text


def grab_text_from_elements(selector: Selector) -> list:
    result = list()
    i = 0
    for element in locate_elements(selector):
        grabbed_text = element.text if element.is_displayed() else execute_js(f"return $('{selector}').eq({i}).text();")
        result.append(grabbed_text)
        i += 1
    return result


def grab_value_from_element(selector: Selector) -> str:
    element = locate_element(selector)

    if element.tag_name == "select":
        select = Select(element)
        grabbed_value = select.first_selected_option.text
        logging.info(f"Grabbed value '{grabbed_value}' from selector '{selector}' as 'select' element")
        return grabbed_value

    grabbed_value = element.text
    logging.info(f"Grabbed value '{grabbed_value}' from selector '{selector}'")
    return grabbed_value


def get_attr_value_from_element(selector: Selector, attr_name: str) -> str:
    if is_element_not_exists(selector):
        logging.warning(f"Can't grab text from selector '{selector}': element do not exist.")
        return ""

    element = locate_element(selector)

    grabbed_value = element.get_attribute(attr_name)
    logging.info(f"Grabbed value '{grabbed_value}' from selector '{selector}' and attribute '{attr_name}'")
    return grabbed_value


# Input in fields methods


def input_in_field(
    selector: Selector,
    string_to_input: str,
    need_check_for_correctly_input: bool = True,
    need_click_by_html: bool = False,
    need_clear_field_with_keyboard: bool = False,
):
    click_by_html(selector) if need_click_by_html else click(selector)
    clear_field_with_keyboard(selector) if need_clear_field_with_keyboard else clear_field(selector)
    logging.info(f"Inputting string '{string_to_input}' in field with selector '{selector}'")
    send_chars(
        selector=selector,
        chars=string_to_input,
        need_check_for_correctly_input=need_check_for_correctly_input,
    )


def input_in_field_by_char(selector: Selector, string_to_input: str, need_click_by_html: bool = False):
    """Input string to field by char without check for correctly input"""
    click_by_html(selector) if need_click_by_html else click(selector)
    clear_field(selector)
    logging.info(f"Inputting string '{string_to_input}' in field with selector '{selector}' by char")
    send_chars_by_char(selector=selector, chars=string_to_input)


def send_chars(selector: Selector, chars: str, need_check_for_correctly_input: bool = True):
    logging.info(f"Sending chars '{chars}' in field with selector '{selector}'")
    element = locate_element(selector)
    element.send_keys(chars)

    if need_check_for_correctly_input:
        for i in range(1, 3):
            try:
                element_value = grab_text_from_element(selector)
            except Exception:
                element_value = ""
            if element_value == chars:
                return
            logging.info(
                f"Incorrectly send chars '{chars}' in field with selector {selector} for {i} attempt. "
                f"Trying sending chars by each char"
            )
            clear_field_with_keyboard(selector)
            send_chars_by_char(selector=selector, chars=chars)


def send_chars_by_char(selector: Selector, chars: str):
    logging.info(f"Sending chars '{chars}' by each char in field with selector '{selector}'")
    element = locate_element(selector)
    for char in chars:
        element.send_keys(char)
        # Sleep in 0.1 second for stability in Chrome
        sleep(0.1)


def send_keys(selector: Selector, text: str):
    logging.info(f"Sending chars '{text}' by each char in field with selector '{selector}'")
    element = locate_element(selector)
    element.send_keys(text)


def clear_field(selector: Selector):
    logging.info(f"Clearing field with selector '{selector}'")
    locate_element(selector).clear()


def clear_field_with_keyboard(selector: Selector):
    logging.info(f"Clearing field with selector '{selector}' with keyboard")
    send_chars(selector, Keys.CONTROL + "a", need_check_for_correctly_input=False)
    send_chars(selector, Keys.DELETE, need_check_for_correctly_input=False)


# Checking state methods


def is_element_exists(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' exists")
    return len(locate_elements(selector)) > 0


def is_element_not_exists(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' not exists")
    return len(locate_elements(selector)) == 0


def is_element_visible(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' visible")
    if is_element_exists(selector):
        return locate_element(selector).is_displayed()
    return False


def is_element_not_visible(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' not visible")
    if is_element_exists(selector):
        return not locate_element(selector).is_displayed()
    return True


def is_element_selected(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' selected")
    return locate_element(selector).is_selected()


def is_element_enabled(selector: Selector) -> bool:
    logging.info(f"Check if an element '{selector}' enabled")
    return locate_element(selector).is_enabled()


# Locate element or elements methods


def get_elements_count(css_selector: Selector) -> int:
    elements_count = len(locate_elements(css_selector))
    logging.info(f"Count of elements with selector '{css_selector}' is {str(elements_count)}")
    return elements_count


def locate_element(css_selector: Selector) -> WebElement:
    try:
        return driver.instance.find_element(by=By.CSS_SELECTOR, value=str(css_selector))
    except NoSuchElementException:
        raise UCException(
            f"Can not find selector: '{css_selector}'. " f"For information, at this time only CSS selectors allowed."
        )


def locate_element_by_text(text: str) -> WebElement:
    try:
        return driver.instance.find_element(By.LINK_TEXT, value=str(text))
    except NoSuchElementException:
        raise UCException(f"Can't find text '{text}'.")


def locate_element_by_xpath(xpath: str) -> WebElement:
    try:
        return driver.instance.find_element(By.XPATH, value=str(xpath))
    except NoSuchElementException:
        raise UCException(f"Can't find element '{xpath}'.")


def locate_element_by_partial_text(text: str) -> WebElement:
    try:
        return driver.instance.find_element(By.PARTIAL_LINK_TEXT, value=str(text))
    except NoSuchElementException:
        raise UCException(f"Can't find text '{text}'.")


def locate_elements(css_selector: Selector) -> List[WebElement]:
    try:
        return driver.instance.find_elements(by=By.CSS_SELECTOR, value=str(css_selector))
    except NoSuchElementException:
        raise UCException(
            f"Can not find selector: '{css_selector}'. " f"For information, at this time only CSS selectors allowed."
        )


# Browser management methods


def reload_page():
    logging.info("Reloading page")
    driver.instance.refresh()
    waiting_actions.wait_for_load()


def go_back():
    logging.info("Go back in browser")
    driver.instance.back()
    waiting_actions.wait_for_load()


def get_current_url() -> TestingProjectUrlData:
    current_url: str = driver.instance.current_url
    logging.info(f"Got URL from browser: '{current_url=}'")
    return TestingProjectUrlData(current_url)


def get_netlock() -> str:
    """Возвращает netlock, основанный на текущем урле из браузера, иначе основанный на урле из ENV"""
    current_url: TestingProjectUrlData = get_current_url()
    if current_url.is_valid():
        return current_url.netlock

    logging.warning(f"Got bad '{current_url.origin_url=}' from browser, getting URL from ENV")
    return env.get_testing_project_url_data().netlock


# Switching windows methods


def open_new_window(need_close_current_window: bool = False):
    logging.info("Opening new window and switch to it")
    execute_js("window.open();")
    if need_close_current_window:
        close_current_window()

    switch_to_next_window()


def switch_to_next_window() -> bool:
    timeout = waiting_actions.get_waiting_timeout_from_env_if_necessary()
    logging.info(f"Switching to a new browser tab/window with timeout {timeout} seconds")
    try:
        old_handle = driver.instance.current_window_handle
    except Exception:
        old_handle = "no such window"

    try_count = 0
    while try_count < timeout:
        logging.info(f"Attempt {try_count} of switching to a new browser tab/window'")
        last_window = driver.instance.window_handles[-1]
        driver.instance.switch_to.window(last_window)

        if driver.instance.current_window_handle != old_handle:
            return True

        time.sleep(1)
        try_count += 1

    raise UCException(f"Could not switch to a new tab/windows for {timeout} seconds.")


def switch_to_first_window():
    logging.info("Switching to first window")
    first_window = driver.instance.window_handles[0]
    driver.instance.switch_to.window(first_window)


def switch_to_last_window():
    logging.info("Switching to last window")
    last_window = driver.instance.window_handles[-1]
    driver.instance.switch_to.window(last_window)


def close_current_window():
    logging.info("Closing current window")
    driver.instance.close()


# Resize window methods


def set_window_size(window_width: int, page_height: int):
    logging.info(f"Set window size to width: {str(window_width)} and height: {str(page_height)}")
    driver.instance.set_window_size(window_width, page_height)


def resize_window_to_full_page():
    """Resize window to full page size"""
    window_width = int(execute_js("return window.innerWidth"))
    page_height = int(execute_js("return document.body.scrollHeight"))
    # Add a few pixels so that the picture is not cropped from the bottom
    set_window_size(window_width, page_height + 250)
    # Some processes can be executing after resize, waiting for then
    waiting_actions.wait_for_load()


# Executing JS methods


def get_dom_object(css_selector: Selector, property_or_method_to_execute: str = None) -> str:
    return f"document.querySelector('{str(css_selector)}')" + (
        "" if property_or_method_to_execute is None else f".{property_or_method_to_execute}"
    )


def execute_js(js: str, *args):
    return driver.instance.execute_script(js, args)


def execute_async_script(js):
    return driver.instance.execute_async_script(js)
