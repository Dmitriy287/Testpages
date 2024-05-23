from testpages.config_playwright.config import *
from testpages.locators.locators_test_pages import *
from testpages.data.data_test_pages import *
from playwright.sync_api import expect


@pytest.fixture
def test_pages_one(page: Page):
    def test_pages_one_func():
        page.goto(data_test_pages)
        assert page.title() == 'Web Testing and Automation Practice Application Pages'
        page.click(locator_index)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/index.jpeg')
        page.click(locator_about)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/about.jpeg')
        page.mouse.wheel(0, 100)
    return test_pages_one_func

@pytest.fixture
def test_pages_web(page: Page):
    def test_pages_web_func():
        page.goto(data_test_pages)
        page.click(locator_basic)
        page.wait_for_timeout(1000)
        paragraph_text = page.locator(locator_paragraph).inner_text()
        print(paragraph_text)
        page.wait_for_timeout(2000)
        paragraph2_text = page.locator(locator_paragraph2).inner_text()
        print(paragraph2_text)
        page.wait_for_timeout(2000)
        page.click(locator_index)
        page.screenshot(path='screenshots/pages_web.jpeg')
    return test_pages_web_func


@pytest.fixture
def test_pages_attribute(page: Page):
    def test_pages_attribute_func():
        page.goto(data_test_pages)
        page.click(locator_attribute)
        page.wait_for_timeout(2000)
        page.click(locator_dom_attributes)
        dom_attributes_id = page.locator(locator_dom_attributes).get_attribute("class")
        assert dom_attributes_id == 'class-attribute'
        print(f'\n--- атрибут, Хорош: {dom_attributes_id} ---')
        page.screenshot(path='screenshots/attribute.jpeg')
        page.click(locator_add_another_attribute)
        page.wait_for_timeout(1000)
        page.wait_for_selector("#jsattributes")
        element_text = page.locator("#jsattributes").inner_text()
        print(element_text)
        assert page.inner_text('h1') == 'Element Attributes Examples'
        page.screenshot(path='screenshots/dynamic_attribute.jpeg')
        page.wait_for_selector("#jsautoattributes")
        element_text = page.locator("#jsautoattributes").inner_text()
        print(element_text)
        page.wait_for_timeout(1000)
    return test_pages_attribute_func


@pytest.fixture
def test_pages_locators(page: Page):
    def test_pages_locators_func():
        page.goto(data_test_pages)
        page.click(locators_find)
        page.wait_for_timeout(2000)
        page.click(locator_8_jump_to_para)
        page.wait_for_timeout(2000)
        page.mouse.wheel(0, 1000)
        d_paragraph_text1 = page.locator(locator_d_paragraph_text1).inner_text()
        print(d_paragraph_text1)
        page.wait_for_timeout(2000)
        page.click(locator_nested)
        page.click(locator_10_jump_to_para)
        page.click(locator_17_jump_to_para)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/locators.jpeg')
    return test_pages_locators_func

@pytest.fixture
def test_pages_webdriver(page: Page):
    def test_pages_webdriver_func():
        page.goto(data_test_pages)
        page.click(locator_webdriver)
        page.wait_for_timeout(2000)
        page.fill(locator_field_for_numbers, data_numbers)
        page.wait_for_timeout(2000)
        page.click(locator_button_server)
        page.wait_for_timeout(2000)
        page.click(locator_field)
        page.wait_for_timeout(3000)
        page.fill(locator_field, data_numbers2)
        page.click(locator_show_as_alert)
        page.wait_for_timeout(2000)
        page.click(locator_show_as_para)
        page.wait_for_timeout(2000)
        page.click(locator_show_from_link)
        page.wait_for_timeout(1000)
        page.screenshot(path='screenshots/webdriver.jpeg')
    return test_pages_webdriver_func

@pytest.fixture
def test_pages_table(page: Page):
    def test_pages_table_func():
        page.goto(data_test_pages)
        page.click(locator_table_test)
        page.wait_for_selector(locator_td)
        first_cell_text = page.query_selector("#mytable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)").inner_text()
        assert first_cell_text == "Alan"
        print(first_cell_text)
        four_cell_text = page.query_selector("#mytable > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(1)").inner_text()
        assert four_cell_text == "Douglas"
        print(four_cell_text)
        first_cell_number = page.query_selector("#mytable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)").inner_text()
        assert first_cell_number == "12"
        print(first_cell_number)
        page.wait_for_timeout(1000)
        rows = page.query_selector_all("//*[@id='mytable']")
        assert len(rows) > 0
        four_cell_number = page.query_selector("#mytable > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)").inner_text()
        assert four_cell_number == "42"
        page.screenshot(path='screenshots/table.jpeg')
    return test_pages_table_func


@pytest.fixture
def test_pages_table_dynamic(page: Page):
    def test_pages_table_dynamic_func():
        page.goto(data_test_pages)
        page.click(locator_table_test_dynamic)
        page.wait_for_timeout(1000)
        page.click(locator_table_data)
        page.wait_for_timeout(1000)
        page.fill(locator_field_data, data_name)
        page.wait_for_timeout(1000)
        page.fill(locator_caption, data_caption)
        page.fill(locator_id, data_id)
        page.click(locator_refresh_table)
        page.wait_for_timeout(3000)
        assert page.title() == 'Table HTML Tag - JavaScript Created'
        page.screenshot(path='screenshots/table_dynamic.jpeg')
        page.click(locator_index)
        page.wait_for_timeout(1000)
    return test_pages_table_dynamic_func


