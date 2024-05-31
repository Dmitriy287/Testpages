import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from html5_page.data.data_html5 import *
from html5_page.locators.locators_html5 import *


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
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
def colour(page: Page):
    def colour_func():
        page.goto(data_html5)
        page.wait_for_timeout(2000)
        page.click(locator_colour)
        for _ in range(4):
            page.keyboard.press("Tab")
        page.keyboard.type("128")
        page.keyboard.press("Enter")
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        text = page.query_selector(locator_colour2).inner_text()
        assert text == '#008000'
        page.screenshot(path="screenshots/html5_form_colour.png")
    return colour_func

@pytest.fixture
def email(page: Page):
    def email_func():
        page.goto(data_html5)
        page.wait_for_timeout(2000)
        page.fill(locator_email, data_email)
        input_value = page.input_value(locator_email)
        assert input_value == data_email, f"Expected email '{data_email}', but got '{input_value}'"
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/html5_email.png")
    return email_func

@pytest.fixture
def number(page: Page):
    def number_func():
        page.goto(data_html5)
        page.wait_for_timeout(2000)
        page.click(locator_number)
        page.keyboard.press("ArrowDown")
        input_value = page.input_value(locator_number)
        assert input_value == data_number, f"Expected number '{data_number}', but got '{input_value}'"
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/html5_number.png")
    return number_func

@pytest.fixture
def date(page: Page):
    def date_func():
        page.goto(data_html5)
        # Ожидаем появления элемента даты
        page.click(locator_date)
        page.wait_for_timeout(2000)
        # Заполняем поле даты
        page.keyboard.press("Space")
        page.wait_for_timeout(2000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
        input_value = page.input_value(locator_date)
        assert input_value == data_date, f"Expected date '{data_date}', but got '{input_value}'"
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/html5_date.png")
    return date_func


@pytest.fixture
def date_time(page: Page):
    def date_time_func():
        page.goto(data_html5)
        page.click(locator_date_time)
        page.wait_for_timeout(2000)
        page.keyboard.press("Space")
        page.wait_for_timeout(2000)
        page.keyboard.press("Tab")
        page.wait_for_timeout(1000)
        page.keyboard.press("Tab")
        page.wait_for_timeout(1000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)
        page.keyboard.press("Tab")
        page.wait_for_timeout(1000)
        for _ in range(5):  # Прокрутить вниз 5 раз
            page.keyboard.press("ArrowDown")
        page.keyboard.press("Tab")
        for _ in range(12):
            page.keyboard.press("ArrowDown")
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        text = page.query_selector('#_valuedatetime').inner_text()
        assert text == "2024-05-31T06:13"
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/html5_date_time.png")
    return date_time_func


@pytest.fixture
def month(page: Page):
    def month_func():
        page.goto(data_html5)
        page.wait_for_timeout(2000)
        page.click(locator_month)
        page.keyboard.press("Space")
        page.wait_for_timeout(2000)
        for _ in range(3):  # Прокрутить вниз 5 раз
            page.keyboard.press("ArrowRight")
        page.wait_for_timeout(3000)
        page.keyboard.press("Enter")
        input_value = page.input_value(locator_month)
        assert input_value == data_month, f"Expected date '{data_month}', but got '{input_value}'"
        page.click(locator_submit)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/html5_month.png")
    return month_func

