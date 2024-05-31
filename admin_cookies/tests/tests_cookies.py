import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from admin_cookies.data.data_cookies import *
from admin_cookies.locators.locators_cookies import *



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
def admin(page: Page):
    def admin_func():
        page.goto(data_cookies)
        page.wait_for_timeout(2000)
        page.fill(locator_username, data_username)
        page.fill(locator_password, data_password)
        page.click(locator_login)
        page.wait_for_timeout(3000)
        page.context.clear_cookies(name=data_cookies_admin_name)
        page.wait_for_timeout(2000)
        page.reload()
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/admin_cookies.png")
    return admin_func

@pytest.fixture
def admin2(page: Page):
    def admin2_func():
        page.goto(data_cookies)
        page.wait_for_timeout(2000)
        page.fill(locator_username, data_username)
        page.fill(locator_password, data_password)
        page.click(locator_login)
        page.wait_for_timeout(3000)
        page.context.cookies()
        page.wait_for_timeout(2000)
        page.reload()
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/admin_cookies2.png")
    return admin2_func


@pytest.fixture
def admin3(page: Page, browser_context):
    def admin3_func():
        page.goto(data_cookies)
        page.wait_for_timeout(2000)
        page.fill(locator_username, data_username)
        page.fill(locator_password, data_password)
        browser_context.add_cookies([
            {
                'name': 'loggedin',
                'value': 'Admin',
                'domain': 'https://testpages.eviltester.com/styled/cookies/adminlogin.html',
                'path': '/',
                'httpOnly': False,
                'secure': False,
                'sameSite': 'Lax'
            }

        ])
        page.click(locator_login)
        page.wait_for_timeout(3000)
        page.wait_for_timeout(2000)
        page.reload()
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/admin_cookies2.png")
    return admin3_func
