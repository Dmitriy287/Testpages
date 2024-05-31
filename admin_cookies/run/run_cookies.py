from admin_cookies.tests.tests_cookies import *

@pytest.mark.smoke
def test_admin(page: Page, admin):
    admin()

@pytest.mark.smoke
def test_admin2(page: Page, admin2):
    admin2()

@pytest.mark.smoke
def test_admin3(page: Page, browser_context, admin3):
    admin3()
