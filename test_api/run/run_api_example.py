from test_api.test.test_api_example import *


@pytest.mark.smoke
def test_api_get_pet(page: Page, api_get_pet):
    api_get_pet()


@pytest.mark.smoke
def test_api_get_weather(page: Page, api_get_weather):
    api_get_weather()


def test_api_post_json(page: Page, api_post_json):
    api_post_json()

@pytest.mark.smoke
def test_api_new_pet(page: Page, api_new_pet):
    api_new_pet()

@pytest.mark.smoke
def test_api_find_pet(page: Page, api_find_pet):
    api_find_pet()


@pytest.mark.smoke
def test_delete_pet(page: Page, delete_pet):
    delete_pet()

@pytest.mark.smoke
def test_api_put_json(page: Page, api_put_json):
    api_put_json()

@pytest.mark.smoke
def test_api_patch_json(page: Page, api_patch_json):
    api_patch_json()