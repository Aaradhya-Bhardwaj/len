from typing import Any

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from .exceptions import LinkException
from .extra_funcs import _add_time

# main function


def main(url: str, desc: bool = False) -> str:
    """Gets the given URL and returns the total time as a string.
    If desc is True, returns the time as 'hours:minutes:seconds';
    else returns it as '{hours} hours, {minutes} minutes and {seconds} seconds'
    """
    print(f"Link given:-\n>: {url}")
    if 'youtube.com' not in url or 'playlist?list' not in url:
        raise LinkException('Link must be a youtube playlist link.')

    options: Options = Options()
    options.headless = True

    driver: Chrome = Chrome(
        'F:\Chromedriver\chromedriver.exe', options=options)
    try:
        driver.get(url)

        aria_list: list[str] = [ele.get_attribute(
            'aria-label') for ele in driver.find_elements_by_class_name('ytd-thumbnail-overlay-time-status-renderer')]

        len_list = []

        for string in aria_list:
            if string is not None:
                len_list.append(
                    list(filter(lambda input: input.isnumeric(), string.split())))

    finally:
        driver.close()

    time: str = _add_time(len_list, desc=desc)

    return time
