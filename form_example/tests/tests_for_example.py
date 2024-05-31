import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from form_example.data.data_form_example import *
from form_example.locators.locators_for_example import *


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
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def usr_pass_fill(page: Page):
    def usr_pass_fill_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(2000)
        page.locator(locator_username).fill(data_username)
        page.locator(locator_password).fill(data_password)
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        text = page.query_selector("#_valueusername").inner_text()
        assert text == 'Диман'
        page.screenshot(path="screenshots/usr_pass_fill.png")
    return usr_pass_fill_func

@pytest.fixture
def textarea(page: Page):
    def textarea_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        def key_textarea(locator_textarea: str, data_textarea: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(data_textarea)
        key_textarea(locator_textarea, data_textarea)
        page.wait_for_timeout(3000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        text = page.query_selector("#_valuecomments").inner_text()
        assert text == 'Compliment'
        page.screenshot(path="screenshots/textarea.png")
    return textarea_func

@pytest.fixture
def set_filename(page: Page):
    def set_filename_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', data_filename_path_2)
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        set_filename = page.locator(locator_file).inner_text()
        assert set_filename == 'filename.txt'
        page.screenshot(path="screenshots/set_filename.png")
    return set_filename_func

@pytest.fixture
def checkbox_items(page: Page):
    def checkbox_items_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.check(locator_checkbox_1)
        page.wait_for_timeout(1000)
        page.click(locator_submit)#_valuecheckboxes0
        page.wait_for_timeout(1000)
        text = page.query_selector("#_valuecheckboxes0").inner_text()
        assert text == 'cb1'
        page.screenshot(path="screenshots/set_filename.png")
    return checkbox_items_func

@pytest.fixture
def radio_items(page: Page):
    def radio_items_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.check(locator_radio_1)
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        hidenfield = page.locator(locator_hidenfield).inner_text()
        assert hidenfield == 'Hidden Field Value'
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/radio.png")
    return radio_items_func

@pytest.fixture
def multiple_select_values(page: Page):
    def multiple_select_values_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_multiple_select_values)
        page.select_option(locator_multiple_select_values, value=["Selection Item 3"])
        page.wait_for_timeout(4000)
        page.mouse.wheel(0, 100)
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        text = page.query_selector("#_valuemultipleselect0").inner_text()
        assert text == 'ms3'
        page.screenshot(path="screenshots/multiple_select_values.png")
    return multiple_select_values_func

@pytest.fixture
def dropdown(page: Page):
    def dropdown_func():
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_dropdown)
        page.select_option(locator_dropdown, value=["Drop Down Item 2"])
        page.wait_for_timeout(2000)
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/set_dropdown.png")
    return dropdown_func