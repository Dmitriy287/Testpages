import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from test_api.data.data_api_example import *



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
def api_get_pet(page: Page):
    def api_get_pet_func():
        response = page.request.get(data_get_pet)
        page.wait_for_timeout(1000)
        assert response.ok
        assert response.status == 200
        body = response.json()
        assert body["name"] == data_pet_name
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"Имя: {body['name']}")
    return api_get_pet_func

@pytest.fixture
def api_get_weather(page: Page):
    def api_get_weather_func():
        zip = "95050"
        units = "imperial"
        appid = "8d3f4ca3fe57058a39b58b2a30945699"
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip}&units={units}&appid={appid}"
        response = page.request.get(url)
        page.wait_for_timeout(1000)
        assert response.ok
        assert response.status == 200
        body = response.json()
        assert body["cod"] == 200
        assert body["name"] == 'Santa Clara'
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"Имя: {body['name']}")
        print(f"Часовой пояс: {body['timezone']}")
    return api_get_weather_func

@pytest.fixture
def api_post_json(page: Page):
    def api_post_json_func():
        response = page.request.post(data_post_url, data=data_post_json)
        assert response.ok
        assert response.status == 200
        body = response.json()
        body_booking = body['booking']
        assert body_booking['firstname'] == "Jim"
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"bookingid: {body["bookingid"]}")
        print(f"Имя: {body_booking["firstname"]}")
    return api_post_json_func


@pytest.fixture
def api_new_pet(page: Page):
    def api_new_pet_func():
        response = page.request.post(data_add_pet, data=data_response_body)
        assert response.ok
        assert response.status == 200
        body = response.json()
        body_pet = body
        assert body_pet['name'] == "cheburek"
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"Имя: {body['name']}")
        print(f"petid: {body["id"]}")
        print(f"status: {body["status"]}")
    return api_new_pet_func


@pytest.fixture
def api_find_pet(page: Page):
    def api_find_pet_func():
        response = page.request.get(data_find_pet_id)
        page.wait_for_timeout(1000)
        assert response.ok
        assert response.status == 200
        body = response.json()
        assert body["id"] == 68
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"Имя: {body['name']}")
        print(f"petid: {body["id"]}")
    return api_find_pet_func


@pytest.fixture
def delete_pet(page: Page):
    def delete_pet_func():
        response = page.request.delete(data_delete_pet, data=data_delete)
        page.wait_for_timeout(2000)
        assert response.ok
        assert response.status == 200
        assert response.ok
        body = response.json()
        assert body["message"] == "68"
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"cообщение: {["Pet удалён"]}")
    return delete_pet_func


@pytest.fixture
def api_put_json(page: Page):
    def api_put_json_func():
        response = page.request.post(data_post_url, data=data_put_json)
        assert response.ok
        assert response.status == 200
        body = response.json()
        body_booking = body['booking']
        assert body_booking['firstname'] == "James"
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"bookingid: {body['bookingid']}")
        print(f"Имя: {body_booking['firstname']}")
        print(f"Заказ: {body_booking['additionalneeds']}")
    return api_put_json_func


@pytest.fixture
def api_patch_json(page: Page):
    def api_patch_json_func():
        response = page.request.patch(data_patch_url, data=data_patch_json)
        assert response.ok
        assert response.status == 200
        body = response.json()
        body_booking = body['booking']
        assert body_booking['firstname'] == "James"
        print("Инфа о тесте:")
        print(f"Состояние: {response.ok}")
        print(f"Статус: {response.status}")
        print(f"bookingid: {body['bookingid']}")
        print(f"Имя: {body_booking['firstname']}")
        print(f"Заказ: {body_booking['additionalneeds']}")
    return api_patch_json_func