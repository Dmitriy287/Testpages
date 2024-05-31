from html5_page.tests.tests_html5 import *

@pytest.mark.smoke
def test_colour(page: Page, colour):
    colour()

@pytest.mark.smoke
def test_email(page: Page, email):
    email()

@pytest.mark.smoke
def test_number(page: Page, email, number):
    number()

@pytest.mark.smoke
def test_date(page: Page, date):
    date()

@pytest.mark.smoke
def test_date_time(page: Page, date_time):
    date_time()

@pytest.mark.smoke
def test_month(page: Page, month):
        month()