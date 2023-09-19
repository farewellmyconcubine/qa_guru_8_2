import pytest
from selene import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.open("https://www.google.com/")

@pytest.fixture(autouse=True)
def setting_browser():
    browser.driver.set_window_size(1920, 1080)

