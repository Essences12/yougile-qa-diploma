
import os
import requests
import pytest


BASE_URL = "https://yougile.com/api-v2"
TIMEOUT = 30


@pytest.fixture
def api_headers():
    """Заголовки для авторизованных запросов."""
    token = os.getenv("YOUGILE_TOKEN")

    if not token:
        pytest.fail("Не задана переменная YOUGILE_TOKEN")

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# 1. Получение профиля пользователя
def test_get_user_profile(api_headers):
    response = requests.get(
        f"{BASE_URL}/users/me",
        headers=api_headers,
        timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


# 2. Получение списка проектов
def test_get_projects(api_headers):
    response = requests.get(
        f"{BASE_URL}/projects",
        headers=api_headers,
        timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert isinstance(response.json(), (dict, list))


# 3. Получение списка задач
def test_get_tasks(api_headers):
    response = requests.get(
        f"{BASE_URL}/tasks",
        headers=api_headers,
        timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert isinstance(response.json(), (dict, list))


# 4. Проверка отказа при неправильном токене
def test_invalid_token():
    headers = {
        "Authorization": "Bearer invalid_test_token"
    }

    response = requests.get(
        f"{BASE_URL}/users/me",
        headers=headers,
        timeout=TIMEOUT
    )

    assert response.status_code == 401


# 5. Проверка отказа без токена
def test_missing_token():
    response = requests.get(
        f"{BASE_URL}/users/me",
        timeout=TIMEOUT
    )

    assert response.status_code == 401
