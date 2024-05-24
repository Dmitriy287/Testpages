from playwright.sync_api import sync_playwright, Page, BrowserContext
import pytest
from alerts.locators.locator_alert import *
from alerts.data.data_alerts import *
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
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.accept()
        page.on('dialog', alert_dialog)
        page.click(locator_alert_box)
        page.click(locator_you_trigered)
        you_trigered = page.locator(locator_you_trigered).inner_text()
        assert you_trigered == 'You triggered and handled the alert dialog'
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_alert_box.png")
    return show_alert_box_func

@pytest.fixture
def show_confirm_box_accept(page: Page):
    def show_confirm_box_accept_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.accept()
        page.on('dialog', alert_dialog)
        page.click(locator_confirm_box)
        you_click = page.locator(locator_you_click).inner_text()
        assert you_click == 'You clicked OK, confirm returned true.'
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_confirm_accept_box.png")
    return show_confirm_box_accept_func

@pytest.fixture
def show_confirm_box_dismiss(page: Page):
    def show_confirm_box_dismiss_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog(dialog):
            print(dialog.message)
            dialog.dismiss()
        page.on('dialog', alert_dialog)
        page.click(locator_confirm_box)
        you_click = page.locator(locator_you_click).inner_text()
        assert you_click == 'You clicked Cancel, confirm returned false.'
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_confirm_dismiss_box.png")
    return show_confirm_box_dismiss_func

@pytest.fixture
def show_prompt_box(page: Page):
    def show_prompt_box_func():
        page.goto(data_page_alerts)
        page.wait_for_timeout(1000)
        def alert_dialog_prompt(dialog):
            print(dialog.message)
            dialog.accept(data_alert_prompt)
        page.on('dialog', alert_dialog_prompt)
        page.click(locator_prompt_box)
        prompt_click = page.locator(locator_you_click_prompt).inner_text()
        assert prompt_click == "You clicked OK. 'prompt' returned Hello"
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/show_prompt_box.png", full_page=True)
    return show_prompt_box_func
