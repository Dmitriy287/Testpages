from testpages.tests.test_pages import *

@pytest.mark.smoke
def testpages_one(page: Page, test_pages_one):
    test_pages_one()

@pytest.mark.smoke
def testpages_web(page: Page, test_pages_web):
    test_pages_web()

@pytest.mark.smoke
def testpages_attribute(page: Page, test_pages_attribute):
    test_pages_attribute()


@pytest.mark.smoke
def testpages_locators(page: Page, test_pages_locators):
    test_pages_locators()


@pytest.mark.smoke
def testpages_webdriver(page: Page, test_pages_webdriver):
    test_pages_webdriver()


@pytest.mark.smoke
def testpages_table(page: Page, test_pages_table):
    test_pages_table()

@pytest.mark.smoke
def testpages_table_dynamic(page: Page, test_pages_table_dynamic):
    test_pages_table_dynamic()


