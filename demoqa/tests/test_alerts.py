from playwright.sync_api import sync_playwright, Page, BrowserContext
import pytest
from demoqa.locators.locator_alert import *
from demoqa.data.data_alerts import *
from playwright.sync_api import expect

@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.firefox.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def show_alert_box(page: Page):
    def show_alert_box_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        page.click(locator_alert_box)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/show_alert_box.jpeg')
    return show_alert_box_func

@pytest.fixture
def show_confirm_box(page: Page):
    def show_confirm_box_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        page.click(locator_confirm_box)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/show_confirm_box.jpeg')
    return show_confirm_box_func
