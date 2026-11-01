YouGile QA Diploma Project
Описание
Дипломный проект по тестированию веб-приложения YouGile.
Технологии
Python
Pytest
Requests
Playwright
Allure Report
Insomnia
Структура проекта
tests/api/ — API-автотесты
tests/ui/ — UI-автотесты
requirements.txt — зависимости Python
.gitignore — исключения Git
Установка
py -m pip install -r requirements.txt
py -m playwright install
API Testing — Insomnia
Для ручного API-тестирования используется Insomnia.
Коллекция содержит запросы для проверки:
- авторизации;
- получения информации о пользователе;
- получения списка проектов;
- создания проекта;
- получения списка задач;
- негативных сценариев авторизации.
Файл коллекции: YouGile_Insomnia_Collection.json.
Для выполнения запросов необходимо настроить переменные окружения Insomnia. Токены и пароли не хранятся в репозитории.
