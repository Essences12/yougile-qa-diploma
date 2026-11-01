
import re
from playwright.sync_api import Page, expect


BASE_URL = "https://app.yougile.com/"


# 1. Приложение открывается
def test_app_page_opens(page: Page):
    response = page.goto(BASE_URL)
    assert response is not None
    assert response.status < 500


# 2. Страница имеет заголовок YouGile
def test_page_has_title(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title(re.compile("yougile", re.I))


# 3. На странице отображается содержимое
def test_page_body_is_visible(page: Page):
    page.goto(BASE_URL)
    expect(page.locator("body")).to_be_visible()


# 4. Страница не пустая
def test_page_has_content(page: Page):
    page.goto(BASE_URL)
    expect(page.locator("body")).not_to_be_empty()


# 5. Проверка, что страница не показывает ошибку 404/500
def test_page_response_is_not_server_error(page: Page):
    response = page.goto(BASE_URL)
    assert response is not None
    assert response.status not in [404, 500, 502, 503]